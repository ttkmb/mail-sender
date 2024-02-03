# Generated by Django 4.2.7 on 2024-02-03 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0005_alter_mailer_time_start_alter_mailer_time_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailerlogger',
            name='mail',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='mailer.mailer', verbose_name='Рассылка'),
        ),
    ]