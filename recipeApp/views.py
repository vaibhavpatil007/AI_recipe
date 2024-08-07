# from django.shortcuts import render, redirect
# from recipeApp.models import *
# from recipeApp.utils import *

# # Create your views here.
# def recipe_input(request):
#     context = ''
#     if request.method == 'POST':
#         ingreadients = request.POST.get('ingredients')
#         meal_type = request.POST.get('meal-type')
#         cuisine_preference = request.POST.get('cuisine-preference')
#         cooking_time = request.POST.get('cooking-tim e')
#         complexity = request.POST.get('complexity')

#         # process input and generate recipe using AI 
#         keywords = process_user_input(ingreadients, meal_type, cuisine_preference, cooking_time, complexity)
#         ai_recipe = generate_recipe_with_ai(keywords, ingreadients, meal_type, cuisine_preference, cooking_time, complexity)
        
#         print(keywords,ai_recipe)
#         # save the recipe in the database 
#         recipe_model.objects.create(
#             ingredients=ingreadients,
#             meal_type=meal_type,
#             cuisine_preference=cuisine_preference,
#             cooking_time=cooking_time,
#             complexity=complexity,
#         )

#         context = {
#             'recipe': ai_recipe,
#         }
#         return render(request,'recipe_result.html',context)
#         # return redirect('/recipeinput')
#     queryset = recipe_model.objects.all()
#     context = {
#         'recipe_view': queryset,
        
#         }


#     # context here
#     # view = {
#     #     'ingredients': ingreadients,    
#     #     'meal_type': meal_type,
#     #     'cuisine_preference': cuisine_preference,
#     #     'cooking_time': cooking_time,
#     #     'complexity': complexity,
#     # }
    
#     return render(request,'recipe_inputPage.html',context)

# ----------------------------------------------Second Code-------------------------------------------

from django.shortcuts import render, redirect
from recipeApp.models import recipe_model
from recipeApp.utils import *
from recipeApp.recipe_model import *

def recipe_input(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients')
        meal_type = request.POST.get('meal-type')
        cuisine_preference = request.POST.get('cuisine-preference')
        cooking_time = request.POST.get('cooking-time')
        complexity = request.POST.get('complexity')

        if not ingredients or not meal_type or not cuisine_preference or not cooking_time or not complexity:
            context = {
                'error': 'All fields are required.',
                'ingredients': ingredients,
                'meal_type': meal_type,
                'cuisine_preference': cuisine_preference,
                'cooking_time': cooking_time,
                'complexity': complexity,
            }
            # return render(request, 'newRecipe_input.html', context)

        # Process input and generate recipe using AI
        ai_recipe_text = generate_recipe(ingredients, meal_type, cuisine_preference, cooking_time, complexity)

        # Parse the AI-generated text
        instruction_list = [instruction.strip() for instruction in ai_recipe_text.split('.') if instruction]

        context = {
            'recipe': {
                'title': 'Generated Recipe',
                'ingredients': ingredients.split(', '),
                'instructions': instruction_list
            }
        }
        print(context)

        # Save the recipe in the database
        recipe_model.objects.create(
            ingredients=ingredients,
            meal_type=meal_type,
            cuisine_preference=cuisine_preference,
            cooking_time=cooking_time,
            complexity=complexity,
        )
        
        return render(request, 'newRecipe_result.html', context)
    
    queryset = recipe_model.objects.all()
    context = {'recipe_view': queryset}
    
    return render(request, 'newRecipe_input.html', context)
