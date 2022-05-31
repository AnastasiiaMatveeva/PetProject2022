from typing import List,Dict

from models.element import Element
from models.node import Node


class Mesh:
    def __init__(self, nodes: Dict[int, Node], elements: Dict[int, Element],node_elems: Dict[Node, List[Element]], node_ids: Dict[Node,int]):
        self.nodes = nodes
        self.elements = elements
        self.node_elems = node_elems
        self.node_ids = node_ids
