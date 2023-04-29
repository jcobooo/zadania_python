zdanie = input("Napisz jakieś zdanie: ")

x = zdanie.split()
for i in reversed(x):
    print(i)