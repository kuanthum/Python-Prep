#14

k = 30
n = 0
prime = True
q = "s"

while q == "s":
    
    for i in range(2, n):
        if (n % i) == 0:
            prime = False
    if(prime):
        print(n)
        q = input("Presionar s para buscar el siguiente primo")
    else:
        prime = True
    n += 1
