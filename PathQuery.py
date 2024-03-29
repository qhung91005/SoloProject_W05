from Path import Path

import json
import csv

class PathQuery(Path):
    def __init__(self, List = []):
        self.list_path = List
        
    def process_json(json_string):
        json_parts = json_string.split('}\n{')
        json_corrected = '[' + '},{'.join(json_parts) + ']'
        return json.loads(json_corrected)

    def readListPath(self,file_name, routevar):
        with open(file_name,'r',encoding='utf-8') as file:
            json_string = file.read()
        json_data = PathQuery.process_json(json_string)
        List = []
        for item in json_data:
            obj = Path(item['lat'],item['lng'],item['RouteId'],item['RouteVarId'])
            List.append(obj)
            for i,var in enumerate(routevar.list_routevar):
                if str(var.RouteId) == item['RouteId'] and str(var.RouteVarId) == item['RouteVarId']:
                    #if len(routevar.list_routevar[i].list_stop.list_stop) != 0:
                    #    print("Invalid")
                    routevar.list_routevar[i].path = obj
                    break
        self.list_path = List
        
    def outputAsJson(self,file_name):
        list_dict = []
        for item in self.list_path:
            obj = item.__dict__ 
            list_dict.append(obj)
        with open(file_name,'w', encoding = 'utf-8') as file:
            for item in list_dict:
                json_string = json.dumps(item, ensure_ascii=False)
                file.write(json_string + '\n')
    
    def outputAsCSV(self,file_name):
        list_dict = []
        for item in self.list_path:
            obj = item.__dict__ 
            list_dict.append(obj)
        header = list(self.list_path[0].__dict__.keys())
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in list_dict:
                writer.writerow(row)




