from django.urls import include, path
from rest_framework import routers
from customers.views import (
    CardViewSet,
    UtilityViewSet,
    UtilityProfileViewSet,
    ConnectedBankViewSet,
    PaymentCycleViewSet,
    GetConnectedBanksRequest,
    GetBanks,
    GetDetailBank,
    ReturnConnectedBAnks,
    VerifyPin,
)


router = routers.DefaultRouter()
  
router.register(r'cards', CardViewSet)
router.register(r'utilitys', UtilityViewSet)
router.register(r'utility_profiles', UtilityProfileViewSet)
router.register(r'connected_banks', ConnectedBankViewSet)
router.register(r'paymentcycles', PaymentCycleViewSet),


urlpatterns = [
    path('', include(router.urls)),
    path('get-connected-banks/', GetConnectedBanksRequest.as_view(), name='get_connected_banks'),
    path('get-banks/', GetBanks.as_view(), name='get_banks'),
    path('get-bank-detail/', GetDetailBank.as_view(), name='get_detail_bank'),
    path('return-connected-banks/', ReturnConnectedBAnks.as_view(), name='return_connected_banks'),
    path('verify-pin/', VerifyPin.as_view(), name='verify_pin')
]