# DES(Data Encryption Standard)
# usage:
# encryption(plaintext, key)
# Both the plaintext and the key are 64 bits
# This program does not care parity bits of key

# Initial Permutation
IP = [58, 50, 42, 34, 26, 18, 10, 2,      
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Inverse Initial Permutation
IPinv = [40, 8, 48, 16, 56, 24, 64, 32,     
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41,  9, 49, 17, 57, 25]

# Expansion Permutation
E = [32, 1, 2, 3, 4, 5,            
      4, 5, 6, 7, 8, 9,
      8, 9,10,11,12,13,
     12,13,14,15,16,17,
     16,17,18,19,20,21,
     20,21,22,23,24,25,
     24,25,26,27,28,29,
     28,29,30,31,32, 1]
                  
# S boxes
S = [ # S1
     [[14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7],             
      [ 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8],
      [ 4, 1,14 ,8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0],
      [15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13]],
      # S2 
     [[15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10],
      [ 3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5],
      [ 0,14, 7,11,10, 4,13, 1, 5, 8,12, 6, 9, 3, 2,15],
      [13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9]],
      # S3
     [[10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1],
      [13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7],
      [ 1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12]],
      # S4      
     [[ 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15],
      [13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9],
      [10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4],
      [ 3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14]],
      # S5   
     [[ 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9],
      [14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6],
      [ 4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14],
      [11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3]],
      # S6  
     [[12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11],
      [10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8],
      [ 9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6],
      [ 4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13]],
      # S7  
     [[ 4,11, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1],
      [13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6],
      [ 1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2],
      [ 6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12]],
      # S8
     [[13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7],
      [ 1,15,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2],
      [ 7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8],
      [ 2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11]]]
    
# Permutation in F-function       
P = [16, 7,20,21,29,12,28,17,     
     1,15,23,26, 5,18,31,10,
     2, 8,24,14,32,27, 3, 9,
    19,13,30, 6,22,11, 4,25]

# for key-schedule
# Permuted Choice 1
PC1 = [57,49,41,33,25,17, 9,              
        1,58,50,42,34,26,18,
       10, 2,59,51,43,35,27,
       19,11, 3,60,52,44,36,
       63,55,47,39,31,23,15,             
        7,62,54,46,38,30,22,
       14, 6,61,53,45,37,29,
       21,13, 5,28,20,12, 4]
# Permuted Choice 2
PC2 = [14,17,11,24, 1, 5,                 
        3,28,15, 6,21,10,
       23,19,12, 4,26, 8,
       16, 7,27,20,13, 2,
       41,52,31,37,47,55,
       30,40,51,45,33,48,
       44,49,39,56,34,53,
       46,42,50,36,29,32]

# number of full round = number of subkeys 
fullround = 16  

# key schedule function
# input: 64 bit key
# output: the list of subkeys           
def keyschedule(key):
    # Table of left shifts (number of bits to rotate) 
    sft = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    int_key = 0
    base64bit = 1 << 64 # 2**64
    # PC1(key) 
    for i in range(len(PC1)):
        pos = base64bit >> PC1[i]
        int_key = int_key | (((key & pos) << (PC1[i]-1))>>(i+8))

    MASK28 = 0xFFFFFFF # for 28bit mask   
    LKey = int_key >> 28 # left key
    RKey = int_key & MASK28 # right key
        
    subkeys = []
    for i in range(fullround):
        C0 = (LKey << sft[i]) & MASK28
        C1 = LKey >> (28 - sft[i])
        LKey = C0 | C1
        D0 = (RKey << sft[i]) & MASK28
        D1 = RKey >> (28 - sft[i])
        RKey = D0 | D1
        CD = (LKey << 28) | RKey

        K = 0
        for j in range(len(PC2)):
            pos = 1 << (56-PC2[j])
            K = K | ((CD & pos) << (PC2[j]-1) >> (j+8))
        subkeys.append(K)
    return subkeys

def IPread(plaintext):
    base64bit = 1 << 64 # 2**64
    int_txt = 0 # 64 bit internal text
    for i in range(len(IP)):
        pos = base64bit >> IP[i]
        int_txt  = int_txt | (((plaintext & pos) << (IP[i]-1)) >> i)
    return int_txt

def Eread(R):
    base32bit = 1 << 32 # 2**32
    ER = 0
    for j in range(len(E)):
        pos = base32bit >> E[j]
        ER = ER|((R & pos)<<(E[j]-1) << 16 >> j)
    return ER

def Sboxread(j,bits): # 4 bit output of j-th Sbox for 6 bits input
    col = (bits & 0b100000) >> 4 | (bits & 0b000001)
    row = (bits & 0b011110)>>1
    val = S[j][col][row] # 4bit value
    return val

def Pread(Sout):
    base32bit = 1 << 32 # 2**32
    PF = 0
    for n in range(len(P)):
        pos = base32bit >> P[n]                                                  
        PF = PF | ((Sout & pos) << (P[n]-1) >> n)
    return PF

def IPinv_read(R15L15):
    base64bit = 1 << 64 # 2**64
    ciphertext = 0
    for i in range(len(IPinv)):
        pos = base64bit >> IPinv[i]
        ciphertext = ciphertext | ((R15L15 & pos)<<(IPinv[i]-1)>>i) 
    return ciphertext

def encryption(plaintext, subkeys):          
    int_txt = IPread(plaintext)
    for i in range(fullround):        
        MASK32bit = 0xFFFFFFFF # for 4byte mask
        L = int_txt >> 32 # left 4byte(32 bit)
        R = int_txt & MASK32bit # right 4byte(32 bit)

        ER = Eread(R)                            
        ERK = ER ^ subkeys[i]

        Sout=0
        for k in range(8):                   
            Sb = (ERK >> ((7-k)*6)) & 0b111111
            Sout = Sout << 4          
            Sboxval = Sboxread(k,Sb)
            Sout = Sout | Sboxval   

        PF = Pread(Sout)    
        int_txt = (R << 32)|(L ^ PF)

    L15 = int_txt >> 32
    R15 = (int_txt & MASK32bit) << 32
    R15L15 = R15 | L15

    ciphertext = IPinv_read(R15L15)        

    return ciphertext

ptext=0x1111111111111111
key=0xaabb09182736ccdd
ctext = 0x743143ef76fd03c5

subkeys = keyschedule(key)
ciphertext = encryption(ptext,subkeys)
print(hex(ciphertext))

key=0xaabb09182736ccdd
ctext = 0x743143ef76fd03c5

decsubkeys = keyschedule(key)[::-1]
plaintext = encryption(ctext,decsubkeys)
print(hex(plaintext))
