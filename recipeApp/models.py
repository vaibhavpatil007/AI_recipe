from django.db import models

# Create your models here.

class recipe_model(models.Model):
    ingredients = models.CharField(max_length=255)
    meal_type_choices = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]
    
    meal_type = models.CharField(max_length=20,choices=meal_type_choices)

    cuisine_preference = models.CharField(max_length=255)
    cooking_time = models.CharField(max_length=255)

    complexity_choices = [
        ('Beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    complexity = models.CharField(max_length=255,choices=complexity_choices)
