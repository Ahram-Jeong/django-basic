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
            print(form.cleaned_data) # -> 딕셔너리 형태 반환
            return redirect(reverse("cars2:thank_you"))
    # Else, render Form
    else:
        form = ReviewForm()
    return render(request, "cars2/rental_review.html", context = {"form" : form})

def thank_you(request):
    return render(request, "cars2/thank_you.html")