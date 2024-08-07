from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label = "Fisrt Name", max_length = 100)
#     last_name = forms.CharField(label = "Last Name", max_length = 100)
#     email = forms.EmailField(label = "Email")
#     review = forms.CharField(label = "Please write your review here",
#                              widget = forms.Textarea(attrs = {"class" : "myform", "rows" : "10", "cols" : "100"}))

# Modelform
class ReviewForm(ModelForm):
    class Meta: # 단일 속성이 있는 클래스
        model = Review
        fields = ["first_name", "last_name", "stars"] # 상호작용 하고자 하는 모델의 필드 연결