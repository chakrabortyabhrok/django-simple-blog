from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Home Page coming soon...")

def about_page(request):
    return HttpResponse("About Page coming soon...")

def blog_list(request):
    return HttpResponse("Blog Page coming soon...")
