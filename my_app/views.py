from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

articles = {
    "sports" : "Sports Page",
    "finance" : "Finance Page",
    "politics" : "Politics Page"
}

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY_APP")

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")

# 동적 뷰 생성
def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        # NotFound 처리
        # return HttpResponseNotFound("No page for that topic!")
        raise Http404("404 GENERIC ERROR :(") # 사용자 지정 404.html 같은 템플릿 연결 가능

def add_view(request, num1, num2):
    # domain.com/my_app/num1/num2 -> num1 + num2
    # domain.com/my_app/3/4 -> 7
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}" # domain.com/my_app/3/4 -> 3 + 4 = 7
    return HttpResponse(str(result))