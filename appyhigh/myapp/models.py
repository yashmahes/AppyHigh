from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=255)
    carbohydrates_amount = models.IntegerField()
    fats_amount = models.IntegerField()
    proteins_amount = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    fullname = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
