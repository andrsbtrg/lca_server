from dataclasses import dataclass, field
import json
from json import JSONEncoder

class material:
    def calculate_sdev(impact:dict):
        sdev = {}
        for key in impact:
            sd = impact[key]**1.27
            sdev[key] = sd
        return sdev

    def __init__(self, name, GWP:dict, reference_size, reference_unit):
        self.name = name
        self.GWP = self.convert_to_float(GWP)
        self.size = reference_size
        self.unit = reference_unit
        
        # self.sdev = self.calculate_sdev()
    def get_factor(self):
        if self.unit == 'Kg':
            factor = 1
        
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


def calculate_mass():
    return [assembly.area * m.get_factor() for m in assembly.materials]

@dataclass
class assembly:
    materials: list[material]
    area: float
    quantity: float = 1
    mass: float = field(default_factory = calculate_mass)
    
    def impact(self):
        {}
        for m in self.materials:
            for module in m.GWP:
                i = m.GWP[module] * self.area * m.get_factor()

class assembly_attributes:

    def __init__(self, fountation, structure, exterior_walls, floors, interior_walls, ceilings, windows, roofs):
        self.foundation = fountation
        self.structure = structure
        self.exterior_walls = exterior_walls
        self.floors = floors
        self.interior_walls = interior_walls
        self.ceilings = ceilings
        self.windows = windows
        self.roofs = roofs

class building_attributes:
    def __init__(self, geom, scenario = {'Climate': 'Continental', 'Period':'1'}, building_systems = [], building_type = 'Office'):
        self.geometry = geom
        self.scenario = scenario
        self.building_sys = building_systems
        self.building_type = building_type

class utilities:
    def import_materials(path):
        with open(path) as f:
            data = json.load(f)
            # materials = {}
            materials = []
            for d in data:
                mat = material.to_object(d)
                # print (mat.name)
                # materials[mat.name] = mat
                materials.append(mat)
            return materials

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  
