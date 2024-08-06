from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    # 모든 차를 가져와서 리스팅하기 위해 models 임포트
    all_cars = models.Car.objects.all()
    context = {
        "all_cars" : all_cars
    }

    return render(request, "cars/list.html", context = context)

def add(request):
    if request.POST:
        brand = request.POST["brand"]
        year = int(request.POST["year"])
        # 새 Car 객체 생성
        models.Car.objects.create(brand = brand, year = year)
        # 리다이렉트 : if 사용자가 post 요청을 보내서 새로운 Car 객체를 생성하면 list.html로 이동
        return redirect(reverse("cars:list"))
    else:
        return render(request, "cars/add.html")

def delete(request):
    if request.POST:
        # delete the car
        pk = request.POST["pk"]
        try:
            models.Car.objects.get(pk = pk).delete()
            return redirect(reverse("cars:list"))
        except:
            print("유효한 PK가 아닙니다.")
            return redirect(reverse("cars:delete"))
    else:
        return render(request, "cars/delete.html")