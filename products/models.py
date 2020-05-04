from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')
    top_note_1 = models.CharField(max_length=254, default='')
    top_note_2 = models.CharField(max_length=254, default='')
    heart_note_1 = models.CharField(max_length=254, default='')
    base_note_1 = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name
