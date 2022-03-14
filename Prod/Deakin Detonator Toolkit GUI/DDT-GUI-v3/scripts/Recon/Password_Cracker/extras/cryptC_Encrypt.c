#include <stdio.h>
#include <crypt.h>
#include <string.h>

int main(int argc, char* argv[]) { // need to pass in argument

    char crypt_hash[20]; //Stores the hash from crypt()
    
    strcpy(crypt_hash, crypt(argv[1], argv[2])); //This will copy the output of crypt to a string
    printf("Encrypting password: %s with Salt: %s\n", argv[1], argv[2]); //Outputs plain text string
    printf("Hashed Password: %s\n", crypt_hash); //Outputs hash string

    return 0;
}
