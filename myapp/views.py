from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home.html')

def description(request):
    return render(request, 'description.html')

def contact(request):
    return render(request, 'contact.html')

def personal_info(request):
    return render(request, 'personal_info.html')