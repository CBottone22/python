frase = input("Decime una frase y te calculo cuanto tardaria si tuvieras que decirla: ")
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras y tendrias {cantidad_de_palabras/2} segundos en decirlo')