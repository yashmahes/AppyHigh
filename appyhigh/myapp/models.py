from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=255)
    carbohydrates_amount = models.IntegerField()
    fats_amount = models.IntegerField()
    proteins_amount = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
