a= int(input())
b= int(input())
if a>b:
    for i in range(b, a + 1):
        a = a - 1
        print(a + 1)
else:
    for i in range(a, b + 1):
        a = a + 1
        print(a - 1)
