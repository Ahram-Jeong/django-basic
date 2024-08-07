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
        # fields = ["first_name", "last_name", "stars"] # 상호작용 하고자 하는 모델의 필드 연결
        fields = "__all__" # 모든 모델 필드를 폼 필드로 전달
        # 레이블 지정
        labels = {
            "first_name" : "Your first name",
            "last_name" : "Your last name",
            "stars" : "Rating"
        }
        # 커스텀 Error msg
        error_messages = {
            "stars" : {
                "min_value" : "최소 점수는 1점 입니다.",
                "max_value" : "최대 점수는 5점 입니다."
            }
        }