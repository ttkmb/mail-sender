# Generated by Django 4.2.7 on 2024-01-30 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0002_mailerlogger'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailer',
            name='mail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='mailer.mailermessage', verbose_name='Письмо'),
        ),
    ]
