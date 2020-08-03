from django.db import models
from django.contrib.auth.models import AbstractUser, Group


PERIOD = (
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
)


class User(AbstractUser):

    CUSTOMER = 1
    FARMER = 2
    MINISTRY = 3

    GROUP_CHOICES = (
        (CUSTOMER, "Customer"),
        (FARMER, "Farmer"),
        (MINISTRY, "Ministry"),
    )

    email = models.CharField(max_length=50, null=True, blank=True)
    pan = models.CharField(
        verbose_name="PAN Number", max_length=15, null=False, blank=False
    )
    aadhar = models.CharField(
        verbose_name="Aadhar Number", max_length=20, null=False, blank=False
    )
    gst = models.CharField(max_length=20, default="")
    REQUIRED_FIELDS = ["email", "pan", "aadhar", "first_name", "last_name"]

    def __str__(self):

        return self.username + "  " + self.first_name


class PhoneOtp(models.Model):

    phone_relation = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(verbose_name="otp", max_length=8, null=False)
    count = models.IntegerField(verbose_name="otp_count", default=0)


class CottonType(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=20, blank=False)
    district = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, default=1, blank=False, on_delete=models.CASCADE)
    cotton_type = models.ForeignKey(CottonType, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + "  " + self.cotton_type.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False)
    selling_price = models.PositiveIntegerField(blank=False)
    msp = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.product.cotton_type.name + "  " + str(self.quantity)


class Order(models.Model):
    user = models.ForeignKey(User, default=1, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=False)
    mobile = models.CharField(max_length=15, blank=False)
    shipping_address = models.TextField(blank=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "  " + self.mobile


class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.order.name + "  " + self.inventory.product.cotton_type.name


class Analysis(models.Model):
    cotton_type = models.ForeignKey(CottonType, blank=False, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, blank=False, on_delete=models.CASCADE)
    period = models.CharField(max_length=8, choices=PERIOD, blank=False)
    date = models.DateField(blank=False)
    prediction = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    confidence_lower = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    confidence_upper = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    temperature = models.CharField(max_length=5, blank=True, null=True)
    rainfall = models.CharField(max_length=5, blank=True, null=True)
    economy_indicator = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return (
            self.cotton_type.name
            + " "
            + self.market.name
            + " "
            + self.period
            + " "
            + str(self.date)
        )

