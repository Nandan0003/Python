def topcube():
    n = 1
    while n <= 10:
        cube = n*n*n
        yield cube
        n += 1
    
cubee = topcube()
for i in cubee:
    print(i)
    
    
