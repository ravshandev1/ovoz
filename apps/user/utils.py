import requests
from django.conf import settings
from django.core.mail import EmailMessage
def send_email_code(email, code):
    subject = "OVOZ"
    body = f"Hi! This is verification code {code} from OVOZ"
    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    email.send()

def send_sms(phone: str, code: str):
    token = requests.post(url='https://notify.eskiz.uz/api/auth/login',
                          data={'email': settings.SMS_EMAIL, 'password': settings.SMS_PASSWORD})
    headers = {
        "Authorization": f"Bearer {token.json()['data']['token']}"
    }
    if phone.startswith('+79'):
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'country_code': "KZ",
            'unicode': '0'
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send-global', data=data, headers=headers)
    elif phone.startswith('+7'):
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'country_code': "RU",
            'unicode': '0'
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send-global', data=data, headers=headers)
    elif phone.startswith('+994'):
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'country_code': "AZ",
            'unicode': '0'
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send-global', data=data, headers=headers)
    elif phone.startswith('+992'):
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'country_code': "TJ",
            'unicode': '0'
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send-global', data=data, headers=headers)
    elif phone.startswith('+996'):
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'country_code': "KG",
            'unicode': '0'
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send-global', data=data, headers=headers)
    else:
        data = {
            'mobile_phone': phone,
            'message': f"The Voice uz mobil ilovasiga kirish uchun tasdiqlash kodi: {code} Confirmation code to access The Voice uz mobile app: {code} Код подтверждения для входа в мобильное приложение The Voice uz: {code}",
            'from': "4546"
        }
        requests.post(url='https://notify.eskiz.uz/api/message/sms/send', data=data, headers=headers)
