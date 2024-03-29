import rtree
import pyproj

class Path:
    transformer = pyproj.Transformer.from_crs('EPSG:4326','EPSG:3405',always_xy = True)
    
    def __init__(self, list_lat = [], list_lng = [], RouteId = -1, RouteVarId = -1):
        self._list_x = []
        self._list_y = []
        self._list_lat = list_lat
        self._list_lng = list_lng
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId
        self._update_list_xy()
        
    @property
    def list_lat(self):
        return self._list_lat

    @list_lat.setter
    def list_lat(self, value):
        self._list_lat = value
        self._update_list_xy()
        
    @property
    def list_lng(self):
        return self._list_lng

    @list_lng.setter
    def list_lng(self, value):
        self._list_lng = value
        self._update_list_xy()
        
    @property
    def RouteId(self):
        return self._RouteId

    @RouteId.setter
    def RouteId(self, value):
        self._RouteId = value

    @property
    def RouteVarId(self):
        return self._RouteVarId

    @RouteVarId.setter
    def RouteVarId(self, value):
        self._RouteVarId = value
        
    @property
    def list_x(self):
        return self._list_x

    @list_x.setter
    def list_x(self, value):
        self._list_x = value

    @property
    def list_y(self):
        return self._list_y

    @list_y.setter
    def list_y(self, value):
        self._list_y = value


    def _update_list_xy(self):
        self._list_x = []
        self._list_y = []
        for i in range(len(self.list_lat)):
            x,y = Path.transformer.transform(self.list_lng[i],self.list_lat[i])
            self._list_x.append(x)
            self._list_y.append(y)



