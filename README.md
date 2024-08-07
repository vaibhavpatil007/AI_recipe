# AI Recipe Generator with Django

This project is an AI-based Recipe Generator built with Django. Users can input their preferences for ingredients, meal type, cuisine, cooking time, and complexity. The application processes these inputs using an NLP-based model to generate a customized recipe, complete with ingredients, instructions, related videos, blogs, images, and audio instructions.

## Features

- User input for recipe preferences
- AI-generated recipe with ingredients and instructions
- Related videos, blogs, and images for the generated recipe
- Audio instructions for the recipe

## Prerequisites

- Python 3.8+
- Django 3.2+
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai-recipe-generator.git
    https://github.com/vaibhavpatil007/AI_recipe.git
    cd ai-recipe-generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and visit `http://127.0.0.1:8000/recipeinput/`.

## Project Structure

- `recipeApp/`: Contains the main application code.
  - `models.py`: Defines the database models.
  - `views.py`: Contains the view logic.
  - `urls.py`: Defines the URL routes.
  - `templates/`: HTML templates for the application.
  - `static/`: Static files like CSS and JavaScript.
  - `utils.py`: Helper functions for processing user input and generating AI recipes.

## Usage

1. Navigate to the recipe input page: `http://127.0.0.1:8000/recipeinput/`.
2. Fill in the form with your preferences (ingredients, meal type, cuisine, cooking time, complexity).
3. Submit the form to generate a customized recipe.
4. View the generated recipe, related content, and audio instructions.

## Example Output

- **Title**: Lunch with Mexican Flavors
- **Ingredients**:
  - 1 cup all-purpose flour
  - ½ teaspoon salt
  - 1 egg

- **Instructions**:
  1. Prepare the 1 cup all-purpose flour, ½ teaspoon salt, and 1 egg by doing XYZ.
  2. Cook the beaten mixture for 30 minutes.
  3. Combine all ingredients and enjoy your beginner meal!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

https://drive.google.com/file/d/19xytVEb0WIE-37e-SobF8yJHySaO7-AB/view?usp=sharing

