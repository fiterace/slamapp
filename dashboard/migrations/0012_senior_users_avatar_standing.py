# Generated by Django 3.0.7 on 2020-07-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200705_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior_users',
            name='avatar_standing',
            field=models.ImageField(default='static/dashboard/img/Avatars/standing/background_removed.png', upload_to='static/dashboard/img/Avatars/standing'),
        ),
    ]
