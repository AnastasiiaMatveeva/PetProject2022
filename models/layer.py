from models.material import Material
class Layer:
    def __init__(self, id: int, thickness, angle, material: Material):
        self.id = id
        self.thickness = thickness
        self.angle = angle
        self.material = material