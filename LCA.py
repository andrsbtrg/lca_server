import numpy as np
from inventory import assembly, material 


def calculate_impact(material:material, quantity, impact = ''):
    """
    Returns {'A1-A3': 'i', 'B1': j ...}
    
    Args:
        material (material): _description_
        quantity (_type_): _description_
        impact (str, optional): _description_. Defaults to ''.

    Returns:
        _type_: _description_
    """
    impacts = {}
    # for now only calculate GWP

    # stages are 'A1', 'A2' ... 'B7'
    for stage in material.GWP:
        impacts[stage] = material.GWP[stage] * quantity
    return impacts

def simulate(assembly:assembly, n):
    n = 100
    results = {}

    return results

def life_cycle_asessment(assemblies):
    results = []
    for assembly in assemblies:
        # chooses a random material from the assembly
        material = np.random.choice(assembly.materials)
        # calculates from that assembly and saves
        partial = calculate_impact(material, assembly.quantity)
        results.append(partial)
    # add results by module
    lca = {}
    for d in results:
        for module in d:
            lca[module] += d[module]
    
    return lca
