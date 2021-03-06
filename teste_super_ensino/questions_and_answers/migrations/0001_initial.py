# Generated by Django 4.0.1 on 2022-02-15 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('alternative_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField(default='')),
                ('is_correct', models.BooleanField()),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'alternative',
                'ordering': ['alternative_id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField(default='')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'question',
                'ordering': ['question_id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=150)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['student_id'],
            },
        ),
        migrations.CreateModel(
            name='QuestionAndAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answered_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('alternative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_and_answers.alternative')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_and_answers.question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_and_answers.student')),
            ],
            options={
                'verbose_name': 'question_and_answer',
                'ordering': ['answered_time'],
            },
        ),
        migrations.AddField(
            model_name='alternative',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_and_answers.question'),
        ),
    ]
