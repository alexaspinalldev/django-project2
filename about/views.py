from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages



def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collab_form = CollaborateForm()

    if request.method == "POST":
        collab_form = CollaborateForm(data=request.POST)
        if collab_form.is_valid():
            collabRequest = collab_form.save
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    return render(
        request,
        "about/about.html",
        {"about": about, "collab_form": collab_form
},
    )