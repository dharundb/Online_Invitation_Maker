from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from num2words import num2words

# for sending mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from .models import *

pid = ''
cntct = ''
dat = ''
ordinal=''

def cred_wed(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method =="POST":
        occasion="Wedding"
        groom = request.POST["Groom"]
        bride = request.POST["Bride"]
        address = request.POST["Address"]
        contact = request.POST["Contact"]
        date =  request.POST["Date"]
        time = request.POST["Time"]
        global cntct
        global dat
        cntct=contact
        dat=date

        if(len(groom)==0 or len(bride)==0 or len(address)==0 or len(contact)==0 or len(date)==0 or len(time)==0):
            messages.info(request,"Do not leave Credentials blank!")
            return redirect('wed')
        else:
            s=wed_credential(occasion=occasion,groom=groom,bride=bride,address=address,contact=contact,date=date,time=time)
            flag=s.save()
            if flag is None:
                return redirect('/stylings/tempw')
            else:
                messages.info(request,"Credentials has not been saved!")
                return redirect('wed')
    return render(request,'credw.html')

def cred_gather(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method =="POST":
        occasion=request.POST["Occasion"]
        address = request.POST["Address"]
        contact = request.POST["Contact"]
        date =  request.POST["Date"]
        time = request.POST["Time"]
        global cntct
        global dat
        cntct=contact
        dat=date

        if(len(occasion)==0 or len(address)==0 or len(date)==0 or len(contact)==0 or len(time)==0):
            messages.info(request,"Do not leave Credentials blank!")
            return redirect('gather')
        else:
            s=gath_credential(occasion=occasion,address=address,contact=contact,date=date,time=time)
            flag=s.save()
            if flag is None:
                return redirect('/stylings/tempg')
            else:
                messages.info(request,"Credentials has not been saved!")
                return redirect('gather')
    return render(request,'credg.html')

def cred_bday(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    ord_ = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    if request.method =="POST":
        occasion="Birthday"
        name = request.POST["Name"]
        address = request.POST["Address"]
        contact = request.POST["Contact"]
        date =  request.POST["Date"]
        time = request.POST["Time"]
        age = request.POST["Age"]
        global cntct
        global dat
        global ordinal
        cntct=contact
        dat=date
        ordinal = ord_(int(age))

        if(len(name)==0 or len(address)==0 or len(date)==0 or len(contact)==0 or len(time)==0):
            messages.info(request,"Do not leave Credentials blank!")
            return redirect('bday')
        else:
            s=bday_credential(occasion=occasion,name=name,address=address,contact=contact,date=date,time=time,age=age)
            flag=s.save()
            if flag is None:
                return redirect('/stylings/tempb')
            else:
                messages.info(request,"Credentials has not been saved!")
                return redirect('bday')
    return render(request,'credb.html')

def occ(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    return render(request,'occasion.html')

def temp_wed(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method=="POST":
        global pid
        pid = request.POST["pic"]
        return redirect("wedstyle")
    images = (Media.objects.filter(tag="Wedding"))
    return render(request,'tempw.html',{"images":images})

def temp_gath(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method=="POST":
        global pid
        pid = request.POST["pic"]
        return redirect("gathstyle")
    images = (Media.objects.filter(tag="Gathering"))
    return render(request,'tempg.html',{"images":images})

def temp_bday(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method=="POST":
        global pid
        pid = request.POST["pic"]
        return redirect("bdaystyle")
    images = (Media.objects.filter(tag="Birthday"))
    return render(request,'tempb.html',{"images":images})

def wedstyling(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    global pid
    images = (Media.objects.filter(pic_url=pid)).first()
    temp = wed_credential.objects.filter(contact=cntct,date=dat)
    wcred = temp.first()
    return render(request, "wedstyle.html", {"wcred":wcred,"pid":pid,"images":images})

def gathstyling(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    global pid
    images = (Media.objects.filter(pic_url=pid)).first()
    temp = gath_credential.objects.filter(contact=cntct,date=dat)
    gcred = temp.first()
    return render(request, "gathstyle.html", {"gcred":gcred,"pid":pid,"images":images})

def bdaystyling(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    global pid
    global ordinal
    images = (Media.objects.filter(pic_url=pid)).first()
    temp = bday_credential.objects.filter(contact=cntct,date=dat)
    bcred = temp.first()
    return render(request, "bdaystyle.html", {"bcred":bcred,"pid":pid,"ordinal":ordinal,"images":images})

def edit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    global pid
    images = (Media.objects.filter(pic_url=pid)).first()
    return render(request,"edit.html",{"images":images})

def sendmail(eml, txt, sub):
    mail_content = txt
    # The mail addresses and password
    sender_address = "invitation.team10@gmail.com"
    sender_pass = "spdteam10"
    receiver_address = eml

    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = receiver_address
    message["Subject"] = sub
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, "plain"))
    attach_file_name = "C:\\Users\\DHARUN DB\\Downloads\\SPD_Invitation.png"
    attach_file = open(attach_file_name, "rb")  # Open the file as binary mode
    payload = MIMEBase("application", "octate-stream")
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header("Content-Decomposition", "attachment", filename=attach_file_name)
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    return "Mail Sent"

def mailshare(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    if request.method == "POST":
        em = str(request.POST["email"])
        text = str(request.POST["txt"])
        subj = str(request.POST["subject"])
        #loc = str(request.POST["location"])
        msg = sendmail(em, text, subj)
        messages.info(request, msg)
    return render(request,"mailshare.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))
