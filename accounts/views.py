from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.twilio_utils import send_verification_code, verify_code
from accounts.models import UserAccount


class VerifyPhoneView(APIView):
    def post(self, request):
        # get the phone number from the request data
        phone_number = request.data.get('phone_number')

        # send a verification code to the phone number
        verification_sid = send_verification_code(phone_number)

        # return the verification SID to the client
        return Response({'verification_sid': verification_sid})

    def put(self, request):
        # get the phone number and verification code from the request data
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')

        # verify the code
        is_valid = verify_code(phone_number, verification_code)

        if is_valid:
            user = UserAccount.objects.get(phone_number=phone_number)
            user.is_verified = True

        # return whether the code is valid to the client
        return Response({'is_valid': is_valid})

