# Generated by Django 5.0.6 on 2024-07-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recive_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(max_length=255)),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], max_length=20)),
                ('cuisine_preference', models.CharField(max_length=255)),
                ('cooking_time', models.DateTimeField(max_length=255)),
                ('complexity', models.CharField(choices=[('Beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=255)),
            ],
        ),
    ]
