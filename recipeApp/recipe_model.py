import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_recipe(ingredients, meal_type, cuisine_preference, cooking_time, complexity):
    prompt = (f"Create a recipe with the following details and give me the Name for that recipe.\n"
              f"Title: Generate a title based on the recipe details"
              f"Ingredients which I have: {ingredients}\n"
              f"Meal type which i most prefered : {meal_type}\n"
              f"Cuisine: {cuisine_preference}\n"
              f"Cooking time: {cooking_time}\n"
              f"Complexity: {complexity}\n"
              f"Instructions: ")

    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Create attention mask
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

    # Generate text
    output = model.generate(
        input_ids, 
        max_length=500, 
        num_beams=5, 
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        early_stopping=True, 
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=50,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=attention_mask
    )

    # Decode the output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract instructions from the generated text
    instructions = generated_text.split("Instructions:")[1].strip()

    return instructions
