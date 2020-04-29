x = 25

if x == 25:
    print("Yes you are Right")
else:
    print("You are wrong")

age = 7

if age <= 4:
    print("You are baby!")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old")


print("----END----")

print("-------------------------------------")

all_cars = ['shrudler', 'dacia', 'bmw', 'KIA', 'vw', 'feat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print('Yes Lada is in the list')
else:
    print('Ladi Not is in the list')

print("-------------------------------------")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + ' is German Car')
    else:
        print(xxxx + ' is not German Car')