def findPairs(paris):
    s=set()
    for (x,y) in paris:
        s.add((x,y))
        if (y,x) in s:
            print((x,y),"|",(y,x))
pairs=[(3,4),(1,2),(5,2),(7,10),(4,3),(2,5)]
findPairs(pairs)