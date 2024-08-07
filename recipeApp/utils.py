import spacy 
import os 

# load NLP model 
nlp = spacy.load('en_core_web_sm')

def process_user_input(ingredients, meal_type, cuisine_preference, cooking_time, complexity):
    text = f"{ingredients} {meal_type} {cuisine_preference} {cooking_time} {complexity}"
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# def generate_recipe_with_ai(keywords, ingredients, meal_type, cuisine_preference, cooking_time, complexity):
#     recipe_instructions = []
#     try: 
#         recipe_title = f"{meal_type} with {cuisine_preference} flavors"
#         recipe_ingredients = ingredients.split(', ')  # Assuming ingredients are comma-separated
#         if len(recipe_ingredients) < 2:
#             raise ValueError("Not enough ingredients provided.")
        
#         recipe_instructions = [
#             f"Prepare the {recipe_ingredients[0]} by doing XYZ.",
#             f"Cook the {recipe_ingredients[1]} for {cooking_time}.",
#             f"Combine all ingredients and enjoy your {complexity.lower()} {recipe_title}!"
#         ]
#     except Exception as e:
#         print(e)
    
#     return {
#         'title': recipe_title,
#         'ingredients': recipe_ingredients,
#         'instructions': recipe_instructions
#     }
