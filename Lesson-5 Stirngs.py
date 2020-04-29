mystring = "bla bla bla"
name = "vAsYa pupkin"

print(name.title())
print(name.upper())
print(name.lower())

print("privet stroka nomer 1\nPrivet stroka nomer 2\n\nstroka 3")
print("messages:\n\tmessage1\n\tmessage2\n\tmessage3")
print("Lover name " + name.lower())

a = " ....,dadya vasya ....."
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())
print(a.strip("."))

a = ".... dadya vasya ....."

a = a.strip(".")    # udalenie tochek
a = a.strip()       # udalenie probelov
print(a.title())