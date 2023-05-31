from django.shortcuts import render
from myapp.models import newpost
# Create your views here.
def home_view(request):
    post=newpost.objects.all()
    print(post)
    context={
        'posts':post
    }
    return render(request,'home.html',context)
def newpost_view(request):
    return render(request,'newpost.html',{})
def add_action(request):
    title=request.POST.get('title')
    descr=request.POST.get('descr')
    print(title)
    print(descr)
    new=newpost(name=title,descr=descr)
    new.save()
    post=newpost.objects.all()
    print(post)
    context={
        'posts':post
    }
    return render(request,'home.html',context)
def delete_post(request, pk):
    print("In delete")
    newpost.objects.filter(pk=pk).delete()

    post = newpost.objects.all()
    print(post)
    context = {
        'posts': post
    }
    return render(request, 'home.html', context)
