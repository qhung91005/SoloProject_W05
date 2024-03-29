import pyproj

class Stop:
    transformer = pyproj.Transformer.from_crs('EPSG:4326','EPSG:3405',always_xy = True)

    def __init__(self, StopId, Code, Name, StopType, Zone, Ward, AddressNo, Street, SupportDisability, Status, Lng, Lat, Search, Routes):
        self._coor_x = -1
        self._coor_y = -1
        self._StopId = StopId
        self._Code = Code
        self._Name = Name
        self._StopType = StopType
        self._Zone = Zone
        self._Ward = Ward
        self._AddressNo = AddressNo
        self._Street = Street
        self._SupportDisability = SupportDisability
        self._Status = Status
        self._Lng = Lng
        self._Lat = Lat
        self._Search = Search
        self._Routes = Routes
        self._update_xy()        

    @property
    def StopId(self):
        return self._StopId
    
    @StopId.setter
    def StopId(self, value):
        self._StopId = value
        
    @property
    def Code(self):
        return self._Code
    
    @Code.setter
    def Code(self, value):
        self._Code = value
        
    @property
    def Name(self):
        return self._Name
    
    @Name.setter
    def Name(self, value):
        self._Name = value
        
    @property
    def StopType(self):
        return self._StopType
    
    @StopType.setter
    def StopType(self, value):
        self._StopType = value
        
    @property
    def Zone(self):
        return self._Zone
    
    @Zone.setter
    def Zone(self, value):
        self._Zone = value
        
    @property
    def Ward(self):
        return self._Ward
    
    @Ward.setter
    def Ward(self, value):
        self._Ward = value
        
    @property
    def AddressNo(self):
        return self._AddressNo
    
    @AddressNo.setter
    def AddressNo(self, value):
        self._AddressNo = value
        
    @property
    def Street(self):
        return self._Street
    
    @Street.setter
    def Street(self, value):
        self._Street = value
        
    @property
    def SupportDisability(self):
        return self._SupportDisability
    
    @SupportDisability.setter
    def SupportDisability(self, value):
        self._SupportDisability = value
        
    @property
    def Status(self):
        return self._Status
    
    @Status.setter
    def Status(self, value):
        self._Status = value
        
    @property
    def Lng(self):
        return self._Lng
    
    @Lng.setter
    def Lng(self, value):
        self._Lng = value
        self._update_xy()
        
    @property
    def Lat(self):
        return self._Lat
    
    @Lat.setter
    def Lat(self, value):
        self._Lat = value
        self._update_xy()
        
    @property
    def Search(self):
        return self._Search
    
    @Search.setter
    def Search(self, value):
        self._Search = value
        
    @property
    def Routes(self):
        return self._Routes
    
    @Routes.setter
    def Routes(self, value):
        self._Routes = value
    
    @property
    def coor_x(self):
        return self._coor_x

    @coor_x.setter
    def coor_x(self, value):
        self._coor_x = value

    @property
    def coor_y(self):
        return self._coor_y

    @coor_y.setter
    def y(self, value):
        self._coor_y = value

    def _update_xy(self):
        x,y = Stop.transformer.transform(self._Lng,self._Lat)
        self._coor_x = x 
        self._coor_y = y 