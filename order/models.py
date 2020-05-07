from django.db import models

class Order(models.Model):
    STATUS = (
        ('Order Received', 'Order Received'),
        ('Order Sent', 'Order Sent'),
        ('Order Delivered', 'Order Delivered'),
    )

    #customer =
    #product = 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=254, null=True, choices=STATUS)
