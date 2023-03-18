n = int(input("n: "))
x, y = 1, 1
fib = []
for i in range(n):
    fib.append(x)
    x, y = y, x+y
print(fib)
