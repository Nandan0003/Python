names  = ["a","e","i","o","u"]

new = iter(names)

for i in names:
    print(new.__next__())