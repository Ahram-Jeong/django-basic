from django.urls import path
from . import views # 현재 디렉토리에서 views를 임포트 하라

# 템플릿 내에서 url 이동하기 위해 추가, 앱 이름과 일치시킴
#register the app namespace
# URL NAMES
app_name = "my_app"

# my_app/
urlpatterns = [
    # "" -> /my_app -> PROJECT urls.py
    # path("", views.index, name = "index"), # /my_app
    # path("simple_view/", views.simple_view), # /my_app/simple_view
    #
    # # 동적 뷰 연결
    # path("<str:topic>/", views.news_view, name = "topic-page"), # topic-page 별로 urlpatterns 내부의 특정 경로 참조 가능
    # path("<int:num1>/<int:num2>", views.add_view),
    # path("<int:num>", views.num_page_view)

    # 템플릿 -> 뷰 -> url
    path("", views.simple_view, name = "example"), # domain.com/my_app
    path("variable/", views.variable_view),
    path("example/", views.example_view, name = "example02")
]