# Generated by Django 2.2.16 on 2021-02-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_auto_20201116_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='resource_type',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Resource Type'),
        ),
    ]
