//                                     MANIPULATE

// fix the error
// #include <stdio.h>
// #include <string.h>
// int main(){
//     char names[3][10] = {"Alice", "Bob", "Eve"};
//     strcpy(names[1], "Charlie");
  
//     printf("%s\n", names[1]);
// }

// size of characters
// #include <stdio.h>
// #include <string.h>
// int lengthOf(char array[]){
//     int count = 0;
//     int index = 0;
//     while(array[index] != '\0'){
//         index++;
//         count++;
//     }
//     return count;
// }
// int main(){
//     char array[50];
//     printf("Enter a text: ");
//     fgets(array, sizeof(array), stdin);
//     int size = lengthOf(array) - 1;
//     printf("Number of characters: %d!", size);
//     return 0;
// }

// count vowels
// #include <stdio.h>
// #include <string.h>
// int countVowels(char array[]){
//     int Vow = 0;
//     int i = 0;
//     while(array[i] != '\0'){
//         if(array[i] == 'a' || array[i] == 'A'){
//             Vow++;
//         }else if(array[i] == 'e' || array[i] == 'E'){
//             Vow++;
//         }else if(array[i] == 'i' || array[i] == 'I'){
//             Vow++;
//         }else if(array[i] == 'o' || array[i] == 'O'){
//             Vow++;
//         }else if(array[i] == 'u' || array[i] == 'U'){
//             Vow++;
//         }
//         i++;
//     }
//     i++;
//     return Vow;
// }
// int main(){
//     char array[50];
//     printf("Enter a text: ");
//     fgets(array, sizeof(array), stdin);
//     int vow = countVowels(array);
//     if(vow == 0){
//         printf("There are no vowel!");
//     }else if(vow == 1){
//         printf("There are %d vowel!", vow);
//     }else{
//         printf("There are %d vowels!", vow);
//     }
// }

// reverse string
// #include <stdio.h>
// #include <string.h>
// void reverseString(char* ptrarray){
//     int start = 0;
//     int end = strlen(ptrarray) - 1;
//     char temp;
//     while(start < end){
//         temp = ptrarray[start];
//         ptrarray[start] = ptrarray[end];
//         ptrarray[end] = temp;
//         start++;
//         end--;
//     }
// }
// int main(){
//     char array[50];
//     printf("Enter a text: ");
//     fgets(array, sizeof(array), stdin);
//     reverseString(array);
//     printf("Reverse: %s", array);
//     return 0;
// }

// Lowercase letters to uppercase letters
// #include <stdio.h>
// #include <string.h>
// #include <ctype.h>
// void toUpper(char* ptrText){
//     int i = 0;
//     while(*(ptrText + i) != '\0'){
//         if(*(ptrText + i) >= 'a' && *(ptrText + i) <= 'z'){
//             *(ptrText + i) = *(ptrText + i) - 32;
//         }
//         i++;
//     }
// }
// int main(){
//     char text[50];
//     printf("Enter lowercase letters: ");
//     fgets(text, sizeof(text), stdin);
//     toUpper(text);
//     printf("Uppercase letters: %s", text);
//     return 0;
// }

// string to integer
// #include <stdio.h>
// #include <string.h>
// int parseInt(char* ptrarray){
//     int i = 0;
//     int result = 0;
//     int digit = 0;
//     while(*(ptrarray + i) != '\0'){
//         digit = *(ptrarray) - '0';
//         result = (result * 10) + digit;
//         i++;
//     }
//     return result;
// }
// int main(){
//     char array[50];
//     printf("Enter a string: ");
//     fgets(array, sizeof(array), stdin);
//     int size = parseInt(array);
//     printf("Numbers: %s", array);
//     return 0;
// }


//                                      CREATE

// Stylish Initials Generater
#include <stdio.h>
#include <string.h>
void printInitials(char* ptrarray){
    *ptrarray = *ptrarray - 32; 
    int i = 1;
    char dot[1] = ".";
    while(*(ptrarray + i) != '\0'){
        if(*(ptrarray + i) == ' '){
            *(ptrarray + i) = dot[1];
        }
    }
}
int main(){
    char array[50];
    printf("Enter a text: ");
    fgets(array, sizeof(array), stdin);
    printInitials(array);
    printf("Initials letters: %s", array);
    return 0;
}