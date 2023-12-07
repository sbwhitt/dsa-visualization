from queue import Queue
from pygame.surface import Surface
from pygame.font import Font
from graph.vertex import Vertex
from graph.edge import Edge
import utils.colors as colors

class Graph:
    def __init__(self) -> None:
        self.verts = {
            'a': Vertex('a', pos=(100, 100)),
            'b': Vertex('b', pos=(100, 200)),
            'c': Vertex('c', pos=(200, 150))
        }
        self.edges: dict[str, list[Vertex]] = {
            'a': [self.verts['b'], self.verts['c']],
            'b': [],
            'c': []
        }
        self._init_bfs()

    def update_bfs(self) -> list[int]:
        if self.bfs_q.empty(): self.bfs_done = True
        self.current: Vertex = self.bfs_q.get()
        if not self.edges.get(self.current.label): return
        for v in self.edges.get(self.current.label):
            if v.dist == -1:
                self.bfs_q.put(v)
                v.dist = self.current.dist + 1
                v.color = colors.GREEN

    def render(self, surf: Surface, font: Font) -> None:
        for k, v in self.edges.items():
            for vert in v:
                Edge(self.verts[k], vert).render(surf)
        for _, v in self.verts.items():
            v.render(surf, font)

    def _init_bfs(self) -> None:
        self.current = self.verts['a']
        self.current.dist = 0
        self.current.color = colors.GREEN
        self.bfs_q = Queue()
        self.bfs_q.put(self.current)
        self.bfs_done = False
