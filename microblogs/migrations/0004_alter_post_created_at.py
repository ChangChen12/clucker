# Generated by Django 3.2.8 on 2021-10-31 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]