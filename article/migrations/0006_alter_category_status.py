# Generated by Django 3.2 on 2023-04-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20230408_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=20),
        ),
    ]
