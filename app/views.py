from django.shortcuts import render
from .models import contact
from .forms import RegisterContact
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def acceuil(request):
    form = RegisterContact()
    x ="ds"
    template = "acceuil.html"
    if request.method == 'POST':
        form = RegisterContact(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Message = form.cleaned_data['Message']
            Subject = form.cleaned_data['Subject']
            message = contact.objects.create(Name=Name,Email=Email,Message=Message,Subject=Subject)
            message.save()
        else :
            print("not valid")
            print(form.__str__)
    return render(request,template,{'form':form})
def adm(request):
    template = "message.html"
    message = contact.objects.all().order_by("-id")
    return render(request,template,{'message':message})
def user(request):
    template = "users.html"
    message = contact.objects.all().order_by("-id")
    return render(request,template,{'message':message})
def deleteMail(request,pk):
    template = "base.html"
    toDelete=contact.objects.get(id=pk)
    toDelete.delete()
    return HttpResponseRedirect('/adm')

def sendMail(request,pk):
    template = "send_email.html"
    email=contact.objects.get(id=pk)
    email = email.Email
    return render(request,template,{"email":email})