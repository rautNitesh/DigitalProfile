from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, int_list_validator


class Home(models.Model):
    home_id = models.CharField(max_length=6, validators=[
                               MinLengthValidator(6), MaxLengthValidator(6), int_list_validator])
    ward_no = models.CharField(max_length=2, validators=[int_list_validator])
    tole = models.CharField(max_length=150)
    family_name = models.CharField(max_length=150)
    senior_family_member = models.OneToOneField(
        'profileapp.Citizen', related_name="sernior_member", on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.home_id} -{self.ward_no} - {self.tole} - {self.family_name}"


class Livestock(models.Model):
    home = models.ForeignKey('profileapp.Home', on_delete=models.CASCADE)
    big_animal = models.CharField(
        max_length=4, validators=[int_list_validator])
    small_animals = models.CharField(
        max_length=4, validators=[int_list_validator])
    bird = models.CharField(
        max_length=4, validators=[int_list_validator])

    def __str__(self):
        return self.home


class FamilyIncome(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    source = models.CharField(max_length=150, verbose_name="source of income")
    amount = models.IntegerField(verbose_name="yearly income")

    def __str__(self):
        return f"{self.home} - {self.amount} - {self.source}"
