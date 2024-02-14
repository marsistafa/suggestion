# Generated by Django 5.0.2 on 2024-02-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
        ),
    ]