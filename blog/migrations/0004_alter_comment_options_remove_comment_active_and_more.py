# Generated by Django 4.1.2 on 2022-10-25 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_on',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]