from RouteVar import RouteVar
import json
import csv

class RouteVarQuery(RouteVar):
    def __init__(self,List = []):
        self.list_routevar = List
        
    def process_json(json_string):
        json_parts = json_string.split(']\n[')
        json_corrected = '[' + '],['.join(json_parts) + ']'
        return json.loads(json_corrected)

    def readListRouteVar(self,file_name):
        with open(file_name,'r',encoding='utf-8') as file:
            json_data = file.read()
        json_data = RouteVarQuery.process_json(json_data)
        list_RouteVar = []
        for route in json_data:
            for var in route:
                route = RouteVar(**var)
                list_RouteVar.append(route)
        self.list_routevar = list_RouteVar
    
    def outputAsJson(self, file_name):
        list_dict = []
        for item in self.list_routevar:
            obj = item.__dict__ 
            list_dict.append(obj)
        with open(file_name,'w', encoding = 'utf-8') as file:
            for item in list_dict:
                json_string = json.dumps(item, ensure_ascii=False)
                file.write(json_string + '\n')
    
    def outputAsCSV(self,file_name):
        list_dict = []
        for item in self.list_routevar:
            obj = item.__dict__ 
            list_dict.append(obj)
        header = list(self.list_routevar[0].__dict__.keys())
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in list_dict:
                writer.writerow(row)
        
    def searchBy_RouteId(self, route_id):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RouteId == route_id]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_RouteVarId(self, route_var_id):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RouteVarId == route_var_id]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_RouteVarName(self, route_var_name):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RouteVarName == route_var_name]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_RouteVarShortName(self, route_var_short_name):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RouteVarShortName == route_var_short_name]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_RouteNo(self, route_no):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RouteNo == route_no]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_StartStop(self, start_stop):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.StartStop == start_stop]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_EndStop(self, end_stop):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.EndStop == end_stop]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_Distance(self, distance):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.Distance == distance]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_Outbound(self, outbound):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.Outbound == outbound]
        return RouteVarQuery(filtered_route_vars)
    
    def searchBy_RunningTime(self, running_time):
        filtered_route_vars = [route_var for route_var in self.route_vars if route_var.RunningTime == running_time]
        return RouteVarQuery(filtered_route_vars)
        
    
