from django.db import models


class OTP(models.Model):
    """save otp and then used to active user account"""

    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """used to return email when convert object data to string"""

        return self.email
