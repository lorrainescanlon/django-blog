from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    template_name = "about/index.html"

    return render(request, "about/about.html", {"about": about},)