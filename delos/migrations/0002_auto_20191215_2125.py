# Generated by Django 2.2.8 on 2019-12-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', '남자'), ('F', '여자')], max_length=1),
        ),
    ]