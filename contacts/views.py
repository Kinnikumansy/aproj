import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact

# Create your views here.

# created by uni


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail
        print(
            f"'Listing Inquiry','Inquiry for' + listing + '. Sign into admin for more info','ryan@ryan',[realtor_email, 'ryan@ryan'], fail_silently=False")
        messages.success(
            request, 'Your request had been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
