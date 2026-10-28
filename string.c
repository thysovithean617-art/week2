// #include <stdio.h>
// int countVowels(char array[]){
//     int i = 0;
//     int vow = 0;
//     while(array[i] != '\0'){
//         if(array[i] == 'a' || array[i] == 'A'){
//             vow++;
//         }else if(array[i] == 'e' || array[i] == 'E'){
//             vow++;
//         }else if(array[i] == 'i' || array[i] == 'I'){
//             vow++;
//         }else if(array[i] == 'o' || array[i] == 'O'){
//             vow++;
//         }else if(array[i] == 'u' || array[i] == 'U'){
//             vow++;
//         }
//         i++;
//     }
//     return vow;

// }
// int main(){
//     char array[100];
//     printf("Enter a sentence: ");
//     fgets(array, 100, stdin);
//     int vowels = countVowels(array);
//     if(vowels == 1){
//         printf("%d vowel", vowels);
//     }else{
//         printf("%d vowels", vowels);
//     }
//     return 0;
// }

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
//     char array[] = "CADT";
//     reverseString(array);
//     printf("%s", array);
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>
// #include <ctype.h>
// void toUpper(char* ptrarray){
//     int i = 0;
//     while(ptrarray[i] != '\0'){
//         if(ptrarray[i] >= 'a' && ptrarray[i] <= 'z'){
//             ptrarray[i] = ptrarray[i] - 32;
//         }
//         i++;
//     }

// }
// int main(){
//     char array[50];
//     printf("Enter an array: ");
//     fgets(array, 50, stdin);
//     toUpper(array);
//     printf("New array %s", array);
// }

// #include <stdio.h>
// #include <string.h>
// int parseInt(char *ptrarray){
//     int i = 0;
//     int digit = 0;
//     int result = 0;
//     while(i != '\0'){
//         digit = ptrarray[i] - '0';
//         result = result*10 + digit;
//         i++;
//     }
//     return result;
// }
// int main(){
//     char array[9];
//     printf("Enter an array of characters: ");
//     fgets(array, sizeof(array), stdin);
//     parseInt(array);
//     printf("New array integer: %s", array);
// }