from car import car


car1=car("Toyota",2020,"Red",True)
car2=car("Honda",2018,"Blue",False)

print(car1.model)
print(car1.year)
print(car1.colour)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

car1.drive()
