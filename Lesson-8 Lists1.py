cities = ['New York', 'Moscow', 'new dahli', 'Simnferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[1])
print(cities[-1])
print(cities[-2])
print("\n----------------\n")
for city in cities:
    print(city)

print(cities)

cities[2] = 'Tula'

print(cities)

cities.append('Kursk')
cities.append('Yalta')
cities.append('Rostov')
print(cities)

cities.insert(2, 'Feodosiya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)


cities.sort(reverse=True)
print(cities)

cities.sort()
print(cities)


cities.reverse()
print(cities)

