from django.contrib import admin
from django.urls import path, include
# from customers.views import Pay


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('accounts.urls')),
    path('api/', include('customers.urls')),
    # path('pay/', Pay.as_view(), name='pay'),
]
