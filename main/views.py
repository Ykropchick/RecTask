from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    name = request.GET.get("name") or 'Rekruto'
    message = request.GET.get("message") or "Давай дружить"
    return HttpResponse(f"<h1>Hello {name}! {message}!")

