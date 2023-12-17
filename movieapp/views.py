from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):

    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return render(request, 'index.html',context)    
def details(request,movie_id):
    #return HttpResponse("this is movie number %s"% movie_id)

    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movie_obj=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie_obj)
    
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie_obj})
def delete(request,id):
    if request.method=='POST':
        movie_obj=Movie.objects.get(id=id)
        movie_obj.delete()
        return redirect("/")
    return render(request,'delete.html')