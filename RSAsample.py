def ExtEuclid(a, b):
    if b != 0:
        q = a // b # quotient
        r = a % b # remainder
        g, y, x = ExtEuclid(b, r)
        y = y - q*x
        return g, x, y
    else:
        return a, 1, 0
def ModInv(a, b):
    # modular inverse
    g, x, y = ExtEuclid(a, b)
    while x < 0:
        x = x + b
    return x
# RSA parameters for RSA-768
p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489

q = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917

N = p*q # public modulus
e = 65537 # 2**16 + 1 public exponent
phi = (p-1)*(q-1)
d = ModInv(e, phi) # secret(private) exponent
# Message 
M = 2**766-2**723-2**50-2**8-1
C = pow(M,e,N) # ciphertext
R = pow(C,d,N) # decrypted ciphertext
print('d=',d)
print('message=',M)
print('ciphertext=', C)
print('decrypted ciphertext=', R)