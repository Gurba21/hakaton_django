from django.db import models


CHOICES = (
        ('1', 'Chui'),
        ('2', 'Yssyk-Kol'),
        ('3', 'Naryn'),
        ('4', 'Talas'),
        ('5', 'Djalal-Abad'),
        ('6', 'Osh'),
        ('7', 'Batken'),
    )


CHOICES1 = (
    ('1','Sawbones'),
    ('2','Therapist')
)

class Hosp(models.Model):
    hosp_okpo = models.CharField(max_length=100, primary_key=True, unique=True)
    hosp_region = models.CharField(max_length=50, choices = CHOICES)
    hosp_name = models.CharField(max_length=50)
    hosp_number = models.CharField(max_length=100)
    hosp_maindoc = models.CharField(max_length=155)
    hosp_docs = models.CharField(max_length=99,default=9)
    hosp_nurses = models.IntegerField()
    hosp_patients = models.IntegerField()
    hosp_gos = models.BooleanField(default=True)
    def __str__(self):
        return self.hosp_name

class Nurses(models.Model):
    hospitals = models.ForeignKey(Hosp, on_delete=models.CASCADE)
    nurse_name = models.CharField(max_length=100)
    nurse_pin = models.CharField(max_length=100)
    nurse_age = models.IntegerField()
    nurse_number = models.CharField(max_length=100)
    nurse_patients = models.CharField(max_length=200)
    def __str__(self):
        return self.nurse_name

class Doctors(models.Model):
    hospitals = models.ForeignKey(Hosp, on_delete=models.CASCADE)
    doctor_work = models.CharField(max_length=100, choices=CHOICES1)
    doctor_name = models.CharField(max_length=100)
    doctor_pin = models.CharField(max_length=100)
    doctor_age = models.IntegerField()
    doctor_experience = models.IntegerField()
    doctor_number = models.CharField(max_length=100)
    doctor_nurses = models.OneToOneField(Nurses, on_delete=models.CASCADE)
    doctor_patients = models.CharField( max_length=200)
    def __str__(self):
        return self.doctor_name

class Patients(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_pin = models.CharField(max_length=100)
    patient_age = models.CharField(max_length=5)
    patient_number = models.CharField(max_length=100)
    patient_doc = models.ForeignKey(Doctors, max_length=100,on_delete=models.CASCADE)
    patient_nurse = models.ForeignKey(Nurses, max_length=100, on_delete=models.CASCADE)
    patient_diagnostic = models.CharField(max_length=255)
    def __str__(self):
        return self.name_name

class Maindoctor(models.Model):
    hospitals = models.ForeignKey(Hosp, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_pin = models.CharField(max_length=10)
    doctor_age = models.CharField(max_length=10)
    doctor_experience = models.CharField(max_length=10,default=' 3 years ')
    doctor_number = models.CharField(max_length=100)
    mains_doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    doctor_nurses = models.ForeignKey(Nurses, on_delete=models.CASCADE)
    def __str__(self):
        return self.doctor_name








