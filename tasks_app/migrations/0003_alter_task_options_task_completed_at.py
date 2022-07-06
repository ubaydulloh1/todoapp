# Generated by Django 4.0.6 on 2022-07-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0002_alter_task_options_task_is_pinned_task_pinned_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-is_pinned', '-pinned_at', '-created']},
        ),
        migrations.AddField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]