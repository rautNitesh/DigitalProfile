# Generated by Django 3.0.8 on 2020-08-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0010_remove_citizen_ward_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='gender',
            field=models.CharField(choices=[('पुरुष', 'पुरुष '), ('महिला', 'महिला'), ('अन्य', 'अन्य')], max_length=25),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='specially_abled',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Eye', 'Eye'), ('Hearing', 'Hearing'), ('Speaking', 'Speaking'), ('Manasik', 'Manasik'), ('Hand', 'Hand'), ('Feet', 'Feet'), ('Others', 'Others')], max_length=10, null=True),
        ),
    ]
