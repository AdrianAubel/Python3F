while True:
    n = input("Ingrese un numero mayor a 0 para iniciar el programa La Trifecta: ")
    if not(n.isdigit()) or int(n) <= 0:
         print(f"Finalizando...")
         break   
    
    texto = input("Ingrese una palabra o frase: ")
    caracteres = len(texto)
    print(f"{texto} contiene {caracteres} caracteres...")

    print(f"Calculando el factorial de {caracteres}...")
    factorial = 1
    for i in range(1, caracteres + 1):
        factorial*=i
    print(f"El factorial de {caracteres} es igual a {factorial}")

    print(f"Verificando si el resultado es par o impar...")
    if factorial % 2 == 0:
        print(f"{factorial} es par")
    else:
        print(f"{factorial} es impar")






    

 