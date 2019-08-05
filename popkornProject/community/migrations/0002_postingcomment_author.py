# Generated by Django 2.2.1 on 2019-08-05 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postingcomment',
            name='author',
            field=models.ForeignKey(default=1, null=True, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]