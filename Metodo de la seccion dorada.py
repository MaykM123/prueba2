import math
import itertools
print(" Búsqueda por la sección dorada. 123")

interacciones = int(input("Introdusca la Cantidad de Interacciones: "))
xi = int(input("Introdusca Xi: "))
xu = int(input("Introdusca Xu: "))
Fxi = (2*math.sin(xi))-((xi**2)/10)
Fxu = (2*math.sin(xu))-((xu**2)/10)
R = 0.61803398875
D = xu * R
x1 = xi + D
x2 = xu - D
Fx1 = (2*math.sin(x1))-((x1**2)/10)
Fx2 = (2*math.sin(x2))-((x2**2)/10)

print("\n", "Xi: ", xi, "F(xi): ", Fxi, "x2: ", x2, "Fx2: ", Fx2, "x1: ", x1, "Fx1: ", Fx1, "Xu: ", xu, "F(xu): ", Fxu, "D: ", D, "\n" )

for _ in itertools.repeat(None, interacciones-1):

    if Fx1 > Fx2:    
        xi = x2
        Fxi = Fx2
        x2 = x1
        Fx2 = Fx1
        D = xu * R
        x1 = xi + D
        Fx1 = (2*math.sin(x1))-((x1**2)/10)
        Fx2 = (2*math.sin(x2))-((x2**2)/10)
        print("Xi: ", xi, "F(xi): ", Fxi, "x2: ", x2, "Fx2: ", Fx2, "x1: ", x1, "Fx1: ", Fx1, "Xu: ", xu, "F(xu): ", Fxu, "D: ", D, "\n" )    
    elif Fx2 > Fx1:
        xu = x1
        Fxu = Fx1
        x1 = x2
        Fx1 = Fx2
        D = xu * R
        x2 = xu - D
        Fx1 = (2*math.sin(x1))-((x1**2)/10)
        Fx2 = (2*math.sin(x2))-((x2**2)/10)
        print("Xi: ", xi, "F(xi): ", Fxi, "x2: ", x2, "Fx2: ", Fx2, "x1: ", x1, "Fx1: ", Fx1, "Xu: ", xu, "F(xu): ", Fxu, "D: ", D, "\n" )