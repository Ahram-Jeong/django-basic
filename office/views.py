from django.shortcuts import render
from . import models

# Create your views here.

# ListView
def list_patients(request):
    all_patients = models.Patient.objects.all()
    # context는 딕셔너리 형태여야 함
    context = {
        "patients" : all_patients
    }

    return render(request, "office/list.html", context = context)