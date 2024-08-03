from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("HOMW VIEW:)")

# 404 커스텀 뷰 추가
def my_custom_page_not_found_view(request, exception):
    return render(request, "error_view.html", status = 404)