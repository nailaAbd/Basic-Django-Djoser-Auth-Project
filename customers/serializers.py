from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import requests
from customers.models import (
    Card,
    Utility,
    UtilityProfile,
    ConnectedBank,
    PaymentCycle
)
from accounts.serializers import UserAccountSerializer
import json
from dotenv import load_dotenv
import os
load_dotenv()


# SUPER_CONTROL_IP_ADDRESS = "http://localhost:8000"
SUPER_CONTROL_IP_ADDRESS = os.getenv('SUPER_CONTROL_IP_ADDRESS')
# SUPER_CONTROL_IP_ADDRESS = "http://192.168.242.129:9864"

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('__all__')


class UtilitySerializer(ModelSerializer):
    class Meta:
        model = Utility
        fields = ('__all__')


class UtilityProfileSerializer(ModelSerializer):
    class Meta:
        model = UtilityProfile
        fields = ('__all__')




class ConnectedBankSerializer(ModelSerializer):
    banks_response = requests.post(f'{SUPER_CONTROL_IP_ADDRESS}/banks/get-banks').json()

    BANK_CHOICES = tuple([(bank["id"], bank["name"]) for bank in banks_response])
    bank_name = serializers.ChoiceField(choices=BANK_CHOICES, default='----')

    class Meta:
        model = ConnectedBank
        fields = ['user', 'account_number', 'bank_name', 'bank_id']
    
    def create(self, validated_data):
        # Modify the value of a field before saving
        bank_choices_mapping = dict(self.fields['bank_name'].choices)
        return super().create(validated_data)
    # def get_bank_name(self, obj):
    #     # bank_name = ConnectedBank.obvjects.filter(user=self.request.user)
    #     return obj.bank.bank_name

    # def get_user(self, obj):
    #     # bank_name = ConnectedBank.obvjects.filter(user=self.request.user)
    #     return obj.user.username

class PaymentCycleSerializer(ModelSerializer):
    class Meta:
        model = PaymentCycle
        fields = ('__all__')


