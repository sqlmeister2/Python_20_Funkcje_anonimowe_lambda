
#Programowanie funkcyjne

#Wyrażenia lambda - w innych jezykach jako funkcje anonimowe

def funkcja(f, liczba):
    return f(liczba)

#funkcja kwadrat w lambdzie
#lambda jest stosowana zamiast funkcji jednolinijkowej np x*x więc można ją tak zapisać
print(funkcja(lambda x: x * x, 3))

def kwadrat(x):
    return x * x
print(kwadrat(4))

#tworzenie wyniku lambdy w zadeklarowanej zmiennej
wyn = (lambda x: x * x)(3) #w taki sposób wywołujemy funkcje lambda podając argumenty
print(wyn)

lam = lambda x: x * x
print(lam(5))

#więcej niż jeden argument
lam2 = lambda x, y: x * y
print(lam2(2,4))

print(type(lam2))