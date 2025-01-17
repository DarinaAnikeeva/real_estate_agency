# Generated by Django 2.2.27 on 2022-09-21 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0003_auto_20220920_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('flats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира, на которую жаловались')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
