from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def home(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            message_body = f"""
            Thank you for submitting your application.
            These are your details:
            Name = {first_name} {last_name}
            Email = {email}
            Date available = {date}
            Occupation = {occupation}

            Thankyou!
            You will receive feedback soon.                 
            """

            email_message = EmailMessage("Application Submitted Successfully", message_body, to=[email])
            email_message.send()

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            messages.success(request, "Application submitted successfully")

    return render(request,"home.html")

def about(request):
    return render(request,"about.html")