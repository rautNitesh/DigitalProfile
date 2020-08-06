from django.db import models

#('database storing value', 'display value')

GENDER = [
    ('m', 'पुरुष '),
    ('f', 'महिला'),
    ('o', 'अन्य'),
]
MARITAL_STATUS = [
    ('बिबाहित', 'बिबाहित'),
    ('अबिबाहित', 'अबिबाहित'),
    ('डिभोर्सड', 'डिभोर्सड'),
    ('एकल', 'एकल'),
]
Education = [
    ('सामान्य साक्षर', 'सामान्य साक्षर'),
    ('असाक्षर', 'असाक्षर'),
    ('बिद्यालय', 'बिद्यालय'),
    ('उच्चशिक्षा', 'उच्चशिक्षा'),
    ('स्नातक', 'स्नातक'),
    ('स्नाकोत्तर', 'स्नाकोत्तर'),
    ('विद्यावारिधि', 'विद्यावारिधि'),
]


class Citizen(models.Model):
    citizenship_id = models.CharField(blank=True, max_length=150, null=True)
    full_name = models.CharField(max_length=150)
    ward_no = models.IntegerField()
    #family_ID
    gender = models.CharField(max_length=25, choices=GENDER)
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUS) #marital table
    # married_to
    caste = models.CharField(max_length=100) #caste table ?
    dob = models.DateField()
    religion = models.CharField(max_length=100) #religion table ?
    literacy = models.CharField(max_length=100, choices=Education) #literacy table
    # occupation
    # specially_abled
    citizenship_issued_date = models.DateField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    # mobile_no = PhoneField(blank=True, null=True, max_length=10)
    tole = models.CharField(max_length=150)
    temporary_address = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)