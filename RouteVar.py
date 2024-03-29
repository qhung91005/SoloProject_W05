from StopQuery import StopQuery
from Path import Path
import json
import csv
import pylint

class RouteVar:
    def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, 
                 RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime):
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId
        self._RouteVarName = RouteVarName
        self._RouteVarShortName = RouteVarShortName
        self._RouteNo = RouteNo
        self._StartStop = StartStop
        self._EndStop = EndStop
        self._Distance = Distance
        self._Outbound = Outbound
        self._RunningTime = RunningTime
        self._path = Path()
        self._list_stop = StopQuery()
    
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
    def RouteVarName(self):
        return self._RouteVarName
    
    @RouteVarName.setter
    def RouteVarName(self, value):
        self._RouteVarName = value
        
    @property
    def RouteVarShortName(self):
        return self._RouteVarShortName
    
    @RouteVarShortName.setter
    def RouteVarShortName(self, value):
        self._RouteVarShortName = value
        
    @property
    def RouteNo(self):
        return self._RouteNo
    
    @RouteNo.setter
    def RouteNo(self, value):
        self._RouteNo = value
        
    @property
    def StartStop(self):
        return self._StartStop
    
    @StartStop.setter
    def StartStop(self, value):
        self._StartStop = value
        
    @property
    def EndStop(self):
        return self._EndStop
    
    @EndStop.setter
    def EndStop(self, value):
        self._EndStop = value
        
    @property
    def Distance(self):
        return self._Distance
    
    @Distance.setter
    def Distance(self, value):
        self._Distance = value
        
    @property
    def Outbound(self):
        return self._Outbound
    
    @Outbound.setter
    def Outbound(self, value):
        self._Outbound = value
        
    @property
    def RunningTime(self):
        return self._RunningTime
    
    @RunningTime.setter
    def RunningTime(self, value):
        self._RunningTime = value

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self,value):
        self._path = value
        
    @property
    def list_stop(self):
        return self._list_stop
    
    @list_stop.setter
    def list_stop(self,value):
        self._list_stop = value
        
    


