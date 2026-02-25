// JF Silly Sentences

#include <stdio.h>
#include <string.h>

int main(){
    char prompts[5][45] = {"adjective", "animal", "past tense verb", "adverb", "exclamation (without the exclamation mark)"};
    char responses[5][50];

    int i;
    for (i=0; i<5; i++){
        printf("Type a(n) %s: ", prompts[i]);
        scanf("%50s", responses[i]);
    }

    char sillysillyconcatenation[100];
    strcpy(sillysillyconcatenation, responses[0]);
    strcat(sillysillyconcatenation, " ");
    strcat(sillysillyconcatenation, responses[1]);

    printf("Today I went to the zoo. I saw a(n) %s jumping up and down in its tree. It %s %s. I was so surprised that I shouted, '%s!'", sillysillyconcatenation, responses[2], responses[3], responses[4]);

    return 0;
}