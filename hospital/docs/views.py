from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, template_name='docs/index.html')
def memorial(request):
    return render(request, template_name='docs/memorial.html')
def olc(request):
    return render(request, template_name='docs/olc.html')
def desert(request):
    return render(request, template_name='docs/desert.html')

def hosp(request):

    hospital = hosp.objects.all()
    context = {
        'hosp': hospital,
    }
    return render(request, template_name='index.html', context=context)

def main(request):
    Maindoctors = Maindoctor.objects.all()
    context = {
        'mdoctor': Maindoctors,
    }
    return render(request, template_name='index.html', context=context)
def doctor(request):
    doctor = Doctors.objects.all()
    context = {
        'doctor': doctor
    }
    return  render(request,template_name='memorial.html',context=context)
def nurse(request):
    nurse = Nurses.objects.all()
    context = {
        'nurse': nurse,
    }
    return render(request, template_name='index.html', context=context)

def patients(request):
    patient = Patients.objects.all()
    context = {
        'patient': patient,
    }
    return render(request, template_name='index.html', context=context)

