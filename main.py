from schemas import PassengerListData
from schemas import PassengerData
from fastapi import FastAPI
from joblib import load
from dotenv import load_dotenv
from os import getenv
load_dotenv()
app = FastAPI()
model_name= getenv("MODEL")
model =load(model_name)

metadata={
    "classes":{0:"Didn't Survive",1:"Survived"}
}

def predict(data:list):
    predictions=model.predict(data)
    results = []
    for prediction in predictions:
        results.append(metadata["classes"][prediction])
    return results

# predictions =model.predict([[12,45,3,1,25,0,1,1]])
# results = []
# print(predictions)
# for prediction in predictions:
#     results.append(metadata["classes"][prediction])

# print(results)


# [['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S',
#        'Sex']]
def transform_data (passenger_list_data:list[PassengerData]):
    transformed_data  =[]
    for data in passenger_list_data:
        print(data)
        passenger_transformed_data =[]
        passenger_transformed_data.append(data.passenger_class)
        passenger_transformed_data.append(data.age)
        passenger_transformed_data.append(data.number_of_spouses+data.number_of_siblings)
        passenger_transformed_data.append(data.number_of_parents+data.number_of_children)
        passenger_transformed_data.append(data.fare)
        passenger_transformed_data.append(1 if data.embarked =="Q" else 0)
        passenger_transformed_data.append(1 if data.embarked =="S" else 0)
        passenger_transformed_data.append(1 if data.sex =="female" else 0)
        transformed_data.append(passenger_transformed_data)
    return transformed_data

@app.post('/models/prediction')
def survival_prediction_handler(passenger_data: PassengerData):
    passenger_transformed_data=transform_data([passenger_data])
    results = predict(passenger_transformed_data)
    return {"data":results}

    
@app.post('/models/batch-prediction')
def survival_prediction_handler(passenger_list_data: PassengerListData):
    
    passenger_transformed_data=transform_data(passenger_list_data.data)
    results = predict(passenger_transformed_data)
    return {"data":results}


        
