from queue import Queue
from queue import LifoQueue
from graph.vertex import Vertex
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
            'j': Vertex('j', pos=(100, 500)),
            'k': Vertex('k', pos=(400, 300)),
            'l': Vertex('l', pos=(400, 400)),
            'm': Vertex('m', pos=(400, 500))
        }
        self.edges: dict[str, list[Vertex]] = {
            'a': [self.verts['b'], self.verts['c'], self.verts['i']],
            'b': [self.verts['d']],
            'c': [self.verts['e']],
            'd': [self.verts['g']],
            'e': [self.verts['d'], self.verts['h']],
            'f': [],
            'g': [self.verts['j']],
            'h': [self.verts['m']],
            'i': [self.verts['e'], self.verts['f'], self.verts['k']],
            'j': [],
            'k': [self.verts['l']],
            'l': [],
            'm': []
        }
        self.alg: int = BFS
        self.start_alg()
        self.link: Vertex = None

    def update(self) -> None:
        if not self._update_timer():
            return
        if self.alg == BFS:
            self._run_bfs_loop()
        elif self.alg == DFS:
            self._run_dfs_loop()
        self.loop_timer = 0

    def set_bfs(self) -> None:
        self.alg = BFS
        self.start_alg()

    def set_dfs(self) -> None:
        self.alg = DFS
        self.start_alg()

    def start_alg(self) -> None:
        self._reset()
        if self.alg == BFS and self.verts:
            self._init_bfs()
        elif self.alg == DFS and self.verts:
            self._init_dfs()

    def get_vertices(self) -> list[Vertex]:
        return [v for _, v in self.verts.items()]

    def handle_link(self, label: str) -> None:
        if not self.link:
            self._start_link(label)
            return
        elif self.link.label != label:
            self.edges[self.link.label].append(self.verts[label])
            self.edges[label].append(self.verts[self.link.label])
        self.link = None

    def _start_link(self, label: str) -> None:
        self.link = self.verts[label]

    def delete_vertex(self, label: str) -> Vertex:
        '''
        returns deleted vertex
        '''
        for _, v in self.edges.items():
            if self.verts[label] in v:
                v.remove(self.verts[label])
        d = self.verts.pop(label)
        self.edges.pop(label)
        self.start_alg()
        return d

    def _reset(self) -> None:
        self.loop_timer = 0
        for _, v in self.verts.items():
            v.dist = -1
            v.visited = False
            v.color = colors.RED

    def _update_timer(self) -> bool:
        self.loop_timer += 1
        return self.loop_timer > 30

    def _init_bfs(self) -> None:
        self.bfs_q: Queue[Vertex] = Queue()
        first = list(self.verts.keys())[0]
        self.bfs_q.put(self.verts[first])
        self.bfs_q.queue[0].start_bfs()

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
        self.dfs_q: LifoQueue[Vertex] = LifoQueue()
        first = list(self.verts.keys())[0]
        self.dfs_q.put(self.verts[first])
        self.dfs_q.queue[0].start_dfs()

    def _run_dfs_loop(self) -> None:
        if self.dfs_q.empty():
            return
        self.current: Vertex = self.dfs_q.get()
        if self.edges.get(self.current.label):
            for v in self.edges.get(self.current.label):
                if not v.visited:
                    self.dfs_q.put(v)
                    v.visited = True
                    v.color = colors.GREEN
        self.current.color = colors.BLUE
