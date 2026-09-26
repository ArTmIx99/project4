from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        INPROGRESS='in_progress', 'В процесі'
        COMPLETED='completed', 'Завершено'
        POSTRONED='postroned', 'Відхилено'
    title=models.CharField(max_length=255, verbose_name='Назва'
                           )
    description=models.TextField(blank=True, verbose_name='Опис')
    status=models.CharField(max_length=20, choices=Status.choices, default=Status.INPROGRESS, verbose_name='status')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Призначений користувач')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} ({self.get_status_display()}) -> {self.user.username}"