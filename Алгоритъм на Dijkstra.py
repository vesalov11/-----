import itertools
from heapq import heappush, heappop


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list  # Списък на съседите


class Vertex:
    def __init__(self, value):
        self.value = value  # Стойността на върха

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return self.value


class Edge:
    def __init__(self, distance, vertex):
        self.distance = distance  # Разстоянието на ръба
        self.vertex = vertex  # Съседен връх


def dijkstra(graph, start, end):
    previous = {v: None for v in graph.adjacency_list.keys()}  # Предходни върхове
    visited = {v: False for v in graph.adjacency_list.keys()}  # Посетени върхове
    distances = {v: float("inf") for v in graph.adjacency_list.keys()}  # Разстояния
    distances[start] = 0  # Разстоянието до началния връх
    queue = PriorityQueue()
    queue.add_task(0, start)  # Добавяне на началния връх в опашката
    path = []

    while queue:
        removed_distance, removed = queue.pop_task()  # Извличане на върха с най-малко разстояние
        visited[removed] = True

        # Печат на текущото разстояние и текущия връх
        print(f"\nОбработваме връх: {removed}, Разстояние: {int(removed_distance)}")

        # Проверка за достигане на края
        if removed == end:
            while previous[removed]:
                path.append(removed)  # Добавяне на върха в пътя
                removed = previous[removed]
            path.append(start)
            print(f"\nНай-кратко разстояние до {end}: ", int(distances[end]))  # Преобразуване в цяло число
            print(f"Път до {end}: ", [v.value for v in path[::-1]])  # Печат на пътя
            return

        for edge in graph.adjacency_list[removed]:
            if visited[edge.vertex]:  # Пропускане на вече посетени върхове
                continue
            new_distance = removed_distance + edge.distance  # Изчисляване на новото разстояние

            # Печат на новото разстояние
            print(f"  Оценка на ръб: {removed} -> {edge.vertex}, Ново разстояние: {int(new_distance)}")

            if new_distance < distances[edge.vertex]:  # Проверка за по-кратко разстояние
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)

                # Печат на актуализираното разстояние
                print(f"  Актуализирано разстояние до {edge.vertex}: {int(new_distance)}")

    return


class PriorityQueue:
    def __init__(self):
        self.pq = []  # Списък от елементи, подредени в купчина
        self.entry_finder = {}  # Отображение на задачи към елементи
        self.counter = itertools.count()  # Уникален последователен номер

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        'Добавя нова задача или обновява приоритета на съществуваща задача'
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update_priority(self, priority, task):
        'Обновява приоритета на задача на място'
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        'Премахва и връща задачата с най-нисък приоритет. Извиква KeyError, ако е празна.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError('pop from an empty priority queue')


# Тест на алгоритъма
vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F"), Vertex("G"), Vertex("H")]
A, B, C, D, E, F, G, H = vertices

# Дефиниране на списък на съседите с цели числа
adj_list = {
    A: [Edge(2, B), Edge(1, C), Edge(4, D)],
    B: [Edge(2, A), Edge(3, E)],
    C: [Edge(1, A), Edge(3, E), Edge(4, F)],
    D: [Edge(4, A), Edge(1, F), Edge(2, G)],
    E: [Edge(3, B), Edge(2, C), Edge(5, F), Edge(2, H)],
    F: [Edge(4, C), Edge(1, D), Edge(5, E), Edge(2, G), Edge(3, H)],
    G: [Edge(2, D), Edge(3, F), Edge(4, H)],
    H: [Edge(3, E), Edge(2, F), Edge(1, G)],
}

my_graph = Graph(adj_list)

# Извикване на алгоритъма на Дейкстра
dijkstra(my_graph, start=A, end=H)
