from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First Job Description",
    "Second Job Description"
]

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")


def job_detail(request, id):
    print(type(id))
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    site = "https://www.google.com"
    # return HttpResponse(f'Job Detail Page {id}')
    return HttpResponse(return_html)