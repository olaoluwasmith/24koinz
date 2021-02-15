from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model()

def f():
    d = uuid4()
    str = d.hex
    return str[0:13]

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Package(models.Model):
    package = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.package


class BasicPrice(models.Model):
    price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.price


class AdvancedPrice(models.Model):
    price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.price


class PremiumPrice(models.Model):
    price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.price


class BasicOption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=50, blank=True)
    coupon = models.CharField(max_length=50, blank=True)
    select_package = models.ForeignKey(BasicPrice, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class AdvancedOption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=50, blank=True)
    coupon = models.CharField(max_length=50, blank=True)
    select_package = models.ForeignKey(AdvancedPrice, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PremiumOption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=50, blank=True)
    coupon = models.CharField(max_length=50, blank=True)
    select_package = models.ForeignKey(PremiumPrice, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True, default='')
    phone_number = models.CharField(max_length=50, blank=True, default='')
    referral_id = models.CharField(max_length=200, blank=True, default='')
    balance = models.IntegerField(default=0, null=True, blank=True)
    referral_bonus = models.IntegerField(default=0, null=True, blank=True)
    total_balance = models.IntegerField(null=True, blank=True)
    current_package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    number_of_referral = models.IntegerField(default=0, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    coupon = models.CharField(max_length=50, blank=True)
    vendor_id = models.CharField(default=f, max_length=15, unique=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.total_balance = self.balance + self.referral_bonus
        super(Detail, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.total_balance = self.balance + self.referral_bonus
        super().save(*args, **kwargs)