from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
# 함수 기반 뷰
# def home_view(request):
#     return render(request, "classroom/home.html")

# 클래스 기반 뷰 (TemplateView)
class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"

class ContactFormView(FormView):
    # 폼 클래스 연결
    form_class = ContactForm # 인스턴스 생성이 아닌, 연결만 하는 것
    template_name = "classroom/contact.html"

    # 성공 시, 이동하는 url (not a template.html)
    # 함수 기반 뷰에서 reverse(str 반환)를 사용했다면, 클래스 기반 뷰에서는 reverse_lazy(객체 반환)사용
    success_url = reverse_lazy("classroom:thank_you")

    # 유효한 form이 post 되었을 때 호출
    def form_valid(self, form):
        print(form.cleaned_data)
        
        # 함수 기반 뷰의 ContactForm(request.POST)와 유사
        return super().form_valid(form)


# =========================== 모델 기반 CBV ===========================
class TeacherCreateView(CreateView):
    # 1. 모델 연결
    # 연결 템플릿은 CreateView가 기본적으로 model_form.html 템플릿을 찾아감
    model = Teacher
    # 2. 실제로 CreateView에 표시하는 필드 파악
    fields = "__all__"

    # 템플릿에서 submit 버튼을 누르면, save()를 누른 것 처럼 자동으로 작동하게 됨
    # 3. 성공 시, 이동하는 url
    success_url = reverse_lazy("classroom:thank_you")
# ====================================================================