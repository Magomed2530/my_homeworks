from django.db import models

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')  # help_text - необязательный аргумент
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'


# https://docs.djangoproject.com/en/4.2/ref/models/fields/
# https://django.fun/ru/docs/django/4.1/ref/models/fields/

# 1. python manage.py makemigrations - создание - подготовка миграции
# 2. python manage.py migrate - применение миграции