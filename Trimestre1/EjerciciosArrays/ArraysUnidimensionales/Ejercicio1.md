Ejercicio 1:

**1.- Muestra el valor del elemento 6 de un array f.**

    print(f[6])

**2.- Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.**

    f = [8] * 5

**3.- Total de los 100 elementos de punto-flotante de un array c.**
    
c = [float(n) for n in range(1,100)]
c = [random.randint(1,10) for _ in range(10)    ]
print(sum(c))

**4.- Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.**
    
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [int(n) for n in range(0, 35)]
b = b + a
print(b)


**5.-Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante.**

