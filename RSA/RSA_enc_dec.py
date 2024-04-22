from Crypto.Util import number

e = 65537
d = 9403444398337346753
m = 6385496198122641910
c = 6385496198122641910
n = 10199657998491469147

plain = pow(m, d, n)    # M = C^d mod n
cipher = pow(c, e, n)   # C = M^e mod n

# Converte il numero esadecimale in una stringa di testo
#plaintext = bytes.fromhex(hex(M_new)[2:]).decode('utf-8')
print("plaintext: ", plain)
print("ciphertext: ", cipher)