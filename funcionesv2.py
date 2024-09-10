print("mas sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

#llamadas a funciones 
print("calculando suma ")
n1=int(input("ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
# resta
def resta_xv(x,v):
    r=x-v
    return r
print("calculando resta ")
n3=int(input("ingresa el primer numero "))
n4=int(input("ingresa el segundo numero "))
resta=resta_xv(n3,n4)
print(f"la resta de {n3} - {n4} es {resta}")

#multiplicacion
def mult_we(w,e):
    m=w*e
    return m
print("calculando multiplicacion ")
n5=int(input("ingresa el primer numero "))
n6=int(input("ingresa el segundo numero "))
multi=mult_we(n5,n6)
print(f"la multiplicacion de {n5} x {n6} es {multi}")

#division
def div_ce(c,e):
    d=c/e
    return d
print("calculando division ")
n7=int(input("ingresa el primer numero "))
n8=int(input("ingresa el segundo numero "))
div=div_ce(n7,n8)
print(f"la division de {n7} / {n8} es {div}")