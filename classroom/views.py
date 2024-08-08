from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# 함수 기반 뷰
# def home_view(request):
#     return render(request, "classroom/home.html")

# 클래스 기반 뷰 (TemplateView)
class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"