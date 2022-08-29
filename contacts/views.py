
from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact


def inquiry(request):
    return render(request, "contacts/inquiry.html", {})


def contact(request):
    # if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    message = request.POST['message']
    member = Contact.objects.all().filter()
    member = Contact(name=name, email=email, phone=phone,
                     address=address, message=message)
    member.save()

    # if request.user.is_authenticated:
    #     user_id = request.user.id
    #     has_contacted = Contact.objects.all().filter(
    #         contact_id=contact_id, user_id=user_id)
    #     if has_contacted:
    #         messages.error(request, "You have already made an inquiry")
    #         response = redirect('contact')
    #         return response
    #         # return render('contacts/contact.html')
    # contact = Contact(contact_id=contact_id, name=name, email=email,
    #                   phone=phone, address=address, message=message, user_id=user_id)
    # contact.save()

    # messages.success(
    #     request, 'Your request has been submitted, we will get back to you soon')
    # response = redirect('contact')
    # return response
    return render(request, "accounts/dashboard.html")
