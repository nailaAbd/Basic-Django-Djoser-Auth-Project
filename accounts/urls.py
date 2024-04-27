from django.urls import include, path
from accounts.views import VerifyPhoneView


urlpatterns = [
    path('verify-phone/', VerifyPhoneView.as_view(), name='verify_phone'),
]
