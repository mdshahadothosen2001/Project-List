from django.db import models
from accounts.models import CustomUser


class country(models.Model):
    """Used to user country name attribute"""

    country_name = models.CharField(max_length=255)

    def __str__(self):
        """Used to return country name when object data to string"""

        return self.country_name


class address(models.Model):
    """Used for user address details"""

    unit_number = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)

    def __str__(self):
        """Used to return unit number when object to string convert"""

        return self.unit_number


class user_address(models.Model):
    """Used to make relationship users and address"""

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address_id = models.ForeignKey(address, on_delete=models.CASCADE)
    is_default = models.BooleanField()
