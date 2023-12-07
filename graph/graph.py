from queue import Queue
from pygame.surface import Surface
from pygame.font import Font
from graph.vertex import Vertex
from graph.edge import Edge
import utils.colors as colors

BFS: int = 0
DFS: int = 1

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
        self.alg = BFS
        self.start_alg()

    def update(self) -> None:
        if not self._update_timer():
            return
        if self.alg == BFS:
            self._run_bfs_loop()
        elif self.alg == DFS:
            pass
        self.loop_timer = 0

    def set_bfs(self) -> None:
        self.alg = BFS
        self.start_alg()

    def set_dfs(self) -> None:
        self.alg = DFS
        self.start_alg()

    def start_alg(self) -> None:
        self._reset()
        if self.alg == BFS:
            self._init_bfs()
        elif self.alg == DFS:
            self._init_dfs()

    def render(self, surf: Surface, font: Font) -> None:
        for k, v in self.edges.items():
            for vert in v:
                Edge(self.verts[k], vert).render(surf)
        for _, v in self.verts.items():
            v.render(surf, font)

    def _reset(self) -> None:
        self.loop_timer = 0
        for _, v in self.verts.items():
            v.dist = -1
            v.color = colors.RED

    def _update_timer(self) -> bool:
        self.loop_timer += 1
        return self.loop_timer > 30

    def _init_bfs(self) -> None:
        self.bfs_q: Queue[Vertex] = Queue()
        self.bfs_q.put(self.verts['a'])
        self.bfs_q.queue[0].visit()

    def _run_bfs_loop(self) -> None:
        if self.bfs_q.empty():
            return
        self.current: Vertex = self.bfs_q.get()
        if self.edges.get(self.current.label):
            for v in self.edges.get(self.current.label):
                if v.dist == -1:
                    self.bfs_q.put(v)
                    v.dist = self.current.dist + 1
                    v.color = colors.GREEN
        self.current.color = colors.BLUE

    def _init_dfs(self) -> None:
        pass

    def _run_dfs_loop(self) -> None:
        pass
