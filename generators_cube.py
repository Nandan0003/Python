def topcube():
    n = 1
    while n <= 10:
        cube = n*n*n
        yield cube
        n += 1
        
    
cubee = topcube()
for i in cubee:
    print(i)
    
    
def next():
    n = 0
    for i in range(0,21):
        n += 1
        yield n
nn = next()
print(nn.__next__())
