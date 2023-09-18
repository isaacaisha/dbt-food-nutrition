import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
type_ = os.getenv("TYPE")
app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")

type_nutri = os.getenv("TYPE_NUTRI")
app_id_nutri = os.getenv("APP_ID_NUTRI")
app_key_nutri = os.getenv("APP_KEY_NUTRI")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    recipe_data = None
    nutritional_info = None

    if request.method == 'POST':
        if 'search_query' in request.form:
            search_query = request.form['search_query']
            # Construct the API request URL with the user's query
            api_url = (f'https://api.edamam.com/api/recipes/v2?type={type_}&q={search_query}&app_id={app_id}'
                       f'&app_key={app_key}')
            # Send the GET request to the API
            response = requests.get(api_url)
            if response.status_code == 200:
                recipe_data = response.json()
                # Process and display recipe data as needed
                print(recipe_data)
            else:
                print(f'Error: {response.status_code}')
                print(response.text)  # Print the response content for more details

        if 'ingredients' in request.form:
            ingredients = request.form['ingredients']
            # Construct the API request URL with the user's ingredients
            api_url = (f'https://api.edamam.com/api/nutrition-data?app_id={app_id_nutri}&app_key={app_key_nutri}'
                       f'&nutrition-type={type_nutri}&ingr={ingredients}')
            # Send the GET request to the API
            response = requests.get(api_url)
            if response.status_code == 200:
                nutritional_info = response.json()
                # Process and display nutritional information as needed
                print(nutritional_info)
            else:
                print(f'Error: {response.status_code}')
                print(response.text)  # Print the response content for more details

    return render_template('index.html', recipe_data=recipe_data, nutritional_info=nutritional_info,
                           date=datetime.now().strftime("%a %d %B %Y"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
