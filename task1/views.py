from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Recipe
# Create your views here.
def index(request):
    peoples = [
        {'name': 'waqas','age':'20','city': 'lohore',},
        {'name': 'ishfaq','age':'21','city': 'perdos',},
        {'name': 'aleem','age':'22','city': 'dargai',},  
        {'name': 'yasir','age':'23','city': 'swat',}, 
        {'name': 'maryam','age':'18','city': 'mardan',},       
              
             
    ]
    return render(request, 'index.html',context = {'peoples':peoples})
def about(request): 
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image') 
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        return redirect('/recipe/')  

    elif request.method == 'GET':
        queryset = Recipe.objects.all()
        context = {'recipe': queryset}
        return render(request, 'recipe.html',context)  
    return HttpResponseNotAllowed(['GET', 'POST']) 


def learn_math(request):
    a=10+10
    return HttpResponse(a)

def learn_format(request):
    a='geekyshows'
    return HttpResponse(f'how are you {a}')

