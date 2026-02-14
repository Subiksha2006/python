def add(a, b):
return a + b
def sub(c, d):
return c - d
def mul(e, f):
return e * f
def div(g, h):
return g / h

print(&quot;============================&quot;)
print(&quot;1. TO PERFORM ADDITION&quot;)
print(&quot;2. TO PERFORM SUBTRACTION&quot;)
print(&quot;3. TO PERFORM MULTIPLICATION&quot;)
print(&quot;4. TO PERFORM DIVISION&quot;)
print(&quot;5. EXIT&quot;)
print(&quot;============================&quot;)
while True:
choice = int(input(&quot;Enter your choice: &quot;))
if choice == 1:
a = int(input(&quot;Enter the 1st value: &quot;))
b = int(input(&quot;Enter the 2nd value: &quot;))
print(add(a, b))
elif choice == 2:
c = int(input(&quot;Enter the 1st value: &quot;))
d = int(input(&quot;Enter the 2nd value: &quot;))
print(sub(c, d))
elif choice == 3:
e = int(input(&quot;Enter the 1st value: &quot;))
f = int(input(&quot;Enter the 2nd value: &quot;))
print(mul(e, f))
elif choice == 4:
g = int(input(&quot;Enter the 1st value: &quot;))
h = int(input(&quot;Enter the 2nd value: &quot;))
print(div(g, h))
elif choice == 5:
print(&quot;Exited&quot;)
break
else:
print(&quot;Wrong choice&quot;)
