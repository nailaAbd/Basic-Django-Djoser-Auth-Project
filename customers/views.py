from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from customers.permissions import IsObjectOwner
from rest_framework import status
import requests
import json
from customers.serializers import (
    CardSerializer,
    UtilitySerializer,
    UtilityProfileSerializer,
    ConnectedBankSerializer,
    PaymentCycleSerializer,
)
from customers.models import (
    Card,
    Utility,
    UtilityProfile,
    ConnectedBank,
    PaymentCycle
)
from accounts.models import UserAccount
from dotenv import load_dotenv
import os
load_dotenv()



SUPER_CONTROL_IP_ADDRESS = os.getenv('SUPER_CONTROL_IP_ADDRESS')


# class AccountViewSet(ModelViewSet):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#     # permission_classes = [IsAccountAdminOrReadOnly]


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = []


class UtilityViewSet(ModelViewSet):
    queryset = Utility.objects.all()
    serializer_class = UtilitySerializer
    permission_classes = []


class UtilityProfileViewSet(ModelViewSet):
    queryset = UtilityProfile.objects.all()
    serializer_class = UtilityProfileSerializer
    permission_classes = []


class ConnectedBankViewSet(ModelViewSet):
    queryset = ConnectedBank.objects.all()
    serializer_class = ConnectedBankSerializer
    permission_classes = []
    banks = requests.post(f'{SUPER_CONTROL_IP_ADDRESS}/banks/get-banks')

    def post(self, request):
        obj_data = request.data
        serializer = self.serializers_class(data=obj_data)
        serializer.is_valid(raise_exception=True)
        try:
            obj = ConnectedBank.objects.create(
                    user = serializer.validated_data.get('user'),
                    bank_id = serializer.validated_data.get('bank_id'),
                    bank_name = serializer.validated_data.get('bank_name'),
                    account_number = serializer.validated_data.get('account_number')
            )
        except IntegrityError:
            return Response("This bank account is already connected.",
                status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        return Response(response, status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        print("************")
        user = UserAccount.objects.get(id=request.data.get('user'))
        first_name = user.first_name
        last_name = user.last_name
        account_number = request.data.get('account_number')
        bank_id = request.data.get('bank_name')
        phone_number = str(user.phone_number).replace("+251", "0")
        print(first_name, last_name, phone_number)


        connect_bank_response = requests.post(f'{SUPER_CONTROL_IP_ADDRESS}/customers/connect-bank/', json={
            "first_name": first_name,
            "last_name": last_name,
            "account_number": account_number,
            "bank_id": bank_id,
            "phone_number": phone_number
        })
        
        # connect_bank_response = requests.post(f'{SUPER_CONTROL_IP_ADDRESS}/customers/connect-bank/', json={
        #     "first_name": "Abdi",
        #     "last_name": "Adem",
        #     "account_number": "1000154410728",
        #     "bank_id": "0644a363-7c50-75a7-8000-608df169e369",
        #     "phone_number": "0947952012"
        # })

        if connect_bank_response.status_code != 200:
            return Response({'error': connect_bank_response.json()['detail']}, status=connect_bank_response.status_code)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        bank_choices = dict(serializer.fields['bank_name'].choices)
        validated_data['bank_id'] = validated_data['bank_name']
        validated_data['bank_name'] = bank_choices[validated_data['bank_name']]
        serializer.save()


class PaymentCycleViewSet(ModelViewSet):
    queryset = PaymentCycle.objects.all()
    serializer_class = PaymentCycleSerializer
    permission_classes = []

# super-control

class GetDetailBank(APIView):
    def get(self, request):
        bank_id = request.data.get('bank_id')
        response = requests.get(f"http://localhost:1100/banks/{bank_id}")
        return Response(json.loads(response.text))


class GetBanks(APIView):
    def get(self, request):
        response = requests.get(f"http://localhost:1100/banks")
        return Response(json.loads(response.text))


class ReturnConnectedBAnks(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        connected_banks = ConnectedBank.objects.filter(user__id=customer_id)
        print(connected_banks)
        for i in connected_banks:
            print(i.bank_id)
        serializer = ConnectedBankSerializer(connected_banks, many=True)
        return Response(serializer.data)


class VerifyPin(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        pin = request.data.get('pin')
        card = Card.objects.get(user__id=customer_id)
        if card.pin != pin:
            print("True")
            return Response({'error': 'Incorrect PIN'}, status=400)

        serializer = CardSerializer(card)
        return Response({"status": "Correct PIN"})


class GetConnectedBanksRequest(APIView):
    
    def post(self, request):
        # Retrieve the data sent in the POST request from the external API
        data = request.data

        # Retrieve the parameters sent with the request
        customer_id = request.GET.get('customer_id') # replace with your parameter name
        # parameter2 = request.GET.get('pb', 'pa') # replace with your parameter name

        # Process the data and parameters as needed
        # processed_data = {} # replace with your processing logic
        # processed_parameters = {} # replace with your processing logic

        # Send the response back to the external API

        response_data = {
            'status': 'success',
            'data': "processed_data",
            'parameters': "processed_parameters"
        }
        return Response(response_data)


class GetConnectedBanksRequest(APIView):
    
    def post(self, request):
        # Retrieve the data sent in the POST request from the external API
        data = request.data

        # Retrieve the parameters sent with the request
        customer_id = request.GET.get('customer_id') # replace with your parameter name
        # parameter2 = request.GET.get('pb', 'pa') # replace with your parameter name

        # Process the data and parameters as needed
        # processed_data = {} # replace with your processing logic
        # processed_parameters = {} # replace with your processing logic

        # Send the response back to the external API

        response_data = {
            'status': 'success',
            'data': "processed_data",
            'parameters': "processed_parameters"
        }
        return Response(response_data)


"""

class GetBanks(APIView):
    def get(self, request):
        bank_id = request.data.get('bank_id')
        response = requests.get(f"http://localhost:1100/banks/{bank_id}")
        response_dict = json.loads(response.text)
        return Response(response_dict)


class SendConnectedBanks(APIView):
    def get(self, request):
        customer_id = request.data.get('customer_id')
        connected_banks = ConnectedBank.objects.filter(user__id=customer_id)
        serializer = ConnectedBankSerializer(connected_banks, many=True)
        # response = requests.post(f"http://localhost:1100/connected-banks/{customer_id}")
        # response_dict = json.loads(response.text)
        return response.Response(serializer.data)
        # return Response(response_dict)

        # connected_banks = ConnectedBank.objects.filter(user__id=user_account_id)
        # serializer = ConnectedBankSerializer(connected_banks, many=True)

"""



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PaySerializer

# class Pay(APIView):
#     permission_classes = []
#     serializer_class = PaySerializer

#     def post(self, request):
#         serializer = PaySerializer(data=request.data)
#         if serializer.is_valid():
#             # Return the input data as it is
#             return Response(request.data, status=status.HTTP_201_CREATED)
#         else:
#             # Return the serializer errors in the response
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # if serializer.is_valid():
#         #     # Create a new object based on the validated data
#         #     obj = serializer.save()

#         #     # Return the serialized object data in the response
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # else:
#         #     # Return the serializer errors in the response
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
