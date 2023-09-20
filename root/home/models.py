from django.db import models
from django.utils import timezone
import pytz


class Response(models.Model):

    name = models.CharField("Ім'я", max_length=100, null=False)
    email = models.EmailField('Email', max_length=100, unique=True, null=False)
    response = models.TextField('Відгук',max_length=1024)
    image = models.FileField('Фото', upload_to='images/response_user')
    timestamp = models.DateTimeField('Час',auto_now_add=True, null=False)

    def save(self, *args, **kwargs):
        # Отримуємо поточний час у вашому часовому поясі
        your_timezone = pytz.timezone('EET')  # Замініть на свій часовий пояс
        current_time = timezone.now().astimezone(your_timezone)

        # Зберігаємо поточний час у поле created_at
        self.created_at = current_time
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return str(self.name)
