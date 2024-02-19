#!/usr/bin/env python3

street = "15 rue bignon"
city = "Palis"
country = "Trance"

addr1 = street+"\n"+city+"\n"+country
addr2 = f"{street}\n{city}\n{country}"

print("Address - 1st way:")
print(addr1)
print()
print("Address - 2nd way:")
print(addr2)


vari = "Earth revolves around the sun"
print(vari[6:14])
print(vari[-3:])


fruitN = 2
veggieN = 4
print(f"I eat {veggieN} veggies and {fruitN} daily")


s = 'maine 200 banana khaye'
s = s[:6] + "10 samosa" + s[16:]
print(s)

s = 'maine 200 banana khaye'
s = s.replace('banana', 'samosa')
s = s.replace('200', '10')
print(s)

s = 'maine 200 banana khaye'
s = s.replace('banana', 'samosa').replace('200', '10')
print(s)
