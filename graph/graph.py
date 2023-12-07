from queue import Queue
from pygame.surface import Surface
from pygame.font import Font
from graph.vertex import Vertex
from graph.edge import Edge
import utils.colors as colors

class Graph:
    def __init__(self) -> None:
        self.verts: dict[str, Vertex] = {
            'a': Vertex('a', pos=(200, 100)),
            'b': Vertex('b', pos=(100, 200)),
            'c': Vertex('c', pos=(200, 200)),
            'd': Vertex('d', pos=(100, 300)),
            'e': Vertex('e', pos=(200, 300)),
            'f': Vertex('f', pos=(300, 300)),
            'g': Vertex('g', pos=(100, 400)),
            'h': Vertex('h', pos=(300, 400)),
            'i': Vertex('i', pos=(300, 200)),
            'j': Vertex('j', pos=(100, 500))
        }
        self.edges: dict[str, list[Vertex]] = {
            'a': [self.verts['b'], self.verts['c'], self.verts['i']],
            'b': [self.verts['d']],
            'c': [self.verts['e'], self.verts['f']],
            'd': [self.verts['g']],
            'e': [],
            'f': [self.verts['h']],
            'g': [self.verts['h'], self.verts['j']],
            'h': [],
            'i': [self.verts['f']],
            'j': []
        }
        self.loop_timer = 0
        self._init_bfs()

    def update(self) -> None:
        self.loop_timer += 1
        if self.bfs_q.empty() or self.loop_timer < 30:
            return
        self.loop_timer = 0
        self._run_bfs_loop()

    def restart_bfs(self) -> None:
        self.loop_timer = 0
        for _, v in self.verts.items():
            v.dist = -1
            v.color = colors.RED
        self._init_bfs()

    def render(self, surf: Surface, font: Font) -> None:
        for k, v in self.edges.items():
            for vert in v:
                Edge(self.verts[k], vert).render(surf)
        for _, v in self.verts.items():
            v.render(surf, font)

    def _run_bfs_loop(self) -> None:
        self.current: Vertex = self.bfs_q.get()
        if not self.edges.get(self.current.label): return
        for v in self.edges.get(self.current.label):
            if v.dist == -1:
                self.bfs_q.put(v)
                v.dist = self.current.dist + 1
                v.color = colors.GREEN
                self.current.color = colors.BLUE

    def _init_bfs(self) -> None:
        self.bfs_q: Queue[Vertex] = Queue()
        self.bfs_q.put(self.verts['a'])
        self.bfs_q.queue[0].visit()
