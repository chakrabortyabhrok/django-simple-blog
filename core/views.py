from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    return render(request, 'core/home.html')

def about_page(request):
    return render(request, 'core/about.html')

def hello_world(request):
    return HttpResponse("<h1>Hello World from Django!</h1>")

def greet_user(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!<h1>")

def post_detail(request, post_id):
    return HttpResponse(f"<h1>Post Detail - ID: {post_id}<h1>")

def blog_post(request, slug):
    return HttpResponse(f"<h1>Blog Post - Slug: {slug}<h1>")

def test_routing(request):
    return HttpResponse(f"<h1>URL Routing is working perfectly!<h1>")

#def contact_page(request):
#    return HttpResponse("<h1>Contact Page</h1><p>Email: example@gmail.com</p>")

def services_page(request):
    return HttpResponse("<h1>Our Services</h1><ul><li>Web Development</li><li>AI Integration</li></ul>")

def dynamic_year(request, year):
    return HttpResponse(f"<h1>Year: {year}</h1><p>This is a dynamic page for {year}</p>")

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("✅ Form submitted successfully!")
            print(form.cleaned_data)
            return render(request, 'core/contact_success.html', {'form' : form})
        
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form' : form})
