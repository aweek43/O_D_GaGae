# Generated by Django 2.2.8 on 2019-12-15 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delos', '0003_group_groupschedule_member_survey_timeschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupschedule',
            old_name='group_name',
            new_name='group_pk',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='group_name',
            new_name='group_pk',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='group_member',
            new_name='member',
        ),
        migrations.AddField(
            model_name='timeschedule',
            name='day',
            field=models.CharField(choices=[('1', '월요일'), ('2', '화요일'), ('3', '수요일'), ('4', '목요일'), ('5', '금요일'), ('6', '토요일'), ('7', '일요일')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='timeschedule',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timeschedule',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
