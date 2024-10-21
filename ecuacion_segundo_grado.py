import math

n = input("Dame una ecuacion (formato: ax^2 +bx +c = 0): ").replace(" ", "")
n_split = n.split("=")
lhs = n_split[0]
rhs = n_split[1]
lhs_list = []
rhs_list = []

last_pivot = 0
#Lado izquierdo de la ecuación
for i in range(0, len(lhs)):
    if lhs[i] in ["+", "-"]: #Si el actual es + o -
        lhs_list.append(lhs[last_pivot: i])
        last_pivot = i

    if i == len(lhs)-1: #Si está al final
            lhs_list.append(lhs[last_pivot:])

for i in range(len(lhs_list)):
    lhs_list[i] = lhs_list[i].replace(" ", "")

# Lado derecho de la ecuación
last_pivot = 0
for i in range(0, len(rhs)):
    if rhs[i] in ["+", "-"]: #Si el actual es + o -
        rhs_list.append(rhs[last_pivot: i])
        last_pivot = i

    if i == len(rhs)-1: #Si está al final
            rhs_list.append(rhs[last_pivot:])

for i in range(len(rhs_list)):
    rhs_list[i] = rhs_list[i].replace(" ", "")

a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

for i in lhs_list:
    if ("x^2" in i):
        a += i.replace("x^2", "")
    elif ("x" in i):
        b += i.replace("x", "")
    else:
        c += i

for i in rhs_list:
    if ("x^2" in i):
        d += i.replace("x^2", "")
    elif ("x" in i):
        e += i.replace("x", "")
    else:
        f += i

d = float(d) if d != "" else 0
e = float(e) if e != "" else 0
f = float(f) if f != "" else 0

a = float(a) - d if a != "" else -d
b = float(b) - e if b != "" else -e
c = float(c) - f if c != "" else -f

x1 = 0
x2 = 0

if (a != 0):
    if (b*b-4*a*c < 0):
        x1 = complex(-b/(2*a), round(math.sqrt(abs(b*b-4*a*c))/(2*a), 3))
        x2 = complex(-b/(2*a), round(-math.sqrt(abs(b*b-4*a*c))/(2*a), 3))
    else:
        x1 = round((-b+math.sqrt(b*b-4*a*c))/(2*a), 3)
        x2 = round((-b-math.sqrt(b*b-4*a*c))/(2*a), 3)

    if (x1 != x2): #Si son diferentes soluciones
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        print(f"x = {x1}")
else:
    print(f"x = {-b/c}")
