from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class Region(models.Model):
    region_name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=100)

    def __str__(self):
        return self.region_name


class Zone(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    zone_name = models.CharField(max_length=100)
    zone_code = models.CharField(max_length=100)

    def __str__(self):
        return self.zone_name


class Woreda(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    woreda_name = models.CharField(max_length=100)
    woreda_code = models.CharField(max_length=100)

    def __str__(self):
        return self.woreda_name


class UserAccountManager(BaseUserManager):

    # def create_user(self, first_name, middle_name, last_name, email, username, phone_number, password=None):
    #     if not email:
    #         raise ValueError('Please input email address.')
        
    #     email = self.normalize_email(email)
    #     user = self.models(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, username=username, phone_number=phone_number)

    #     user.set_password(password)
    #     user.save()

    #     return user

    
    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # if not email:
        #     raise ValueError("Email field is required")

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
		
        return user

    def create_user(self, password=None,  **extra_fields):
        # if not email:
        #     raise ValueError('Email Field is required.')

        # email = self.normalize_email(email)
        user = self.model(**extra_fields)

        user.set_password(password)
        user.save()
        
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    # middle_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=None)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255, default='email_address')
    # username = models.CharField(max_length=255, unique=True)
    # address = models.CharField(max_length=255, unique=True, default="Address")
    # address = models.ForeignKey(Address, null=True, on_delete=models.SETNULL)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    woreda = models.ForeignKey(Woreda, on_delete=models.CASCADE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'date_of_birth']
    # REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number']

    def __str__(self):
        return str(self.phone_number)

    
    # @property()
    # def address(self):
    #     if self.region.region_name != None and self.woreda.woreda_name != None and self.zone.zone_name != None:
    #         return self.region.region_name + self.woreda.woreda_name + self.zone.zone_name
    #     return "No address"

    # @property()
    # def full_name(self):
    #     return self.first_name + self.middle_name + self.last_name

