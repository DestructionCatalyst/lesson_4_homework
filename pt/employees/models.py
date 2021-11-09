from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True)
    position = models.CharField(max_length=512)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-name']


class Positions(models.Model):
    name = models.CharField(max_length=150)
