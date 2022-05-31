from enum import Enum
#import numpy as np
from models.integration_points import IntegrationPoints

class TaskType(Enum):
    THERMAL= (1,1)
    STRUCTURAL= (2,6)
    MODAL= (3,6)


class ElementType(Enum):
    TS3R = (1,TaskType.THERMAL,3,IntegrationPoints.LinearReducedTriangle) # thermal linear triangles (reduced)
    TS4R = (2,TaskType.THERMAL,4,IntegrationPoints.LinearReducedQuad) # thermal linear quads (reduced)
    SS3R = (3, TaskType.STRUCTURAL, 3, IntegrationPoints.LinearReducedTriangle)  # thermal linear triangles (reduced)
    SS4R = (4, TaskType.STRUCTURAL, 4, IntegrationPoints.LinearReducedQuad)  # thermal linear quads (reduced)

    def __init__(self, id, task_type: TaskType, n_nodes, int_points: IntegrationPoints):
        self.id = id
        self.task_type = task_type
        self.n_nodes = n_nodes  # number of degrees of freedom
        self.int_points = int_points  # integration points coordinates

