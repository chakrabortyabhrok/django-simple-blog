from django.http import HttpResponse

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