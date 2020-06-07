from django.contrib import admin
from review.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date', 'review_text', 'score']