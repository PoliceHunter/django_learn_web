from django.shortcuts import render

def home_page(request):
    data = {
        'key': 'value'
            }
    return render(request, 'main/index.html', data)

def about_page(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')