from django.db import models


class Articles(models.Model):
    title = models.CharField("Ім'я", max_length=15)
    about = models.TextField('Тема', max_length=256, null=False)
    email = models.EmailField('Email', max_length=30)
    phone = models.CharField('Телефон', max_length=20)
    message = models.TextField('Повідомлення', max_length=1024, null=False)

    def __str__(self) -> str:
        return str(self.title)


class ResponseSite(models.Model):
    title = models.CharField("Ім'я", max_length=15)
    about = models.TextField('Тема', max_length=256, null=False)
    message = models.TextField('Повідомлення', max_length=1024, null=False)

    def __str__(self) -> str:
        return str(self.title)