from django.shortcuts import render,redirect
from .models import MovieInfo
# Create your views here.
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

def create(request):
    
    if request.POST:
        frm=MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('create')
            
    else:
        frm=MovieForm()

    return render(request,'create.html',{'frm':frm})


@login_required(login_url='login/')
def list(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count
    '''print(request.COOKIES)
    visits=int(request.COOKIES.get('visits',0))
    visits=visits+1'''
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)
    movie_set=MovieInfo.objects.all().order_by('year')
    '''movie_set=MovieInfo.objects.filter(year=2023)'''
    '''movie_set=MovieInfo.objects.exclude(year=2023)'''
    '''movie_set=MovieInfo.objects.filter(acters__name='Mohanlal')''' '''field lookups filter(year__gt='2013')'''
    print(movie_set)
    response=render(request,'list.html',{'recent_movies':recent_movie_set,'movies':movie_set,'visits':count })
    '''response.set_cookie('visits',visits)'''
    return response

def edit(request,pk):

    instance_edit=MovieInfo.objects.get(pk=pk)
    '''
   if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        description=request.POST.get('description')
        instance_edit.title=title
        instance_edit.year=year
        instance_edit.description=description
        instance_edit.save()

  '''

    if request.POST:
        frm=MovieForm(request.POST, request.FILESS, instance=instance_edit)
        if frm.is_valid():
            instance_edit.save()

    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits

        frm=MovieForm(instance=instance_edit)
    return render(request,'create.html',{'frm':frm})

    


def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set })