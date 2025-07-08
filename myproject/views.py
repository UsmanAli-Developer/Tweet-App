from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from service.models import SKILL
from service.models import login
from service.models import tweet
from django.contrib.auth.decorators import login_required


def home(request):
    data = SKILL.objects.all()
    
    show = {
        'servicedata': data
    }
    
    return render(request, "index.html", show)



def header(request):
    return render(request,'header.html')

def page(request):

    if request.method == "POST":
     
     name=request.POST.get("user")

     email=request.POST.get("email")

     password=request.POST.get("password")

     page=login(name=name,email=email,password=password)

     page.save()

     return redirect('hello')

    return render(request,'login.html')




def home(request):
     mes = tweet.objects.all()
     if request.method=='GET':
        sb=request.GET.get('searchbar')
        if sb!=None:
            mes = tweet.objects.filter(title=sb)
     
     return render(request,'home.html', {'mes': mes})




def tweetm(request):
     
      if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        image = request.FILES.get("image")

        tweeter = tweet(title=title, desc=desc, image=image)
        tweeter.save()

        return redirect("/home/")

      mes = tweet.objects.all()
      return render(request, 'tweet.html', {'mes': mes})



def delete(request,id):
    if request.method == 'POST':
     dl=tweet.objects.get(pk=id)
     dl.delete()
    return redirect('/home/')



def update(request, id):
     
     dl = tweet.objects.get(pk=id) 
     if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        image = request.FILES.get("image")

        dl.title = title
        dl.desc = desc
        if image:
            dl.image = image

        dl.save()
        return redirect("/home/")
    
     return render(request, 'update.html', {'data': dl})

      
    