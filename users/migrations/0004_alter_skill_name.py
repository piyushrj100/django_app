# Generated by Django 4.0.5 on 2022-06-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]