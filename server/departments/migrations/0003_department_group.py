# Generated by Django 3.1.2 on 2021-02-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_department_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
