n = 5

while n>0:
    print(n, end=' ')
    n-=1
print()

def display(n):
    if n==0:
        return
    print(n, end=' ')
    display(n-1) #rec call
    print(n, end=' ')


display(5) #fn call