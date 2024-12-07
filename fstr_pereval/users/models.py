from django.db import models

class PassUser(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('moderated', 'На модерации'),
        ('approved', 'Одобрен'),
        ('rejected', 'Отклонен'),
    )

    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    firstname = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    lastname = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"