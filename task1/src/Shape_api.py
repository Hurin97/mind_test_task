from Figures.Circle import Circle
from Figures.Triangle import Triangle
from fastapi import FastAPI, Query
from typing import Annotated, Union
import json


app = FastAPI()

class Shape_api:
    
    @app.get("/api/v1/shape")
    def get_area(a: Annotated[Union[float, None], Query()] = None, b: Annotated[Union[float, None], Query()] = None, 
                 c: Annotated[Union[float, None], Query()] = None, radius: Annotated[Union[float, None], Query()] = None, right_tr:Annotated[Union[bool, None], Query()] = False):
        area = None
        right_triangle = None
        if a!=None and b!=None and c!=None and radius==None:
            try:
                triangle = Triangle(a,b,c)
                area = triangle.get_area()
                if right_tr==True:
                    right_triangle= triangle.is_right_triangle()
            except Exception as er:
                return "Alert! {0}".format(er)
        if a==None and b==None and c==None and radius!=None:
            area = Circle(radius).get_area()
        response = dict()
        response['area'] = area
        response['is_right_triangle'] = right_triangle
        return json.dumps(response)