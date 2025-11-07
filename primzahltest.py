from tqdm import tqdm
def primecheck(num):
    i = 2
    for i in tqdm(range(2, num)):
        if i == num:
            return("Primzahl.")
            break
        if num % i == 0:
            return("Keine Primzahl. Teilbar durch", i)
            break
        i += 1
    else:
        return("Was solln dat jetze?")
input = int(input("Zahl: "))
print(primecheck(input))