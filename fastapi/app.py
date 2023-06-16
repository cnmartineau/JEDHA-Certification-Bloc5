import pickle
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import  OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression

description = """

### API to estimate optimum car rental price 

This API is meant to help car owners to define the optimum price for renting their car on the 
Getaround application depending on the characteristics of the car.
"""

tags_metadata = [
    {
        "name": "Default",
        "description": ""
    },
    {
        "name": "Price prediction",
        "description": ""
    }
]

# load preprocessor and model 
def load_pickle(filename):
    with open(filename, 'rb') as file:
        contents = pickle.load(file)
    return contents
preprocessor = load_pickle("preprocessor.pkl")
model = load_pickle("model.pkl")

# define data types
class PredictionRequest(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool

# create app
app = FastAPI(
    title = "Getaround - Prediction",
    description = description,
    version = "0.1",
    openapi_tags = tags_metadata)

# set home endpoint
@app.get("/", tags = ["Default"])
async def home():
    message = "This is the default endpoint. The documentation of the api is available at /docs."
    return message

# set predict endpoint
@app.post("/predict", tags = ["Price prediction"])
async def prediction(features: PredictionRequest):

    """
    Input data should be sent as a json following this format:

    * model_key : Citroën, Peugeot, PGO, Renault, Audi, BMW, Ford, Mercedes, Opel,
                  Porsche, Volkswagen, KIA Motors, Alfa Romeo, Ferrari, Fiat, 
                  Lamborghini, Maserati, Lexus, Honda, Mazda, Mini, Mitsubishi,
                  Nissan, SEAT, Subaru, Suzuki, Toyota, Yamaha
    * mileage : numerical value
    * engine_power : numerical value
    * fuel : diesel, petrol, hybrid_petrol, electro
    * paint_color : black, grey, white, red, silver, blue, orange, beige, brown, green
    * car_type : convertible, coupe, estate, hatchback, sedan, subcompact, suv, van
    * private_parking_available : True, False
    * has_gps : True, False
    * has_air_conditioning : True, False
    * automatic_car : True, False
    * has_getaround_connect : True, False
    * has_speed_regulator : True, False
    * winter_tires : True, False
    """

    # read data 
    car_features = pd.DataFrame({
        "model_key": [features.model_key],
        "mileage": [features.mileage],
        "engine_power": [features.engine_power],
        "fuel": [features.fuel],
        "paint_color": [features.paint_color],
        "car_type": [features.car_type],
        "private_parking_available": [features.private_parking_available],
        "has_gps": [features.has_gps],
        "has_air_conditioning": [features.has_air_conditioning],
        "automatic_car": [features.automatic_car],
        "has_getaround_connect": [features.has_getaround_connect],
        "has_speed_regulator": [features.has_speed_regulator],
        "winter_tires": [features.winter_tires]
        })

    # preprocess and predict
    car_features2 = preprocessor.transform(car_features)
    prediction = model.predict(car_features2)
    prediction = np.round(prediction,0)

    # format and return response
    response = {"price": prediction.tolist()[0]}
    return response

if __name__=="__app__":
    uvicorn.run(app, host="0.0.0.0", port=4000)
