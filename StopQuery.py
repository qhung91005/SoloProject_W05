import json
import csv
from Stop import Stop

class StopQuery(Stop):
    def __init__(self,List = []):
        self.list_stop = List
        
    def process_json(json_string):
        json_parts = json_string.split('}\n{')
        json_corrected = '[' + '},{'.join(json_parts) + ']'
        return json.loads(json_corrected)

    def readListStop(self,file_name, routevar):
        with open(file_name,'r',encoding='utf-8') as file:
            json_string = file.read()
        json_data = StopQuery.process_json(json_string)
        List = []
        for item in json_data:
            tmpList = []
            for obj_dict in item['Stops']:
                List.append(obj_dict)
                tmpList.append(Stop(**obj_dict))
            for i,var in enumerate(routevar.list_routevar):
                if str(var.RouteId) == item['RouteId'] and str(var.RouteVarId) == item['RouteVarId']:
                    #if len(routevar.list_routevar[i].list_stop.list_stop) != 0:
                    #    print("Invalid")
                    routevar.list_routevar[i].list_stop = StopQuery(tmpList)
                    break
        newList = []
        appear = set()
        for item in List:
            if item['StopId'] not in appear:
                newList.append(Stop(**item))
                appear.add(item['StopId'])
        self.list_stop = newList
        
    def outputAsJson(self,file_name):
        list_dict = []
        for item in self.list_stop:
            obj = item.__dict__ 
            list_dict.append(obj)
        with open(file_name,'w', encoding = 'utf-8') as file:
            for item in list_dict:
                json_string = json.dumps(item, ensure_ascii=False)
                file.write(json_string + '\n')
    
    def outputAsCSV(self,file_name):
        list_dict = []
        for item in self.list_stop:
            obj = item.__dict__ 
            list_dict.append(obj)
        header = list(self.list_stop[0].__dict__.keys())
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in list_dict:
                writer.writerow(row)
        
    def searchBy_StopId(self, stop_id):
        matching_stops = [stop for stop in self.stops if stop.StopId == stop_id]
        return StopQuery(matching_stops)
    
    def searchBy_Code(self, code):
        matching_stops = [stop for stop in self.stops if stop.Code == code]
        return StopQuery(matching_stops)
    
    def searchBy_Name(self, name):
        matching_stops = [stop for stop in self.stops if stop.Name == name]
        return StopQuery(matching_stops)
    
    def searchBy_StopType(self, stop_type):
        matching_stops = [stop for stop in self.stops if stop.StopType == stop_type]
        return StopQuery(matching_stops)
    
    def searchBy_Zone(self, zone):
        matching_stops = [stop for stop in self.stops if stop.Zone == zone]
        return StopQuery(matching_stops)
    
    def searchBy_Ward(self, ward):
        matching_stops = [stop for stop in self.stops if stop.Ward == ward]
        return StopQuery(matching_stops)
    
    def searchBy_AddressNo(self, address_no):
        matching_stops = [stop for stop in self.stops if stop.AddressNo == address_no]
        return StopQuery(matching_stops)
    
    def searchBy_Street(self, street):
        matching_stops = [stop for stop in self.stops if stop.Street == street]
        return StopQuery(matching_stops)
    
    def searchBy_SupportDisability(self, support_disability):
        matching_stops = [stop for stop in self.stops if stop.SupportDisability == support_disability]
        return StopQuery(matching_stops)
    
    def searchBy_Status(self, status):
        matching_stops = [stop for stop in self.stops if stop.Status == status]
        return StopQuery(matching_stops)
    
    def searchBy_Lng(self, lng):
        matching_stops = [stop for stop in self.stops if stop.Lng == lng]
        return StopQuery(matching_stops)
    
    def searchBy_Lat(self, lat):
        matching_stops = [stop for stop in self.stops if stop.Lat == lat]
        return StopQuery(matching_stops)
    
    def searchBy_Search(self, search):
        matching_stops = [stop for stop in self.stops if stop.Search == search]
        return StopQuery(matching_stops)
    
    def searchBy_Routes(self, routes):
        matching_stops = [stop for stop in self.stops if routes in stop.Routes]
        return StopQuery(matching_stops)




