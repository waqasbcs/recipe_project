from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe

def index(request):
    peoples = [
        {'name': 'waqas','age':'20','city': 'lohore',},
        {'name': 'ishfaq','age':'21','city': 'perdos',},
        {'name': 'aleem','age':'22','city': 'dargai',},  
        {'name': 'yasir','age':'23','city': 'swat',}, 
        {'name': 'maryam','age':'18','city': 'mardan',},       
    ]
    return render(request, 'index.html', context={'peoples': peoples})

def about(request): 
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def recipe(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

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
        context = {'recipe': queryset}  
        return render(request, 'recipe.html', context)  

    return HttpResponseNotAllowed(['GET', 'POST'])


def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.delete()
        return redirect('recipe') 

def update_recipe(request, recipe_id):
    recipe_instance = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image') 
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        # Update the attributes of the recipe_instance
        recipe_instance.recipe_name = recipe_name
        recipe_instance.recipe_description = recipe_description
        
        if recipe_image:
            recipe_instance.recipe_image = recipe_image
        
        # Save the updated recipe_instance
        recipe_instance.save()
        return redirect('recipe')  
        
    context = {'recipe': recipe_instance}
    return render(request, 'update.html', context)