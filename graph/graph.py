from math import floor
from queue import Queue
from queue import LifoQueue
from graph.vertex import Vertex
import utils.colors as colors

BFS: int = 0
DFS: int = 1

ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Graph:
    def __init__(self) -> None:
        self.verts: dict[int, Vertex] = {}
        self.edges: dict[int, list[Vertex]] = {}
        self.vert_id = 0
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
        if self.alg == BFS:
            self._init_bfs()
        elif self.alg == DFS:
            self._init_dfs()

    def get_vertices(self) -> list[Vertex]:
        return [v for _, v in self.verts.items()]

    def _start_link(self, id: int) -> None:
        self.link = self.verts[id]    

    def handle_link(self, id: int) -> None:
        if not self.link:
            self._start_link(id)
            return
        elif self.link.id != id:
            self.edges[self.link.id].append(self.verts[id])
            self.edges[id].append(self.verts[self.link.id])
        self.link = None

    def _make_label(self) -> str:
        '''
        generates a-z then aa-zz etc.
        '''
        loop = floor(len(self.verts) / len(ALPHA)) + 1
        return ''.join([ loop*ALPHA[len(self.verts) % len(ALPHA)] ])

    def add_vertex(self) -> None:
        self.verts[self.vert_id] = Vertex(self.vert_id, self._make_label())
        self.edges[self.vert_id] = []
        self.vert_id += 1

    def delete_vertex(self, id: int) -> Vertex:
        '''
        returns deleted vertex
        '''
        for _, v in self.edges.items():
            if self.verts[id] in v:
                v.remove(self.verts[id])
        d = self.verts.pop(id)
        self.edges.pop(id)
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
        if self.verts:
            first = list(self.verts.keys())[0]
            self.bfs_q.put(self.verts[first])
            self.bfs_q.queue[0].start_bfs()

    def _run_bfs_loop(self) -> None:
        if self.bfs_q.empty():
            return
        self.current: Vertex = self.bfs_q.get()
        if self.edges.get(self.current.id):
            for v in self.edges.get(self.current.id):
                if v.dist == -1:
                    self.bfs_q.put(v)
                    v.dist = self.current.dist + 1
                    v.color = colors.GREEN
        self.current.color = colors.BLUE

    def _init_dfs(self) -> None:
        self.dfs_q: LifoQueue[Vertex] = LifoQueue()
        if self.verts:
            first = list(self.verts.keys())[0]
            self.dfs_q.put(self.verts[first])
            self.dfs_q.queue[0].start_dfs()

    def _run_dfs_loop(self) -> None:
        if self.dfs_q.empty():
            return
        self.current: Vertex = self.dfs_q.get()
        if self.edges.get(self.current.id):
            for v in self.edges.get(self.current.id):
                if not v.visited:
                    self.dfs_q.put(v)
                    v.visited = True
                    v.color = colors.GREEN
        self.current.color = colors.BLUE
