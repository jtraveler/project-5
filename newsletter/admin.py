from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'signup_date', 'is_active')
    list_filter = ('is_active', 'signup_date')
    search_fields = ('email',)
    ordering = ('-signup_date',)