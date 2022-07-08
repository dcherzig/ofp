#%%
class SensorID:
    pass

class Central:
    class _SensorData: #internal use for a class or attribute
        def __init__(self): #constructor
            self.cur, self.min, self.max, self.avg= None, None, None, None
            self.n = 0
            self.__displays = [] #double underscores for attributes that shouldn't be inherited, only accessible

        def add_measurement(self, x:float): #why only x and not cur, min, max, n as input? -> was already initializied in __init__!
            if self.n > 0:
                self.cur, self.min, self.max = x, min(self.min,x), max(self.max,x)
                self.n +=1
                self.avg = self.avg + (x-self.avg)/self.n
            else:
                self.cur, self.min, self.max, self.n = x, x, x, 1
                for d in self.__displays: #to show which displays should show the new values
                    d.update() #update list

        def add_display(self, display:float): #adds new display in list
            if display not in self.__displays:
                self.__displays.append(display)
                
    def __init__(self): #initializing the dictionary
        self.__sensor_dict: {SensorID: Central._SensorData} = dict() #internal dictionary

    def add_measurement(self, sensor_id, x:float):
        try:
            sd = self.__sensor_dict[sensor_id] #what happens here?
        except KeyError: #if no datas are available
            sd = Central._SensorData() #Daten in dictionary einlesen
            self.__sensor_dict[sensor_id]=sd
        sd.add_measurement(x) #Daten in dictionary einbinden

    def add_display(self, sensor_id:float, display:float):
        try:
            sd = self.__sensor_dict[sensor_id]
        except KeyError:
            sd = Central._SensorData()
            self.__sensor_dict[sensor_id]=sd
        sd.add_display(display)

    def get_min(self, sensor_id):
        return self.__sensor_dict[sensor_id].min

    def get_max(self, sensor_id):
        return self.__sensor_dict[sensor_id].max

    def get_avg(self, sensor_id):
        return self.__sensor_dict[sensor_id].avg
    
    def get_cur(self, sensor_id):
        return self.__sensor_dict[sensor_id].cur

    



#%%
class SensorID:
    pass

#%%
class Display:
    def update(self):
        pass