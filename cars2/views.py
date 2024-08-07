from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def rental_review(request):
    # POST request -> Check the Form contents -> Redirect : Thank you
    if request.method == "POST" :
        form = ReviewForm(request.POST)
        # 요청이 유효하다면
        if form.is_valid():
            form.save() # form을 저장, 이것은 ModelForm이기 때문에 사용자가 모델의 새 인스턴스로 전달한 내용을 자동으로 저장
            # print(form.cleaned_data) # -> 딕셔너리 형태 반환
            return redirect(reverse("cars2:thank_you"))
    # Else, render Form
    else:
        form = ReviewForm()
    return render(request, "cars2/rental_review.html", context = {"form" : form})

def thank_you(request):
    return render(request, "cars2/thank_you.html")