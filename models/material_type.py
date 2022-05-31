from enum import Enum
from typing import List
from models.material_property import MaterialProperty

#Плотность исключил в отдельный класс
class MaterialType(Enum):
    THERMAL_ISOTROPIC = (1, [2, 3])
    THERMAL_ORTHOTROPIC = (2, [3, 4, 5, 6])
    STIFFNESS_ISOTROPIC = (3, [7, 8])
    STIFFNESS_ORTHOTROPIC = (4, [9, 10, 11, 12, 13, 14, 15, 16, 17])
    DENSITY = (5, [1])

    def __init__(self, id, mat_props_ids: List[int]):
        self.id = id
        self.mat_props = mat_props_ids


