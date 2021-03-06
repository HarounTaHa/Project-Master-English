# Generated by Django 4.0.4 on 2022-06-04 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
        migrations.CreateModel(
            name='PractiseQuestionTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_two', models.CharField(max_length=200)),
                ('practise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise.practise')),
            ],
            options={
                'verbose_name': 'PractiseQuestionTwo',
                'verbose_name_plural': 'PractiseQuestionTwo',
            },
        ),
        migrations.CreateModel(
            name='PractiseQuestionOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_one', models.CharField(max_length=200)),
                ('practise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise.practise')),
            ],
            options={
                'verbose_name': 'PractiseQuestionOne',
                'verbose_name_plural': 'PractiseQuestionOne',
            },
        ),
        migrations.CreateModel(
            name='AnswerQuestionTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise.practisequestiontwo')),
            ],
            options={
                'verbose_name': 'AnswerQuestionTwo',
                'verbose_name_plural': 'AnswerQuestionTwo',
            },
        ),
        migrations.CreateModel(
            name='AnswerQuestionOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise.practisequestionone')),
            ],
            options={
                'verbose_name': 'AnswerQuestionOne',
                'verbose_name_plural': 'AnswerQuestionOne',
            },
        ),
    ]
