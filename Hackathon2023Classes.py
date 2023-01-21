import random 
from datetime import date, strptime
class Monitor:
    def __init__(self,longitude,latitude,curFlow,avgFlow):
        self.longitude = float(longitude)
        self.latitude= float(latitude)
        self.curFlow = float(curFlow)
        self.avgFlow = float(avgFlow)
    def update(self):
        self.pressure = random.uniform(0,20.5)
  
    
class pipe:
    def __init__(self,start,end,depth,sewage,material,instalDate):
        self.start = start
        self.end = end
        self.avgFlow = (start.avgFlow + end.avgFlow)/2
        self.depth = depth
        self.sewage = bool(sewage)
        self.curFlow = (start.curFlow + end.curFlow)/2
        self.material = material
        self.instalDate = instalDate
    def returnPipeAge(self):
        intstalDateTime = strptime(self.instalDate, "%d%m%y")
        today = date.today()
        return today.year - instalDateTime.year - ((today.month,today.day)<(intstalDateTime.month,intstalDateTime.day))




    def isLeaking(self):
        if self.curFlow - 10 < self.avgFlow:
            return True
        else:
            return False
    def ErRisk(self):
        if self.sewage:
            erRate = self.material.sewageRate
        else:
            erRate = self.material.cleanRate
        erRisk = self.returnPipeAge() * erRate
        return erRate
    def TempRisk(self):
        tempChanges = (tempChange(self.start.longitude,self.start.latitude)+tempChange(end.start.longitude,end.start.latitude)) / 2
        tempRisk = tempChanges / depth
    
    def risk(self):
        riskPoint = self.TempRisk() + self.ErRisk()



def tempChange(long,lat):
    #work out temp changes at given loc
