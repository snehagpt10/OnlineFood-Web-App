# Generated by Django 5.1.2 on 2024-11-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'CUSTOMER')], null=True),
        ),
    ]
