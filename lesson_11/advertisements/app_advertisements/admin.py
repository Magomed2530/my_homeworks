from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'auction', 'created_at', 'created_date', 'updated_date', 'user', 'image', 'show_mini_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'make_auction_true']

    @admin.action(description='Перевести auction в False')
    def make_auction_false(self, request, query):
        query.update(auction=False)

    @admin.action(description='Перевести auction в True')
    def make_auction_true(self, request, query):
        query.update(auction=True)

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

admin.site.register(Advertisement, AdvertisementAdmin)