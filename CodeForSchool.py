n = 0
ln = []
inp = str(input("enter multiple numbers hidden within a string"))
for i in inp:
    try:
        ln.append(float(i))
    except ValueError:
        pass
for i in  ln:
    n = n + i
print("sum of all digits in the string is ", n)
