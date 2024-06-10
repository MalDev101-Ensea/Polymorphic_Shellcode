# Polymorphic_Shellcode

Le shellcode polymorphique est une technique utilisée par les développeurs de shellcode pour masquer les véritables instructions du code, le rendant ainsi plus difficile à détecter et à analyser par les systèmes de sécurité et les antivirus. Voici une explication plus détaillée de ce concept :
Caractéristiques du shellcode polymorphique

    Déchiffrement à l'exécution
        Le shellcode est stocké dans un format chiffré ou obfusqué dans le programme. Lorsqu'il est exécuté, une routine de déchiffrement convertit le code chiffré en son format original avant l'exécution.

    Évasion des signatures
        En chiffrant ou en obfusquant les instructions, le shellcode polymorphique peut éviter la détection par les signatures statiques des antivirus et des systèmes de détection d'intrusion (IDS).

    Variabilité
        Chaque instance du shellcode peut être différente. Même si la fonctionnalité reste la même, les instructions et les valeurs peuvent varier, rendant chaque échantillon unique.

Un shellcode polymorphique typique comporte deux parties principales :

    Le déchiffreur : Une séquence d'instructions qui déchiffre le shellcode principal.
    Le shellcode chiffré : Le code qui exécute la fonction malveillante, mais qui est initialement chiffré ou obfusqué.

    
Avantages :

    Évasion des signatures : Éviter la détection par les signatures statiques.
    Variabilité : Chaque instance est différente, rendant difficile la création de signatures de détection.

Inconvénients :

    Complexité : Plus difficile à écrire et à déboguer que le shellcode traditionnel.
    Performance : La phase de déchiffrement ajoute un surcoût en termes de temps d'exécution.

Techniques de chiffrement

    XOR : Simple et rapide, mais peut être facilement détecté si la clé est connue.
    ROT : Rotation des bits dans chaque octet.
    Chiffrement plus avancé : AES, DES, mais rarement utilisé dans le shellcode en raison de la taille et de la complexité.


Étapes pour créer un shellcode polymorphique

    Écrire le shellcode original
        Commencez par écrire le shellcode original qui réalise la tâche souhaitée.

    Ajouter une routine de déchiffrement
        Ajoutez une routine qui déchiffrera le shellcode à l'exécution.

    Chiffrer le shellcode
        Chiffrez le shellcode original en utilisant une technique comme XOR.

    Introduire la variabilité
        Utilisez des techniques pour rendre chaque instance unique (obfuscation, NOP sleds, junk code, etc.).

    Automatiser le processus
        Écrivez un script ou un programme pour automatiser les étapes ci-dessus.


UTILISATION :

1 - Exécutez le script Python pour générer le shellcode polymorphique :

        python3 ShellcodeGenerator.py

2 - Copiez le shellcode généré (sortie du script Python) dans le code C à la place de unsigned char polymorphic_shellcode[].

3 - Compilez et exécutez le code C :

        gcc -o ShellcodeLauncher ShellcodeLauncher.c -z execstack -fno-stack-protector
        ./ShellcodeLauncher




        
