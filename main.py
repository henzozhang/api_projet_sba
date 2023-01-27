# # from flask import Flask, request
# # from joblib import load

# # app = FastAPI()

# # # Chargement du modèle
# # model = load('my_pipe_vot.pkl')

# # @app.route('/predict', methods=['POST'])
# # def predict():
#     # Récupération des variables d'entrée
#     data = request.get_json()
#     state = data['state']
#     bankstate = data['bankstate']
#     naics = data['naics']
#     term = data['term']
#     noemp = data['noemp']
#     newexist = data['newexist']
#     createjob = data['createjob']
#     retainedjob = data['retainedjob']
#     franchisecode = data['franchisecode']
#     urbanrural = data['urbanrural']
#     revlinecr = data['revlinecr']
#     lowdoc = data['lowdoc']
#     grappv = data['grappv']
    
# #     # Prédiction
# #     prediction = model.predict([[state, bankstate, naics, term, noemp, newexist, createjob, retainedjob, franchisecode, urbanrural, revlinecr, lowdoc, grappv]])
    
# #     return prediction

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=8000)

# from joblib import load
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
# from sklearn.datasets import load_iris


# # Chargement du modèle
# loaded_model = load('my_pipe_vot.pkl')

# # Création d'une nouvelle instance fastAPI
# app = FastAPI()

# # Définir un objet (une classe) pour réaliser des requêtes
# # dot notation (.)
# class request_body(BaseModel):
#     sepal_length : float
#     sepal_width : float
#     petal_length : float
#     petal_width : float

# # Definition du chemin du point de terminaison (API)
# @app.post("/predict") # local : http://127.0.0.1:8000/predict

# # Définition de la fonction de prédiction
# def predict(data : request_body):
#     # Nouvelles données sur lesquelles on fait la prédiction
#     new_data = [[
#         data.sepal_length,
#         data.sepal_width,
#         data.petal_length,
#         data.petal_width
#     ]]

#     # Prédiction
#     class_idx = loaded_model.predict(new_data)[0]

#     # Je retourne le nom de l'espèce iris
#     return {'class' : iris.target_names[class_idx]}


from fastapi import FastAPI
from model import predict
from pydantic import BaseModel

class Textin(BaseModel):
    state : str
    bankstate : str
    naics : str
    term : int
    noemp : int
    newexist : str
    createjob : int
    retainedjob : int
    franchisecode : str
    urbanrural : str
    revlinecr : str
    lowdoc : str
    grappv : int
    

class Prediction(BaseModel):
    mis_status : bool

app = FastAPI()

@app.post("/predict", response_model=Prediction)
async def root_predict(payload : Textin):
    value = [x for x in payload.__dict__.values()]
    to_return = predict(value)
    return {"mis_status": to_return}