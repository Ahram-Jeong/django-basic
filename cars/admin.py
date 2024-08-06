from django.contrib import admin
from cars.models import Car

# Register your models here.
# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    # 객체의 필드 순서 지정 가능
    # fields = ["year", "brand"]

    # 관리자 페이지의 필드셋 지정 가능
    fieldsets = [
        ("TIME INFORMATION", {"fields" : ["year"]}),
        ("CAR INFORMATION", {"fields" : ["brand"]})
    ]

admin.site.register(Car, CarAdmin)