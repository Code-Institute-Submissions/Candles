from django.db import models
from django.conf import settings
from django.utils import timezone
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    review_title = models.CharField(max_length=100, blank=False)
    review_text = models.TextField(default='')

    def publish(self):
        self.date = timezone.now()
        self.save()
        return self.date

    def __str__(self):
        return f'Review for user {self.user.username}'


