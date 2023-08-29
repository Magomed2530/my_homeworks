from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


User = get_user_model()  # взять данные из таблицы по-умолчанию User

class Advertisement(models.Model):  # модель

    # колонки модели
    title = models.CharField('Заголовок', max_length=128)  # 1-ый атрибут - verbose_name
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField('Изоборажение', upload_to='advertisements/', blank=True)
    # upload_to - путь относительно папки media
    # blank=True - заполнение поля становится необязательным

    # отдельные колонки для панели администратора, не существующие в самой БД (гипотетические колонки)
    @admin.display(description='дата создания')  # используется не колонка модели, а метод модели
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;"> Сегодня в {}</spam>', created_time
            )
        return self.created_at.strftime('%d.%m.%S в %H:%M:%S')

    @admin.display(description='дата редактирования')  # используется не колонка модели, а метод модели
    def updated_date(self):
        from django.utils import timezone
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: bold;"> Сегодня в {}</spam>', updated_time
            )
        return self.update_at.strftime('%d.%m.%S в %H:%M:%S')

    @admin.display(description='мини изображение')  # используется не колонка модели, а метод модели
    def show_mini_image(self):
        if self.image:  # если есть картинка
            return format_html(
                '<img src={} width=50 height=50>', self.image.url
            )

    # изменение названия таблицы
    class Meta:
        db_table = 'advertisements'

    # настройка строкового представления объекта
    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'


# https://docs.djangoproject.com/en/4.2/ref/models/fields/
# https://django.fun/ru/docs/django/4.1/ref/models/fields/

# 1. python manage.py makemigrations - создание - подготовка миграции
# 2. python manage.py migrate - применение миграции