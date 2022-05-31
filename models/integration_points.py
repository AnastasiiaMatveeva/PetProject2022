from enum import Enum
import numpy as np

class IntegrationPoints(Enum):
    LinearReducedTriangle = (1, ([1/3, 1/3, 1/3])) #array for integration points in triangle coordinates
    LinearReducedQuad = (2, [0, 0]) #array for integration points in local coordinates
    LinearFullTriangle = (3, ([0.6, 0.2, 0.2],
      [0.2, 0.6, 0.2],
      [0.2, 0.2, 0.6]))
    LinearFullQuad = (4, ([-1/np.sqrt(3), 1/np.sqrt(3)],
      [1/np.sqrt(3), 1/np.sqrt(3)],
      [1/np.sqrt(3), -1/np.sqrt(3)],
      [-1/np.sqrt(3), -1/np.sqrt(3)]))

    def __init__(self, id, lcoords):
        self.id = id
        self.lcoords = lcoords  # local coords massiv
