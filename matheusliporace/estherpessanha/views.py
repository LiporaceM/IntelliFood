from django.shortcuts import render
import requests
from django.http import HttpResponseNotFound
from googletrans import Translator

# Chave da API do Gemini
API_KEY = ''
API_URL = '' + API_KEY


recipes_data = []

def home(request):
    return render(request, 'home.html')

def search_recipes(request):
    global recipes_data
    if request.method == 'POST':
        ingredientes = request.POST.getlist('ingredientes')
        tempo = request.POST.get('tempo')

        
        prompt_text = (
            f"What are 5 recipes I can make with only the following ingredients: {', '.join(ingredientes)}, no other ingredients outside the ones previously mentioned should be in the recipe "
            f"in less than {tempo} minutes? Please return the recipe name, preparation time, ingredients list, and instructions in the following format: "
            f"**Recipe:** [recipe name] **Preparation time:** [time] **Ingredients:** [list of ingredients] **Instructions:** [instructions]."
        )

        
        response = requests.post(
            API_URL,
            headers={'Content-Type': 'application/json'},
            json={
                'prompt': {
                    'text': prompt_text
                }
            }
        )

        
        recipes_data = []
        if response.status_code == 200:
            response_data = response.json()
            if 'candidates' in response_data:
                candidates = response_data['candidates']
                for candidate in candidates:
                    recipe_text = candidate.get('output', '')
                    
                    recipes_data.extend(parse_recipes_from_text(recipe_text))

               
                translator = Translator()
                for recipe in recipes_data:
                    recipe['name'] = translator.translate(recipe['name'], src='en', dest='pt').text
                    recipe['ingredients'] = [translator.translate(ingredient, src='en', dest='pt').text for ingredient in recipe['ingredients']]
                    recipe['instructions'] = translator.translate(recipe['instructions'], src='en', dest='pt').text
                    recipe['image_url'] = search_image(recipe['name'])  
        else:
            print("Erro na solicitação da API:", response.text)

        return render(request, 'search.html', {'recipes': recipes_data, 'ingredientes': ingredientes, 'tempo': tempo})
    return render(request, 'search.html')

def parse_recipes_from_text(text):
    recipes = []
    
    recipe_parts = text.split('**Recipe:**')
    for part in recipe_parts[1:]:
        
        name = ""
        prep_time = ""
        ingredients = []
        instructions = []

        
        lines = part.strip().split('\n')
        for i, line in enumerate(lines):
            
            if i == 0:
                name = line.strip().replace('**', '')
            
            elif line.startswith('**Preparation time:**'):
                prep_time = line.split('**Preparation time:**')[1].strip()
           
            elif line.startswith('* '):
                ingredients.append(line.strip().lstrip('* ').strip())
           
            elif line.startswith('**Instructions:**'):
                instructions = ' '.join(lines[i+1:]).replace('**Instructions:**', '').strip()
                break
        
       
        recipes.append({
            'name': name,
            'prep_time': prep_time,
            'ingredients': ingredients,
            'instructions': instructions,
            'id': len(recipes) + 1,
            'image_url': 'https://via.placeholder.com/100'
        })
    
    return recipes

def search_image(query):
    # Chave da API do Google Custom Search e ID do mecanismo de pesquisa
    API_KEY = ''
    SEARCH_ENGINE_ID = ''
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={API_KEY}&searchType=image&num=1"
    
    response = requests.get(search_url)
    if response.status_code == 200:
        search_results = response.json()
        if 'items' in search_results:
            image_url = search_results['items'][0]['link']
            return image_url

    return "https://via.placeholder.com/100"

def recipe_detail(request, recipe_id):
    global recipes_data
    recipe = next((r for r in recipes_data if r['id'] == recipe_id), None)
    if recipe is None:
        return HttpResponseNotFound("Recipe not found")
    return render(request, 'recipe_detail.html', {'recipe': recipe})
