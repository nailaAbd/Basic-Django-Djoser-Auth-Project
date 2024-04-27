from django.db import models
from accounts.models import UserAccount


class Card(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    
    def __str__(self):
        return self.card_number


class ConnectedBank(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    bank_id = models.CharField(max_length=100, default="bank_id", blank=True)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'bank_name', 'account_number', 'bank_id'], 
                name='Unique connected banks'
                )
        ]
    def __str__(self):
        return self.user.first_name


class Utility(models.Model):
    utility_name = models.CharField(max_length=100)
    utility_code = models.CharField(max_length=100)
    def __str__(self):
        return self.utility_name


class PaymentCycle(models.Model):
    cycle_name = models.CharField(max_length=100)


class UtilityProfile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    user_utility_id = models.CharField(max_length=100)
    pay_every = models.ForeignKey(PaymentCycle, on_delete=models.CASCADE)
    amount = models.FloatField()
    pay_automatically = models.BooleanField(default=False)
    def __str__(self):
        return self.utility.utility_name


    

