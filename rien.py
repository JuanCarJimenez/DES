import random

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    while (len(result)%64!= 0):
        result= result + [0,0,0,0,0,0,0,0]
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

#######################################################   KEY_SCHEDULE

PC1= [49, 41, 33, 25, 17, 9, 1,
        50, 42, 34, 26, 18, 10, 2,
        51, 43, 35, 27, 19, 11, 3,
        52, 44, 36, 28, 20, 12, 4,
        53, 45, 37, 29, 21, 13, 5,
        54, 46, 38, 30, 22, 14, 6,
        55, 47, 39, 31, 23, 15, 7,
        56, 48, 40, 32, 24, 16, 8]

PC2= [14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32]

def l_shift(data, k):
    if k not in (1, 2, 9, 16):
        shift= 2
    else:
        shift= 1
    return data[shift:] + data[:shift]

def permutation(data, permutation):
    permuted_data= [0] * len(permutation)
    for i in range(len(permutation)):
        index = permutation[i]-1
        permuted_data[i]= data[index]
    return permuted_data

def key_sch(key):
    keys=[]
    my_key= permutation(key, PC1) ## PC1 (key)
    list_L= my_key[:28]
    list_R= my_key[28:]
    for i in range (1,17):
        list_L= l_shift(list_L, i)
        list_R= l_shift(list_R, i)
        keys.append(permutation((list_L + list_R), PC2)) ## PC2(key)
    return keys

def random_key(length):
    return [random.randint(0,1) for _ in range (length)]


##################################################################### ENCRYPTION
E= [32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

P= [16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]

sbox_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

sbox_2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

sbox_3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

sbox_4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

sbox_5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

sbox_6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

sbox_7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 8, 1],
    [13, 0, 11, 7, 4, 9, 1, 10 , 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

sbox_8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]

sboxes= {
        "sbox_1": sbox_1,
        "sbox_2": sbox_2,
        "sbox_3": sbox_3,
        "sbox_4": sbox_4,
        "sbox_5": sbox_5,
        "sbox_6": sbox_6,
        "sbox_7": sbox_7,
        "sbox_8": sbox_8}


def substitution(my_data, sbox):
    my_list= [my_data[0], my_data[5]]
    row= int(''.join(str(bit) for bit in my_list), 2)
    column=int(''.join(str(bit) for bit in my_data[1:5]), 2)
    decimal_number= sbox[row][column]
    binary_string = bin(decimal_number)[2:].zfill(4)
    bit_list = [int(bit) for bit in binary_string]
    return bit_list 


def DES_encryption(data, key):
    my_data= permutation(data, E)  #### E(x)
    my_string= []
    for i in range(len(my_data)):  ##### E(x) XOR key_i
            my_data[i]= (my_data[i]+key[i]) % 2
    for i in range(8):
        sbox_value= sboxes.get(f"sbox_{i+1}")
        my_string= my_string + substitution(my_data[6*i:(6*i)+6], sbox_value)
    my_string= permutation(my_string, P) #### P
    return my_string


#################################################################### FEISTEL


### len(P_I)= 64 
P_I= [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

### len(P_I)= 64
P_I_I= [40,  8, 48, 16,  56, 24,  64, 32,
     39,  7, 47, 15,  55, 23,  63, 31,
     38,  6, 46, 14,  54, 22,  62, 30,
     37,  5, 45, 13,  53, 21,  61, 29,
     36,  4, 44, 12,  52, 20,  60, 28,
     35,  3, 43, 11,  51, 19,  59, 27,
     34,  2, 42, 10,  50, 18,  58, 26,
     33,  1, 41,  9,  49, 17,  57, 25]


def mu(l_text, r_text):
    return r_text, l_text 

def phi(l_text, r_text, key):
    y= DES_encryption(r_text, key)
    for i in range(len(l_text)):
        l_text[i]= (l_text[i] + y[i]) % 2
    return l_text, r_text

def DES(text, keys): ## texto de 64p y 16 keys de 48 
    my_text= permutation(text, P_I)
    l_text= my_text[:32]
    r_text= my_text[32:]
    for i in range(15):
        l_text, r_text = phi(l_text, r_text, keys[i])
        l_text, r_text = mu(l_text, r_text)
    l_text, r_text = phi(l_text, r_text, keys[15])
    my_text= l_text+r_text
    my_text= permutation(my_text, P_I_I)
    return my_text

def DES_block(text, keys):
    my_text= []
    for i in range(len(text)//64):
        my_text= my_text+DES(text[i*64:(i+1)*64], keys)
    return my_text

######################################################################## PROGRAMA


#key=[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]
key= [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
#key= (random_key(56))
my_keys= key_sch(key)


message= tobits('Gracias. ¿Cúal es tu nombre completo?') ######## mensaje a encriptar
#message= [0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0]

ciphertext= DES_block(message, my_keys)
#print(f"Cifrado:", ciphertext)
print(f"Texto cifrado:", frombits(ciphertext))


my_keys.reverse()
deciphertext= DES_block(ciphertext, my_keys)
deciphered_message= frombits(deciphertext)
print(f"Texto descifrado:", deciphered_message)

#def avalanche_test(message, my_keys):
#    ciphertext_1 = DES(message, my_keys)
#    message_length = len(message)
#    c=0
#    for i in range(message_length):
#        message[i] = (message[i] + 1) % 2
#        ciphertext_2 = DES(message, my_keys)
#        message[i] = (message[i] + 1) % 2
#        for j in range(message_length):
#            if ciphertext_1[j] != ciphertext_2[j]:
#                c+=1
#    avalanche= c/(message_length)
#    return avalanche

#print(avalanche_test(message, my_keys))
