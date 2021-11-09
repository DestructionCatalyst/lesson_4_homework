from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-username']
