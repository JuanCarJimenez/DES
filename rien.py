import random
#solo un comentarico
#Hola
### len(P) = 32, simple permutacion
P= [16, 7, 20, 21, 29, 12, 28, 17, 
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]

### len (PC1) = 56, se deshace de 8 bits
PC1= [57, 49, 41, 33, 25, 17,  9,
    1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4]
### len(PC2) = 48, se deshace de 8 bits
PC2= [14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10, 
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32]
### len(E) = 28, agrega 12 bits 
E= [32, 1, 2, 3, 4, 5, 
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17, 
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

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



def permutation(data, permutation):
    permuted_data= [0] * len(permutation)
    for i in range(len(permutation)):
        index = permutation[i]-1
        permuted_data[i]= data[index]
    return permuted_data

def E_extension(data):
  extended_data= []
  for i in E:
    extended_data.append(data[i-1])
  return extended_data

def swap(data):
    l= len(data)
    midpoint= l // 2
    return data[midpoint:] + data[:midpoint]

def shift(data, k):
    shifted_data= []
    if k == 1 or 2 or 9 or 16:
        for i in range(28):
            index= data

def l_shift(data, k):
    if k not in (1, 2, 9, 16):
        shift= 2
    else:
        shift= 1
    return data[shift:] + data[:shift]

def random_key(length):
    return [random.randint(0,1) for _ in range (length)]

def key_sch(key): ## regresa lista con 16 llaves de 48
    keys=[]
    permuted_key= permutation(key, PC1)
    block_length= len(permuted_key)//2
    C_0= permuted_key[:block_length]
    D_0= permuted_key[block_length:]
    for i in range(16):
        C_1= l_shift(C_0, i+1)
        D_1= l_shift(D_0, i+1)
        C_0= C_1
        D_0= D_1
        key_i= permutation(C_1 + D_1, PC2)
        keys.append(key_i)
    print(keys)
    return keys



def DES_encrypt(text, key): ## texto de 32 y key de 48 que genera key_sch -> texto de 32
    extended_text= E_extension(text)
    xor_text= [ a ^ b for a, b in zip(extended_text, key)]

    #permuted_text= permutation(selected_text, P)
    return True #permuted_text

def Feistel(text, key): ## texto de 64, key de 64 -> texto de 64
    output= permutation(text, P_I)
    keys= key_sch(key)
    L_0= output[:32]
    R_0= output[32:]
    for i in range (14):
        R_1=DES_encrypt(text, keys[i])
        L_1=L_0
        swap

    
data_P= [0,0,0,0,0,0,0,1,
        0,0,0,0,0,0,0,1,
        0,0,0,0,0,0,0,1,
        0,0,0,0,0,0,0,1]

data_PC1= [1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 11, 12, 13, 14,
           15, 16, 17, 18, 19, 20, 21, 
           22, 23, 24, 25, 26, 27, 28, 
           29, 30, 31, 32, 33, 34, 35,
           36, 37, 38, 39, 40, 41, 42,
           43, 44, 45, 46, 47, 48, 49,
           50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]

data_PC2= [1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 11, 12, 13, 14,
           15, 16, 17, 18, 19, 20, 21, 
           22, 23, 24, 25, 26, 27, 28, 
           29, 30, 31, 32, 33, 34, 35,
           36, 37, 38, 39, 40, 41, 42,
           43, 44, 45, 46, 47, 48, 49,
           50, 51, 52, 53, 54, 55, 56]

#permuted_data= p_permutation(data_PC2,PC2)
#extended_data = E_extension(data_P)
#swaped_data= swap(data_PC1)
#new= l_shift(data_PC2, 1)
a = random_key(32)
b = random_key (48)
DES_encrypt(a, b)
#print(new)




