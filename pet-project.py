rom flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
          <h1>Adopt a Pet!</h1>
          <p>Browse through the links below to find your new furry friend:</p>
          <ul>
            <li><a href='/animals/dogs'>Dogs</a></li>
            <li><a href='/animals/cats'>Cats</a></li>
            <li><a href='/animals/rabbits'>Rabbits</a></li>
           </ul> 
          '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'''
            <h1>List of {pet_type}</h1>
            <ul>
          '''
  for pet_kind in pets.keys():
    if pet_kind == pet_type:
      for index, pet_attributes in enumerate(pets[pet_kind]):
        html = html + f"<li><a href='/animals/{pet_type}/{index}'>{pet_attributes['name']}</a></li>"
  return html + '</ul>'


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = {}
  pet_list = []
  for pet_kind in pets.keys():
    if pet_kind == pet_type:
        pet_list = pets[pet_kind]
        pet = pet_list[pet_id]
  html = f'''
            <h1>{pet['name']}</h1>
            <img src={pet['url']}>
            <p>{pet['description']}</p>
            <ul>
              <li>Breed: {pet['breed']}</li>
              <li>Age: {pet['age']}</li>
            </ul>
          '''   
  return html
