from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
from Graph import Graph

ListRouteVar = RouteVarQuery()
ListRouteVar.readListRouteVar('vars.json')
ListStop = StopQuery()
ListStop.readListStop('stops.json',ListRouteVar)
ListPath = PathQuery()
ListPath.readListPath('paths.json',ListRouteVar)

busMap = Graph()
busMap.buildGraph(ListRouteVar,ListStop)
busMap.all_pair_shortest()
#busMap.outputAllPairShortest('allpair.txt')
busMap.outputCriticalVertices('critical.json')
