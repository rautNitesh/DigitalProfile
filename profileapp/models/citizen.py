from django.db import models
from django.core.validators import int_list_validator, MaxLengthValidator, MinLengthValidator

from .home import Home

# ('database storing value', 'display value')

GENDER = [
    ('पुरुष', 'पुरुष '),
    ('महिला', 'महिला'),
    ('अन्य', 'अन्य'),
]
MARITAL_STATUS = [
    ('बिबाहित', 'बिबाहित'),
    ('अबिबाहित', 'अबिबाहित'),
    ('डिभोर्सड', 'डिभोर्सड'),
    ('एकल', 'एकल'),
]
EDUCATION = [
    ('सामान्य साक्षर', 'सामान्य साक्षर'),
    ('असाक्षर', 'असाक्षर'),
    ('बिद्यालय', 'बिद्यालय'),
    ('उच्चशिक्षा', 'उच्चशिक्षा'),
    ('स्नातक', 'स्नातक'),
    ('स्नाकोत्तर', 'स्नाकोत्तर'),
    ('विद्यावारिधि', 'विद्यावारिधि'),
]

RELIGION = [
    ('H', 'Hindu'),
    ('M', "Muslim"),
    ('C', 'Christan'),
    ('B', 'Buddist'),
    ('S', 'Shikh'),
]

DISABILITY = [
    ('Normal', 'Normal'),
    ('Eye', "Eye"),
    ('Hearing', 'Hearing'),
    ('Speaking', 'Speaking'),
    ('Manasik', 'Manasik'),
    ('Hand', 'Hand'),
    ('Feet', 'Feet'),
    ('Others', 'Others')
]


class Citizen(models.Model):
    citizenship_id = models.CharField(blank=True, max_length=150, null=True)
    birth_registration_id = models.CharField(
        blank=True, max_length=150, null=True)
    full_name = models.CharField(max_length=150)
    ward_no = models.CharField(max_length=2,
                               validators=[int_list_validator])
    home = models.ForeignKey(
        'profileapp.Home', related_name="house_no", default=5000, blank=True, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=25, choices=GENDER)
    marital_status = models.CharField(
        max_length=30, choices=MARITAL_STATUS)  # marital table
    married_to = models.ForeignKey(
        'self', blank=True, null=True, related_name='spouse', on_delete=models.DO_NOTHING)
    father = models.ForeignKey('self', blank=True, null=True,
                               related_name='is_father_of', on_delete=models.DO_NOTHING)
    mother = models.ForeignKey('self', blank=True, null=True,
                               related_name='is_mother_of', on_delete=models.DO_NOTHING)
    caste = models.CharField(max_length=100)  # caste table ?
    dob = models.DateField()
    religion = models.CharField(
        max_length=100, choices=RELIGION)  # religion table ?
    literacy = models.CharField(
        max_length=100, choices=EDUCATION)  # literacy table
    specially_abled = models.CharField(
        max_length=10, null=True, choices=DISABILITY)
    citizenship_issued_date = models.DateField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    mobile_no = models.CharField(blank=True, null=True, max_length=10, validators=[
                                 MaxLengthValidator(10), MinLengthValidator(10), int_list_validator])
    tole = models.CharField(max_length=150)
    temporary_address = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.full_name


# class Marriage(models.Model):
#     husband = models.OneToOneField(Citizen, related_name="is_husband_of")
#     wife = models.OneToOneField(Citizen, related_name="is_wife_of")
