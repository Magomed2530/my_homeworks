from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
        )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='дата редактирования')
    def updated_date(self):
        from django.utils import timezone
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', update_time
        )
        return self.update_at.strftime("%d.%m.%Y в %H:%M:%S")


    @admin.display(description='мини изображение')
    def show_mini_image(self):
        if self.image:
            return format_html('<img src={} width=50 height=50>', self.image.url)



    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'


# eng: https://docs.djangoproject.com/en/4.2/ref/models/fields/
# rus: https://django.fun/ru/docs/django/4.1/ref/models/fields/

# python manage.py makemigrations  # создание-подготовка миграции
# python manage.py migrate  # применение миграции