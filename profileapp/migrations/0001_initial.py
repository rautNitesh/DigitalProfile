# Generated by Django 3.0.8 on 2020-08-06 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenship_id', models.CharField(blank=True, max_length=150, null=True)),
                ('full_name', models.CharField(max_length=150)),
                ('ward_no', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'पुरुष '), ('f', 'महिला'), ('o', 'अन्य')], max_length=25)),
                ('marital_status', models.CharField(choices=[('बिबाहित', 'बिबाहित'), ('अबिबाहित', 'अबिबाहित'), ('डिभोर्सड', 'डिभोर्सड'), ('एकल', 'एकल')], max_length=30)),
                ('caste', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('religion', models.CharField(choices=[('H', 'Hindu'), ('M', 'Muslim'), ('C', 'Christan'), ('B', 'Buddist'), ('S', 'Shikh')], max_length=100)),
                ('literacy', models.CharField(choices=[('सामान्य साक्षर', 'सामान्य साक्षर'), ('असाक्षर', 'असाक्षर'), ('बिद्यालय', 'बिद्यालय'), ('उच्चशिक्षा', 'उच्चशिक्षा'), ('स्नातक', 'स्नातक'), ('स्नाकोत्तर', 'स्नाकोत्तर'), ('विद्यावारिधि', 'विद्यावारिधि')], max_length=100)),
                ('citizenship_issued_date', models.DateField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('tole', models.CharField(max_length=150)),
                ('temporary_address', models.CharField(blank=True, max_length=150, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='is_father_of', to='profileapp.Citizen')),
                ('married_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='spouse', to='profileapp.Citizen')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='is_mother_of', to='profileapp.Citizen')),
            ],
        ),
    ]
