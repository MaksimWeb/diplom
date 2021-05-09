# Generated by Django 3.1.7 on 2021-03-19 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_auto_20210316_1542'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_results', '0002_result_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='quizes.quiz'),
        ),
        migrations.AlterField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
