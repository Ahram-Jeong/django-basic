from django.urls import path
from . import views # 현재 디렉토리에서 views를 임포트 하라

# my_app/
urlpatterns = [
    # "" -> /my_app -> PROJECT urls.py
    # name -> 실제 함수 이름과 일치 시킴
    path("", views.index, name = "index"), # /my_app
    path("simple_view/", views.simple_view), # /my_app/simple_view
    # 동적 뷰 연결
    path("<str:topic>/", views.news_view),
    path("<int:num1>/<int:num2>", views.add_view)
]