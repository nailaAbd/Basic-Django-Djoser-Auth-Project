from twilio.rest import Client
from django.conf import settings

def send_verification_code(phone_number):
    # create a Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # generate a verification code
    verification = client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verifications.create(to=phone_number, channel='sms')

    return verification.sid

def verify_code(phone_number, code):
    # create a Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # verify the code
    verification_check = client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verification_checks.create(to=phone_number, code=code)

    return verification_check.status == 'approved'
