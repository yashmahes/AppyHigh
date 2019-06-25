from django.db import models

# Create your models here.


class Food(models.Model):
    code = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    creator_t = models.CharField(max_length=255)
    created_datetime = models.CharField(max_length=255)
    last_modified_t = models.CharField(max_length=255)
    last_modified_datetime = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    packaging_tags = models.CharField(max_length=255)
    brands = models.CharField(max_length=255)
    brands_tags = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    categories_tags = models.CharField(max_length=255)
    categories_en = models.CharField(max_length=255)
    origins = models.CharField(max_length=255)
    origins_tags = models.CharField(max_length=255)
    manufacturing_places = models.CharField(max_length=255)
    manufacturing_places_tags = models.CharField(max_length=255)
    labels = models.CharField(max_length=255)
    labels_tags = models.CharField(max_length=255)
    labels_en = models.CharField(max_length=255)
    emb_codes = models.CharField(max_length=255)
    emb_codes_tags = models.CharField(max_length=255)
    first_packaging_code_geo = models.CharField(max_length=255)
    cities = models.CharField(max_length=255)
    cities_tags = models.CharField(max_length=255)
    purchase_places = models.CharField(max_length=255)
    stores = models.CharField(max_length=255)
    countries = models.CharField(max_length=255)
    countries_tags = models.CharField(max_length=255)
    countries_en = models.CharField(max_length=255)
    ingredients_text = models.CharField(max_length=255)
    allergens = models.CharField(max_length=255)
    allergens_en = models.CharField(max_length=255)
    traces = models.CharField(max_length=255)
    traces_tags = models.CharField(max_length=255)
    traces_en = models.CharField(max_length=255)
    serving_size = models.CharField(max_length=255)
    no_nutriments = models.CharField(max_length=255)
    additives_n = models.CharField(max_length=255)
    additives = models.CharField(max_length=255)
    additives_tags = models.CharField(max_length=255)

    carbohydrates_amount = models.IntegerField()
    fats_amount = models.IntegerField()
    proteins_amount = models.IntegerField()

    def __str__(self):
        return self.code


class User(models.Model):
    fullname = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
