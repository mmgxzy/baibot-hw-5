class Appliance: 
    def turn_on(self): 
        pass 
    def turn_off(self): 
        pass 
    def use(self): 
        pass 
    def repair(self): 
        pass 
 
class WashingMachine(Appliance): 
    def turn_on(self): 
        return "Стиральная машина включена" 
    def use(self): 
        return "Стиральная машина начала стирку." 
    def turn_off(self): 
        return "Стиральная машина выключена" 
    def repair(self): 
        return "Стиральная машина ремонтируется" 
 
class Microwave(Appliance): 
    def turn_on(self): 
        return "Микроволновка включен" 
    def use(self): 
        return "Микроволновка разогревает еду" 
    def turn_off(self): 
        return "Микроволновка выключен" 
    def repair(self): 
        return "Микроволновка ремонтируется" 
 
class Refrigerator(Appliance): 
    def turn_on(self): 
        return "Холодильник включен" 
    def use(self): 
        return "Холодильник охлаждает продукты" 
    def turn_off(self): 
        return "Холодильник выключен" 
    def repair(self): 
        return "Холодильник ремонтируется" 
 
washingMachine = WashingMachine() 
print(washingMachine.turn_on()) 
print(washingMachine.use()) 
print(washingMachine.turn_off()) 
print(washingMachine.repair()) 
microwave = Microwave() 
print(microwave.turn_on()) 
print(microwave.use()) 
print(microwave.turn_off()) 
print(microwave.repair()) 
refrigerator = Refrigerator() 
print(refrigerator.turn_on()) 
print(refrigerator.use()) 
print(refrigerator.turn_off()) 
print(refrigerator.repair())