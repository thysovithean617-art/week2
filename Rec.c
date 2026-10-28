#include <stdio.h>
#include<string.h>
// int f(int a, int b) {
//     if (b == 0) {
//         return 0;
//     }
//     if (b == 1) {
//         return a;
//     }
//     return a + f(a, b - 1);
// }

// int main() {
//     printf("%d", f(3, 4));
//     return 0;
// }

//  int fun(int n) {
//     if (n <= 0) {
//         return 1;
//     }

//     if (n % 2 == 0) {
//         return fun(n - 1) + 3;
//     }
//     else {
//         return fun(n - 1) + 2;
//     }
// }

// int main() {
//     printf("%d", fun(4));
//     return 0;
// }

// void pattern(int n){
//     if (n == 1){
//         printf("1 ");
//         return;
//     }
//     pattern(n - 1);
//     printf("%d ", n);
//     pattern(n - 1);
// }
// int main(){
//     int n = 3;
//     pattern(n);
//     return 0;
// }

// int power(int a, int b){
//     if(b == 0)  return 1;
//     return power(a ,b - 1) * a;
// }
// int main(){
//     int a, b;
//     printf("Enter a: ");
//     scanf("%d", &a);
//     printf("Enter b: ");
//     scanf("%d", &b);
//     int pow = power(a, b);
//     printf("%d", pow);
//     return 0;
// }

// int fibonacci(int n){
//     if(n == 0) return 0;
//     if(n == 1) return 1;
//     return fibonacci(n - 1) + fibonacci(n - 2);
// }
// int main(){
//     int n;
//     printf("Enter n: ");
//     scanf("%d", &n);
//     int fib = fibonacci(n);
//     printf("%d", fib);
//     return 0;
// }

// int countDigits(int number){
//     if(number < 10) return 1;
//     if(number / 10 > 0) return 1 + countDigits(number / 10);
// }
// int main(){
//     int number;
//     printf("Enter a number: ");
//     scanf("%d", &number);
//     int dig = countDigits(number);
//     printf("%d", dig);
//     return 0;
// }

// int max(int array[], int size){
//     if(size == 1) return array[0];
//     int largest = max(array, size - 1);
//     if(array[size - 1] > largest) return array[size - 1];
//     return largest;
// }
// int main(){
//     int size = 5;
//     int array[5] = {3, 9, 2, 15, 6};
//     int largest = max(array, size);
//     printf("%d", largest);
// }

