# Generated by Django 4.1.1 on 2023-02-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_address',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
