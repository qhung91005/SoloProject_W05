
from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
import shapely
import rtree
import heapq
import json

class Edge:
    def __init__(self, destination, distance, time):
        self.destination = destination
        self.distance = distance
        self.time = time

class Graph:
    def __init__(self, list_vertice = [], list_edge = []):
        self.list_vertice = list_vertice
        MAX = 0
        for item in self.list_vertice:
            MAX = max(MAX,item.StopId)
        self.num_vertices = MAX + 1
        self.adj_list = [[] for _ in range(self.num_vertices)]
        self.distances = [[] for _ in range(self.num_vertices)]
        self.crit_cnt = [[0,i] for i in range(self.num_vertices)]
        for name in list_vertice:
            self.adj_list[name].append([])
        
    def add_edge(self, source, destination, distance, time):
        edge = Edge(destination, distance, time)
        self.adj_list[source].append(edge)
    
    def buildVertice(self, stops):
        self.list_vertice = list(stop for stop in stops.list_stop)
        MAX = 0
        for item in self.list_vertice:
            MAX = max(MAX,item.StopId)
        self.num_vertices = MAX + 1
        self.crit_cnt = [0 for _ in range(self.num_vertices)]
        self.adj_list = [[] for _ in range(self.num_vertices + 1)]
        self.distances = [[] for _ in range(self.num_vertices + 1)]
        
       

    def buildEdge(self, routevars):
        for var in routevars.list_routevar:
            velocity = var.Distance/(60*var.RunningTime)
            Index = rtree.index.Index()
            Points = []
            # for i in range(len(var.path.list_x)):
            #     x = var.path.list_x[i]
            #     y = var.path.list_y[i]
            #     Index.insert(i,(x,y,x,y))
            #     Points.append(shapely.Point(x,y))
            
            for i in range(1,len(var.list_stop.list_stop)):
                stop1 = var.list_stop.list_stop[i-1]
                stop2 = var.list_stop.list_stop[i]
                x1 = stop1.coor_x
                y1 = stop1.coor_y
                x2 = stop2.coor_x
                y2 = stop2.coor_y
                dis = shapely.distance(shapely.Point(x1,y1),shapely.Point(x2,y2))
                self.add_edge(stop1.StopId,stop2.StopId,dis,dis/velocity)
                
    def Dijsktra(self, start):
        # Initialize distances to all nodes as infinity except the start node
        distances = list(10000000000 for _ in range(len(self.adj_list)))
        distances[start] = 0
    
        # Priority queue to store nodes to visit next
        pq = [(0, start)]
    
        while pq:
            # Get the node with the smallest distance from the start
            current_distance, current_node = heapq.heappop(pq)
        
            # Visit the node if not visited yet
            if current_distance > distances[current_node]:
                continue
            self.crit_cnt[current_node] += 1
            # Update distances to neighbors
            for item in self.adj_list[current_node]:
                neighbor = item.destination
                time = item.time
                distance = current_distance + time
                # If the new distance is shorter, update the distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Add the neighbor to the priority queue
                    heapq.heappush(pq, (distance, neighbor))
    
        return distances

    def shortest_path(self,start,stop):
        distances = self.Dijsktra(start)
        return distances[stop]
    
    def all_pair_shortest(self):
        for i in range(self.num_vertices):
            if len(self.adj_list[i]) == 0:
                continue
            arr = self.Dijsktra(i)
            self.distances[i] = arr

    def buildGraph(self, routevars, stops):
        self.buildVertice(stops)
        self.buildEdge(routevars)
        
    def outputAllPairShortest(self,file_name):
        with open(file_name,'w') as file:
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if len(self.adj_list[i]) == 0 or len(self.adj_list[j]) == 0:
                        continue
                    file.write(str(i) + ' ' + str(j) + ' ' +  str(self.distances[i][j]) + '\n')

    def outputShortestPath(self,file_name,start,stop):
        pass
    
    def outputCriticalVertices(self,file_name):
        cnt = []
        for item in self.list_vertice:        
            cnt.append([self.crit_cnt[item.StopId],item.StopId])
        cnt.sort(key=lambda x: x[0],reverse = True)
        ListPrint = []
        for i in range(10):
            StopId = cnt[i][1]
            print(cnt[i][0])
            for stop in self.list_vertice:
                if StopId == stop.StopId:
                    obj = {"StopId": stop.StopId, "Code": stop.Code, "Lat": stop.Lat,
                           "Lng": stop.Lng, "Name": stop.Name}
                    ListPrint.append(obj)
        with open(file_name,'w', encoding = 'utf-8') as file:
            for item in ListPrint:
                json_string = json.dumps(item, ensure_ascii=False)
                file.write(json_string + '\n')
        