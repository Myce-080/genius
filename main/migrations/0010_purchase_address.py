# Generated by Django 4.1.2 on 2022-12-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_purchase_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='address',
            field=models.CharField(default='b', max_length=50),
        ),
    ]
