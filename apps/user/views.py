import requests
from rest_framework import generics, response, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from random import randint
from datetime import datetime
from django.conf import settings
from main.models import Season, VoiceTime
from main.paginations import CustomLimitOffsetPagination
from .utils import send_sms, send_email_code
from .serializers import RegisterSerializer, LoginSerializer, VerifyPhoneSerializer, UserSerializer, \
    ApplicationSerializer, TeacherSerializer, ParticipantSerializer, ParticipantDetailSerializer, \
    TeacherDetailSerializer, NotificationSerializer, WinnerSerializer
from .models import User, VerifyPhone, Application, Teacher, Participant, Notification, Winner


class WinnerAPI(generics.GenericAPIView):
    serializer_class = WinnerSerializer
    queryset = Winner.objects.all()

    def get(self, request, *args, **kwargs):
        obj = self.queryset.first()
        serializer = WinnerSerializer(obj)
        return response.Response(serializer.data)


class NotificationAPI(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        Notification.objects.filter(id=self.request.query_params.get('id')).delete()
        return response.Response({'success': True})


# class VotingAPI(generics.GenericAPIView):
#     serializer_class = VoiceSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request, *args, **kwargs):
#         time = VoiceTime.objects.filter(is_active=True, time__gt=datetime.now().astimezone()).first()
#         participant = Participant.objects.filter(id=request.data['participant']).first()
#         season = Season.objects.filter(is_active=True).first()
#         pts = Participant.objects.filter(is_active=True, season=season, teacher=participant.teacher)
#         for i in pts:
#             if Voice.objects.filter(user=self.request.user, time=time, participant=i).exists():
#                 return response.Response(
#                     {'success': False, 'message_uz': "Siz avval shu ustozni boshqa ishtirokchisiga ovoz bergansiz!",
#                      'message_ru': 'Вы сначала проголосовали за этого наставника за другого участника!',
#                      'message_en': "You voted for this mentor for another participant first!"}, status=400)
#         data = self.request.data
#         data['time'] = time.id
#         data['user'] = self.request.user.id
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response({'success': True})


class ApplicationAPI(generics.GenericAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        season = Season.objects.filter(is_active=True).first()
        if Application.objects.filter(user=self.request.user, season_id=season.id).exists():
            return response.Response({'success': False}, status=400)
        data = self.request.data
        data['user'] = self.request.user.id
        data['season'] = season.id
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        txt = f"Ism: {data['first_name']}\n"
        txt += f"Familiya: {data['last_name']}\n"
        txt += f"Telefon raqam: {data['phone']}\n"
        if data['for_kids']:
            txt += f"Bolalar uchun\n"
        txt += f"Ariza kelib tushgan vaqt: {serializer.data['created_at']}"
        requests.get(files={'video': open(serializer.data['video_path'], 'rb')},
                     params={'chat_id': settings.CHAT_ID, 'caption': txt},
                     url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendVideo")
        data = dict()
        data['sent'] = True
        data['checking'] = None
        data['accepted'] = None
        return response.Response(data)

    def get(self, request, *args, **kwargs):
        season = Season.objects.filter(is_active=True).first()
        obj = Application.objects.filter(user=self.request.user, season_id=season.id).last()
        if obj is None:
            return response.Response({'success': False}, status=400)
        data = dict()
        data['sent'] = True
        if obj.status == 1:
            data['checking'] = None
            data['accepted'] = None
        if obj.status == 2:
            data['checking'] = True
            data['accepted'] = None
        elif obj.status == 3:
            data['checking'] = True
            data['accepted'] = True
        elif obj.status == 4:
            data['checking'] = True
            data['accepted'] = False
        return response.Response(data)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        code = str(randint(10000, 100000))
        if request.data.get('phone', None):
            phone = self.request.data['phone']
            user = User.objects.filter(phone=phone).first()
            if user:
                return response.Response(
                    {'success': False, 'message_uz': 'foydalanuvchi allaqachon mavjud',
                     'message_ru': 'пользователь уже существует', 'message_en': "the user already exists"}, status=400)
            send_sms(phone, code)
            VerifyPhone.objects.create(phone=phone, code=code)
        elif request.data.get('email', None):
            email = self.request.data['email']
            user = User.objects.filter(email=email).first()
            if user:
                return response.Response(
                    {'success': False, 'message_uz': 'foydalanuvchi allaqachon mavjud',
                     'message_ru': 'пользователь уже существует', 'message_en': "the user already exists"}, status=400)
            send_email_code(email, code)
            VerifyPhone.objects.create(phone=email, code=code)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'success': True, 'message_ru': 'проверочный код был отправлен на ваш телефон',
                                  'message_uz': 'tasdiqlash kodi telefoningizga yuborildi',
                                  'message_en': "The verification code has been sent to your phone"}, status=201)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        code = str(randint(10000, 100000))
        if request.data['phone']:
            phone = self.request.data['phone']
            user = User.objects.filter(phone=phone).first()
            if not user:
                return response.Response({'success': False, 'message_ru': 'Вы не зарегистрированы!',
                                          'message_uz': "Siz ro'yxatdan o'tmagansiz!",
                                          'message_en': "You are not registered!"}, status=400)
            send_sms(phone, code)
            VerifyPhone.objects.create(phone=phone, code=code)
        elif request.data['email']:
            email = self.request.data['email']
            user = User.objects.filter(email=email).first()
            if not user:
                return response.Response({'success': False, 'message_ru': 'Вы не зарегистрированы!',
                                          'message_uz': "Siz ro'yxatdan o'tmagansiz!",
                                          'message_en': "You are not registered!"}, status=400)
            send_sms(email, code)
            VerifyPhone.objects.create(phone=email, code=code)
        return response.Response({'success': True, 'message_ru': 'проверочный код был отправлен',
                                  'message_uz': 'tasdiqlash kodi yuborildi',
                                  'messgae_en': "the verification code was sent"})


class VerifyPhoneAPI(generics.GenericAPIView):
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data.get('phone', None)
        email = self.request.data.get('email', None)
        code = self.request.data.get('code', None)
        if email:
            user = User.objects.filter(email=email).first()
            v = VerifyPhone.objects.filter(phone=email, code=code).first()
        elif phone:
            user = User.objects.filter(phone=phone).first()
            v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        else:
            return response.Response(
                {'success': False, 'message_ru': 'Неверный проверочный код!',
                 'message_uz': "Email ham telefon ham yuq", 'messgae_en': "Invalid verification code!"}, status=400)
        if v:
            v.delete()
            data = UserSerializer(user).data
            token = RefreshToken.for_user(user)
            auth_token = Token.objects.filter(user=user).first()
            data['token'] = auth_token.key
            data['access_token'] = str(token.access_token)
            data['refresh_token'] = str(token)
            return response.Response(data)
        return response.Response(
            {'success': False, 'message_ru': 'Неверный проверочный код!', 'message_uz': "Tasdiqlash kodi noto'g'ri!",
             'messgae_en': "Invalid verification code!"}, status=400)


class UserAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.request.user).data
        return response.Response(serializer)


class UserDeleteAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        self.request.user.delete()
        return response.Response({'success': True})


class TeacherAPI(generics.GenericAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        data = list()
        season = Season.objects.filter(is_active=True).first()
        if season is None:
            return response.Response({'success': False, 'message_ru': 'В настоящее время сезон активов недоступен!',
                                      'message_uz': "Hozirda aktiv season mavjud emas!",
                                      'message_en': "The asset season is currently unavailable!"}, status=400)
        if self.request.user:
            user_id = self.request.user.id
        else:
            user_id = None
        for i in Teacher.objects.filter(season=season).all():
            dt = TeacherSerializer(i).data
            ls = list()
            for j in i.participants.filter(season=season):
                d = ParticipantSerializer(j).data
                # if Voice.objects.filter(user_id=user_id, participant=j).exists():
                #     d['was_voted'] = True
                # else:
                #     d['was_voted'] = False
                ls.append(d)
            dt['participants'] = ls
            data.append(dt)
        return response.Response(data)


class TeacherFilterAPI(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_queryset(self):
        return Teacher.objects.filter(season_id=self.request.query_params.get('season'))


class ParticipantAPI(generics.ListAPIView):
    serializer_class = ParticipantSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        teacher = self.request.query_params.get('teacher', None)
        if teacher is None:
            return Participant.objects.filter(season_id=self.request.query_params.get('season'))
        else:
            return Participant.objects.filter(season_id=self.request.query_params.get('season'), teacher_id=teacher)


class TeacherDetailAPI(generics.RetrieveAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = TeacherDetailSerializer(obj).data
        data['participants'] = ParticipantSerializer(obj.participants.all(), many=True).data
        return response.Response(data)


class ParticipantDetailAPI(generics.RetrieveAPIView):
    serializer_class = ParticipantDetailSerializer
    queryset = Participant.objects.all()
