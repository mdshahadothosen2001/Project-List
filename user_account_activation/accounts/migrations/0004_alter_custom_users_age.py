# Generated by Django 4.1.4 on 2023-07-14 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_custom_users_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_users',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
