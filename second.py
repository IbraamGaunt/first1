print ('pipiskia')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a<(c/2) and a<b and a<(d-b) :
    print (a)
elif  (c-a)<b and (c-a)<(d-b) :
    print ((c-a))
elif  b<(d-b):
    print (b)
else:
    print (d-b)