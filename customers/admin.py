from django.contrib import admin
from customers.models import (
    Card,
    Utility,
    UtilityProfile,
    ConnectedBank,
    PaymentCycle
)


admin.site.register(Card)
admin.site.register(Utility)
admin.site.register(UtilityProfile)
admin.site.register(ConnectedBank)
admin.site.register(PaymentCycle)
