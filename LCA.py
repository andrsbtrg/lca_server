import json
from json import JSONEncoder

class material:
    def calculate_sdev(impact:dict):
        sdev = {}
        for key in impact:
            sd = impact[key]**1.27
            sdev[key] = sd
        return sdev

    def __init__(self, name, GWP:dict, unit, unit_value):
        self.name = name
        self.GWP = self.convert_to_float(GWP)
        self.unit = unit
        self.unit_value = unit_value
        # self.sdev = self.calculate_sdev()
    
    def __iter__(self):
        yield from{
            "name":self.name,
            "GWP": self.GWP,
            "unit": self.unit,
            "unit_value": self.unit_value
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return self.__str__()
    
    def to_object(d):
        inst = material(d['name'], d['GWP'], d['unit'], d['unit_value'])
        return inst
        
    
    def convert_to_float(self, impact_str:dict):
        impact_float = {}
        for key in impact_str:
            value_f = float(impact_str[key])
            if (value_f != None):
                impact_float[key] = value_f
        
        return impact_float


class assembly:
    def __init__(self, materials:list, qt:float):
        self.materials = materials
        self.qt = qt
        self.quantity = self.qt


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  
