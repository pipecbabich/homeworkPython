class Transport:

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
 

   def seating_capacity(self, capacity = 50):
       return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"
   
autobus = Transport('Renaul Logan', 180, 12)
print(autobus.seating_capacity())