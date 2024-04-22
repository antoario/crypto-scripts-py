import sympy

p = 2637508411
q = 3867156577
e = 65537
phi_n = (p - 1) * (q - 1)

# Calculate the modular multiplicative inverse of e modulo phi(n)
d = sympy.mod_inverse(e, phi_n)
print("Private exponent d: ", d)
