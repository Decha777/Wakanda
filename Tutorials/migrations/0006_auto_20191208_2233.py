# Generated by Django 2.2.7 on 2019-12-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorials', '0005_aboutuspage_accountpage_coursepage_freelancejobpage_incentivepage_paymentpage_toolspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='content',
            field=models.TextField(),
        ),
    ]