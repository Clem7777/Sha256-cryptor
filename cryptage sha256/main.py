#By @Clem7777 on github ><

from hashlib import sha256

enter = input("Entrez le nom du fichier a chiffrer/dechiffrer : ")
sortie = input("Entrez le nom du fichier final : ")
key = input("Entré la clé : ")
keys = sha256(key.encode('utf-8')).digest()
with open(enter, 'rb') as f_enter:
    with open(sortie, 'wb') as f_sortie:
        i = 0
        while f_enter.peek():
            c = ord(f_enter.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i = i + 1