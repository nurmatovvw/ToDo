from django.shortcuts import render
from .models import Hospital, Doctor, MainDoctor,Patients

def index(request):
    hospitals = Hospital.objects.all()
    return render(request, 'index.html', {'hospitals':hospitals})

def detail(request, pk):
    hospital_detail = Hospital.objects.get(pk=pk)
    doctor_detail = Doctor.objects.filter(hospital=pk)
    patients_detail = Patients.objects.filter(doctor=pk)

    context = {
        'hospital_detail':hospital_detail,
        'doctor_detail':doctor_detail,
        'patients_detail':patients_detail
    }
    return render(request, "detail.html", context)
    