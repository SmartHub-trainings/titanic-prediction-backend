from pydantic import BaseModel,Field
from typing import Literal

['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S',
       'Sex']

class PassengerData(BaseModel):
    passenger_class:int = Field(3,ge=1,le=3)
    age:int = Field(...,ge=0,le=100)
    number_of_spouses:int = Field(...,ge=0)
    number_of_siblings:int = Field(...,ge=0)
    number_of_parents:int = Field(...,ge=0)
    number_of_children:int = Field(...,ge=0)
    fare:float = Field(...,gt=0)
    embarked:Literal["S","C","Q"]
    sex:Literal["male","female"]

class PassengerListData(BaseModel):
    data: list[PassengerData]