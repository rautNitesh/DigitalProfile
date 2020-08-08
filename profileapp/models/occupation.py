from django.db import models
from django.core.validators import int_list_validator

OCCUPATION = [
    ('F', "बैदेशिक"),
    ('H', "आन्तरिक"),
]


class Occupation(models.Model):
    citizen = models.OneToOneField(
        "profileapp.Citizen", on_delete=models.CASCADE)
    occupation_type = models.CharField(max_length=1, choices=OCCUPATION)
    name = models.CharField(max_length=150, verbose_name="Employment Name")
    salary = models.CharField(max_length=8, validators=[int_list_validator])
