# coding=utf-8

import queue

from metro import Station, Route
import data

class Router:

    def __init__(self):
        self.dist = [1000000000000] * (len(data.STATIONS)+1)

    def make_route(self, source: Station):
        self.dist[source.id_] = 0
        s = queue.PriorityQueue()
        s.put(source.id_)
        while not s.empty():
            cur = s.get()
            for e in data.graph[cur]:
                #print(cur, e)
                if self.dist[e[0]] > self.dist[cur] + e[1]:
                    self.dist[e[0]] = self.dist[cur] + e[1]
                    s.put(e[0])
        return self.dist
