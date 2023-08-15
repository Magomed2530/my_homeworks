from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):  # класс для панели администратора

    list_display = ['id', 'title', 'price', 'auction', 'created_at', 'created_date', 'updated_date']  # колонки таблицы
    # 'created_date' - гипотетическая колонка
    list_filter = ['auction', 'created_at']  # фильтрация таблицы
    actions = ['make_auction_false', 'make_auction_true']  # функционал к таблице

    # функции для таблицы
    @admin.action(description='Перевести auction в False')
    def make_auction_false(self, request, query):
        # в query попадают выбранные в checkbox элементы таблицы бд
        query.update(auction=False)

    @admin.action(description='Перевести auction в True')
    def make_auction_true(self, request, query):
        # в query попадают выбранные в checkbox элементы таблицы бд
        query.update(auction=True)

    # fieldsets - для раздела поля на смысловые блоки
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']  # для сокрытия блока
        })
    )

# регистрация связи между моделью Advertisement и классом AdvertisementAdmin
admin.site.register(Advertisement, AdvertisementAdmin)