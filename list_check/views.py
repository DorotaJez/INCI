from django.shortcuts import render
from .forms import IngredientForm
from .models import Ingredient

# Create your views here.

def home(request):
    return render(request, 'homepage.html', {})

def adding(response):
    form = IngredientForm()
    return render(response, "adding.html", {"form":form})

def analyse(request):
    if request.method == 'POST':
        input_list = str(request.POST['name']).split(', ')
        subs_dict = {}
        for el in input_list:
            if Ingredient.objects.filter(name=el).exists():
                found_ingr = Ingredient.objects.get(name=el)
                description = getattr(found_ingr,"description")
                subs_dict.update({el: description})
        if len(subs_dict) != 0:
            return render(request, 'results.html', {'subs_dict':subs_dict, 'subs_names': subs_dict.keys, 'subs_desc': subs_dict.values(), 'found': True})
        else:
            return render(request, 'results.html', {'found': False})
    else:
        form = IngredientForm()
        return render(request, 'results.html', {'form': form})