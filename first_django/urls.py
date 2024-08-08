"""
URL configuration for first_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# 함수 기반 뷰로 홈페이지 추가 (함수 기반 뷰 예시, unusual)
# def home_view(request):
#     return HttpResponse("HOME PAGE")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', include('my_app.urls')), # 추가
    path('office/', include('office.urls')), # 추가
    path('cars/', include('cars.urls')), # 추가
    path('cars2/', include('cars2.urls')), # 추가
    path('classroom/', include('classroom.urls')), # 추가
    # path('', home_view) # 프로젝트 레벨의 home_view url 추가 (by. function)
    path('', views.home_view) # 프로젝트 레벨의 home_view url 추가 (by. views)
]

# 참고 : https://docs.djangoproject.com/en/5.0/topics/http/views/#customizing-error-views
handler404 = "first_django.views.my_custom_page_not_found_view"