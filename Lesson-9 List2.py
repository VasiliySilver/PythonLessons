#         0      2     3        4        5
cars = ['bmw', 'vw', 'feat', 'skoda', 'lada']

for car in cars:
    print(car.upper())

print("-----------------------------------")

for x in range(1,6):
    print(x)

print("-----------------------------------")

mynumber_list = list(range(0,10))
print(mynumber_list)

print("-----------------------------------")

for x in mynumber_list:
    x = x * 2
    print(x)

print("-----------------------------------")
print(mynumber_list)
mynumber_list.sort(reverse=True)
print(mynumber_list)

print("-----------------------------------")

print("Max number is: " + str(max(mynumber_list)))
print("Max number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))

print("-----------------------------------")

#         0      2     3        4        5
cars = ['bmw', 'vw', 'feat', 'skoda', 'lada']

my_cars = cars[1:4]
print(my_cars)

my_cars = cars[:4]
print(my_cars)

my_cars = cars[-2:]
print(my_cars)

print("-----------------------------------")

#         0      2     3        4        5
cars = ['bmw', 'vw', 'feat', 'skoda', 'lada']
my_cars = cars[:]

