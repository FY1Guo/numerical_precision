from num import HPNumber

a1 = 8271364783645461723467839247562345128764
b1 = 10

a2 = 187687627845278324176498743267585978
b2 = -23
N = HPNumber(a1, b1)
M = HPNumber(a2, b2)

product_reference_coefficient = a1*a2
product_reference_exponent = b1+b2
product = N*M
print("MULTIPLICATION")
print("High precision:", product.floatlike_string())
print("Float:", ((a1*10**b1)*(a2*10**b2)))
print(f"Exact computation: {product_reference_coefficient}e{product_reference_exponent}")


sum_hp = HPNumber(1, 10)
sum_float = float(1e10)
addend_hp = HPNumber(3,-10)
addend_float = 3e-10
for i in range(1000000):
    sum_hp += addend_hp
    sum_float += addend_float

print("ADDITION")
print("High precision:", sum_hp.floatlike_string())
print("Float:", sum_float)
print("Exact:", "1.000000000000003e10")


a1 = 1264612
b1 = 239
a2 = 12387632123
b2 = -4

a_product = a1*a2
b_product = b1+b2

n_hp = HPNumber(a1, b1)
m_hp = HPNumber(a2, b2)
product_hp = HPNumber(a_product, b_product)

n_float = a1*10**b1
m_float = a2*10**b2
product_float = a_product*10**b_product

print("DIVISION")
print("High precision:", n_hp == product_hp/m_hp)
print("Float:", n_float == product_float/m_float)
print("Exact: True")


