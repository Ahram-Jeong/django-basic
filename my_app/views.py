from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
'''
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

# Redirects (not the typical way)
# domain.com/my_app/0 -Redirect-> domain.com/my_app/finance
def num_page_view(request, num):
    topics_list = list(articles.keys()) # ["sports", "finance", "politics"]
    topic = topics_list[num]

    # topic-page라는 url 경로를 찾고 있는데, 이 topic으로 보내주세요.
    return HttpResponseRedirect(reverse("topic-page", args = [topic])) # topic을 특정 url 경로로 전달
'''

# 템플릿에 뷰 연결
def simple_view(request):
    # my_app/templates/my_app/example_old.html
    return render(request, "my_app/example.html")

def variable_view(request):
    my_var = {
        "first_name" : "wooDz",
        "last_name" : "CHO",
        "some_list" : [1, 2, 3],
        "some_dict" : {
            "inside_key" : "inside_value"
        },
        "user_logged_in" : True
    }

    return render(request, "my_app/variable.html", context = my_var)

def example_view(request):
    return render(request, "my_app/example02.html")