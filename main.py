

def factroial():#This function calculate factroial

    n =int(input("Give me number:"))
    sonuc = 1
    for i in range(1 ,n+1):
        sonuc *= i

    print(sonuc)

factroial()