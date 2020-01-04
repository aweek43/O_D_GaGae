# Generated by Django 2.2.8 on 2020-01-04 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('M', '남자'), ('F', '여자')], max_length=1)),
                ('age_range', models.CharField(blank=True, choices=[('1', '10대'), ('2', '20대'), ('3', '30대'), ('4', '40대'), ('5', '50대')], max_length=1)),
                ('survey_coin', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('generated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(max_length=10)),
                ('member_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_age_start', models.CharField(choices=[('1', '10대'), ('2', '20대'), ('3', '30대'), ('4', '40대'), ('5', '50대')], default='1', max_length=1)),
                ('target_age_end', models.CharField(choices=[('1', '10대'), ('2', '20대'), ('3', '30대'), ('4', '40대'), ('5', '50대')], default='5', max_length=1)),
                ('target_gender', models.CharField(blank=True, choices=[('M', '남자'), ('F', '여자')], max_length=1)),
                ('used_coin', models.IntegerField(default=0)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('generated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer_num', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=20)),
                ('day', models.CharField(choices=[('1', '월요일'), ('2', '화요일'), ('3', '수요일'), ('4', '목요일'), ('5', '금요일'), ('6', '토요일'), ('7', '일요일')], default='0', max_length=1)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('content', models.TextField()),
                ('question_type', models.IntegerField(default=0)),
                ('choices', models.TextField()),
                ('survey_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('survey_question_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.SurveyQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('generated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_alarm_on', models.BooleanField(default=True)),
                ('group_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Group')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('generated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_for_author', to=settings.AUTH_USER_MODEL)),
                ('group_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Group')),
                ('person_in_charge', models.ManyToManyField(blank=True, related_name='User_for_person_in_charge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('generated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('group_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delos.Group')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
