from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'active_page':'home'})

def services(request):
    return render(request, 'main/services.html', {'active_page':'services'})

def about(request):
    return render(request, 'main/about.html', {'active_page':'about'})

def contacts(request):
    return render(request, 'main/contacts.html', {'active_page':'contacts'})
