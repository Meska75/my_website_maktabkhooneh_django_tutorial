# Generated by Django 5.2.1 on 2025-05-29 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogAdmin',
            new_name='Post',
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]
