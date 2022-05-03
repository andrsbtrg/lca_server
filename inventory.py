from dataclasses import dataclass, field
import json
from json import JSONEncoder

# defining set of possible assemblies
ASSEMBLY_ATTRIBUTES = {
    'foundation',
    'structure',
    'exterior_walls',
    'floors',
    'interior_walls',
    'ceilings',
    'windows',
    'roofs',}
BUILDING_TYPES = {
    'office',
    'residential',
    'other'
}

@dataclass
class material:
    id: int 
    name:str
    size: float
    unit: str
    density: float
    area_weight: float
    GWP: dict
    L1: str
    L2: str
    L3: str
    L4: str

# class material:
#     def calculate_sdev(impact:dict):
#         sdev = {}
#         for key in impact:
#             sd = impact[key]**1.27
#             sdev[key] = sd
#         return sdev

#     def __init__(self, name, GWP:dict, reference_size:float, reference_unit:str):
#         self.name = name
#         self.GWP = self.convert_to_float(GWP)
#         self.size = reference_size
#         self.unit = reference_unit
        
#         # self.sdev = self.calculate_sdev()
#     def get_factor(self):
#         if self.unit == 'Kg':
#             factor = 1
        
#     def __iter__(self):
#         yield from{
#             "name":self.name,
#             "GWP": self.GWP,
#             "size": self.size,
#             "unit": self.unit
#         }.items()
#     def __str__(self):
#         return json.dumps(dict(self), ensure_ascii=False)

#     def __repr__(self):
#         return self.__str__()
    
#     def to_json(self):
#         return self.__str__()
    
#     def to_object(d):
#         inst = material(d['Name (en)'], d['GWP'], d['Reference-size'], d['Reference-unit'])
#         return inst
        
    
#     def convert_to_float(self, impact_str:dict):
#         impact_float = {}
#         for key in impact_str:
#             value_f = float(impact_str[key])
#             if (value_f != None):
#                 impact_float[key] = value_f
        
#         return impact_float


structure = { 'uid': 139.4, 'uid2': 128.1 }
@dataclass
class assembly:
    attribute_LV1: str
    attribute_LV2: str
    attribute_LV3: str
    structure: dict
    mass: float = None

    def impact(self, db):
        i = {}
        for mat_id in self.structure:
            gwp = db.iloc[mat_id]['GWP']
            # gwp = mat['GWP']
            for module in gwp:
                # print(module)
                if module in i:
                    i[module] += float(gwp[module]) * self.structure[mat_id]
                else:
                    i[module] = float(gwp[module]) * self.structure[mat_id]
        return i
        
@dataclass
class building:
        assemblies: list[assembly]
        materials: list[material]
        scenario: dict


class utils:
    def import_materials(path):
        with open(path) as f:
            data = json.load(f)
            materials = []
            for d in data:
                mat = material.to_object(d)
                materials.append(mat)
            return materials

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  
