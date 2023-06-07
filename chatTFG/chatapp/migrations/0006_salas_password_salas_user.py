# Generated by Django 4.1.7 on 2023-06-06 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0005_salas_c'),
    ]

    operations = [
        migrations.AddField(
            model_name='salas',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salas',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='salas_p', to=settings.AUTH_USER_MODEL),
        ),
    ]
