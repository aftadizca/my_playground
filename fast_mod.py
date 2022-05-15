import time

start = time.time()
square = 373
base=23
modulus = 747
squareBin = str(format(square,"b"))

print("Calculate", base,"^",square)

i=1
result = base % modulus
print("\n")
while i<=len(squareBin)-1:
    bit = squareBin[i]
    if int(bit) == 0:
        result = (result**2) % modulus
        # print(i,"S ", bit)
    else:
        result = (result**2) % modulus
        result = (result*base) % modulus
        # print(i,"SM ", bit)
    i=i+1
end = time.time()

print("Result : ", result)
print("in ", end-start,"s")

