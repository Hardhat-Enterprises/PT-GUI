#include <stdio.h>
#include <crypt.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char raw_word[40]; //Stores Untrimmed input (with \n)
    char word[40]; //Stores trimmed input (no \n)
    char *hash = argv[1]; //Stores Untrimmed input (with \n)
    char salt[4]; //Stores the salt from the hash
    char crypt_hash[20]; //Stores the hash from crypt()
    sprintf(salt, "%.2s", hash); //Get salt from hash

	FILE *wordlist = fopen(argv[2], "r"); // Open the wordlist from argument 2
	while(fgets(raw_word, 40, wordlist) != NULL) { //While not at end of file, copy line by line
        int length = strlen(raw_word); // Gets the length of the word to try
        sprintf(word, "%.*s", (length - 2), raw_word); //Needed to trim the \n\r
        strcpy(crypt_hash, crypt(word, salt)); //This will copy the output of crypt to a string

        if(strcmp(crypt_hash, hash) == 0) { //Compares 2 strings 0 = equal
            printf("Hash collision found for: %s\n", crypt_hash);
            printf("Password is: %s\n", word);
            fclose(wordlist); //Close the Open file
        }
	}

    return 0;
}
