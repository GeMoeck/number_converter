# dez=float(input("Bitte zu konvertierende Zahl eingeben. "))
# base = int(input("Bitte Basis eingeben (2, 8, 10, 16): "))
import time

def converter(dez, base):
    converted = ""
    if base <= 10:
        while dez > 0:
            converted += str(dez % base)
            dez //= base
    elif base > 10:
        while dez > 0:
            temp = ""
            temp += str(dez % base)
            if int(temp) < 10:
                converted += temp
            elif int(temp) == 10:
                converted += "A"
            elif int(temp) == 11:
                converted += "B"
            elif int(temp) == 12:
                converted += "C"
            elif int(temp) == 13:
                converted += "D"
            elif int(temp) == 14:
                converted += "E"
            elif int(temp) == 15:
                converted += "F"
            dez //= base
    return converted[::-1]

print(converter(10, 16))



# start = time.time()
# converter(200, 2)
# end = time.time() - start
# print(end)

# start = time.time()
# bin(200)
# end = time.time() - start
# print(end)

# print(bin(200))
