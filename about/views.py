from django.shortcuts import render
from .models import About, CollaborateRequest
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    template_name = "about/index.html"

    collaborate_form = CollaborateForm()

    return render(request, "about/about.html", {"about": about, "collaborate_form": collaborate_form,})