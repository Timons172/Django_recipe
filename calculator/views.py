from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}

def home_view(request):
    template_name = 'home/home.html'
    pages = {}
    for dish in DATA.keys():
        pages[dish] = dish
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipe_view(request, dish):
    template_name = 'calculator/index.html'
    recipe = DATA.get(dish)
    servings = int(request.GET.get('servings', 1))
    new_recipe = {ingredient: round(amount * servings, 2) for ingredient, amount in recipe.items()}
    context = {
        'recipe': new_recipe
    }

    return render(request, template_name, context)
