def cesar(message, cle):
    cache = ""
    for i in range(len(message)):
        m=ord(message[i])
        a=ord("a")
        z=ord("z")
        if(m<=z and m>=a):
            key = (m - (a-1)) + cle
            ascii = (a-1) + key%26
            cache = cache + chr(ascii)
    return cache

def decesar(message, cle):
    cache = ""
    for i in range(len(message)):
        m=ord(message[i])
        a=ord("a")
        z=ord("z")
        if(m<=z and m>=a):
            key = ((z+1) - m) + cle
            ascii = (z+1) - key%26
            cache = cache + chr(ascii)
    return cache
        
def dechiffre(message):
    trouve = "non"
    cle = 0
    while trouve == ("oui" and "non"):
        cache = ""
        cle = cle + 1
        for i in range(len(message)):
            m=ord(message[i])
            z=ord("z")
            key = (z - m) + cle
            ascii = z - key%26
            cache = cache + chr(ascii)
        print(cache)
        trouve = input('Est-ce un cohérent pour vous? oui/non: ')
    print("Voici le clés: ",cle)
