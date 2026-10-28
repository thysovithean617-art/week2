#include <stdio.h>
#include <string.h>
#define MAX_LEN 100
typedef struct {
    char data[MAX_LEN];
} String;
String trim(String src) {
    String result;
    for (int i = 0; i < MAX_LEN; i++) {
        result.data[i] = '\0';
    }
    int start = 0;
    while (src.data[start] == ' ' || src.data[start] == '\t') {
        start++;
    }
    if (src.data[start] == '\0') {
        return result; 
    }
    int end = strlen(src.data) - 1;
    while (end >= start && (src.data[end] == ' ' || src.data[end] == '\t' || src.data[end] == '\n')) {
        end--;
    }
    int j = 0;
    for (int i = start; i <= end; i++) {
        result.data[j] = src.data[i];
        j++;
    }
    result.data[j] = '\0';
    return result;
}
int main() {
    String input;
    strcpy(input.data, "   Hello world! \n");
    printf("Before trim: %s\n", input.data);
    String result = trim(input);
    printf("After trim: %s\n", result.data);
    return 0;
}


// #include <stdio.h>
// typedef struct {
//     int min;
//     int max;
// } Range;
// int countOverlap(const Range* ranges, int size){
//     int overlap = 0;
//     for(int i = 0; i < size; i++){
//         for(int j = i + 1; j < size; j++){
//             if(ranges[i].min <= ranges[j].max && ranges[j].min <= ranges[i].max){
//                 overlap++;
//             }
//         }
//     }
//     return overlap;
// }
// int main(){
//     Range ranges[] = {{1, 5}, {4, 8}, {10, 12}, {11, 13}};
//     int count = countOverlap(ranges, 4);
//     printf("Overlap: %d", count);
//     return 0;
// }


// #include <stdio.h>

// #define MAX_SIZE 100

// // Function to compute the diagonal sum
// int diagonalSum(int matrix[MAX_SIZE][MAX_SIZE], int n) {
//     int total_sum = 0;

//     for (int i = 0; i < n; i++) {
//         // 1. Add the main diagonal element (top-left to bottom-right)
//         total_sum += matrix[i][i];

//         // 2. Add the secondary diagonal element (top-right to bottom-left)
//         // Only add it if it's NOT the same element as the main diagonal (center element)
//         if (i != n - 1 - i) {
//             total_sum += matrix[i][n - 1 - i];
//         }
//     }

//     return total_sum;
// }

// int main() {
//     int n;
//     int matrix[MAX_SIZE][MAX_SIZE];

//     // Read the size of the matrix
//     if (scanf("%d", &n) != 1) {
//         return 1;
//     }

//     // Read the matrix elements row by row
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             scanf("%d", &matrix[i][j]);
//         }
//     }

//     // Calculate the total sum of diagonals
//     int result = diagonalSum(matrix, n);

//     // Print the final result
//     printf("%d\n", result);

//     return 0;
// }