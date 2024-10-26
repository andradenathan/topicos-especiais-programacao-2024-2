# reference: https://en.wikipedia.org/wiki/Egyptian_fraction

while True:
    try:
        k = int(input())
        resultados = []

        for x in range(k + 1, 2*k + 1):
            if (k * x) % (x - k) == 0: 
                y = (k * x) // (x - k)
                resultados.append((y, x))
        
        print(len(resultados))
        
        for x, y in resultados:
            print(f"1/{k} = 1/{x} + 1/{y}")
        
    except EOFError:
        break