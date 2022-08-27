from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact


def inquiry(request):
    if request.method == "POST":
        contact_id = request.POST['contact_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                contact_id=contact_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry")
                return render('contacts/inquiry.html')
        contact = Contact(contact_id=contact_id, name=name, email=email,
                              phone=phone, address=address, message=message, user_id=user_id)
        contact.save()
        # send email
        '''
        print(f" 'Listing Inquiry',
              'Inquiry for' + listing + '.Sign into admin for more info',
              'francis@nikka.net.cn',
              [realtor_email, 'francis@nikka.net.cn'], fail_silently=False")

        
        send_mail(
            'Listing Inquiry',
            'Inquiry for' + listing + '.Sign into admin for more info',
            'francis@nikka.net.cn',
            [realtor_email, 'francis@nikka.net.cn'],
            fail_silently=False
        ) '''
        messages.success(
            request, 'Your request has been submitted, we will get back to you soon')
        return render('contacts/inquiry.html')
