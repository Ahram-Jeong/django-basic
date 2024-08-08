from django.urls import path
# from .views import home_view
from .views import *

app_name = "classroom"

# domain.com/classroom/
urlpatterns= [
    # path("", home_view, name = "home") # 함수 기반 뷰 연결 : path는 뷰를 함수라고 기대 함 (home_view)
    path("", HomeView.as_view(), name = "home"), # 클래스 기반 뷰 연결 : as_view() 메소드 호출 -> 클래스를 가지고 경로에 대한 함수를 반환
    path("thank_you/", ThankYouView.as_view(), name = "thank_you"),
    path("contact/", ContactFormView.as_view(), name = "contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name = "create_teacher"),
    path("list_teacher/", TeacherListView.as_view(), name = "list_teacher"),
    path("detail_teacher/<int:pk>", TeacherDetailView.as_view(), name = "detail_teacher"),
]