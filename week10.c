// #include <stdio.h>
// #include <stdlib.h>
// int main(){
//     int num_rat;
//     int* rat = NULL;
//     printf("How many ratings will you enter? ");
//     if(scanf("%d", &num_rat) != 1 || num_rat <= 0){
//         printf("Invalid number of participant!");
//         return 1;
//     }
//     rat = (int*)malloc(num_rat * sizeof(int));
//     if(rat == NULL){
//         printf("Memory allocated fail. Exiting!");
//         return 1;
//     }
//     for(int i = 0; i < num_rat; i++){
//         printf("Enter rating #%d: ", i + 1);
//         scanf("%d", &rat[i]);
//         while(rat[i] < 1 || rat[i] > 10){
//             printf("Invalid number!\nPlease enter a valid number from 1 to 10.\n");
//             printf("Enter rating #%d: ", i + 1);
//             scanf("%d", &rat[i]);
//         }
//     }
//     printf("\nRatings entered: ");
//     for(int i = 0; i < num_rat; i++){
//         printf("%d ", rat[i]);
//     }
//     free(rat);
//     rat = NULL;
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// typedef struct{
//     char name[50];
//     int salary;
// } Employee;
// int main(){
//     int cur_size = 2;
//     Employee* emp = (Employee*)malloc(cur_size * sizeof(Employee));
//     if(emp == NULL){
//         printf("First memory allocated fail!");
//         return 1;
//     }
//     printf("----- Enter detail for the first %d employees -----\n", cur_size);
//     for(int i =0; i < cur_size; i++){
//         printf("Employee %d name: ", i + 1);
//         scanf("%s", emp[i].name);
//         printf("Employee %d salary: ", i + 1);
//         scanf("%d", &emp[i].salary);
//     }
//     printf("\n");
//     int new_size = 5;
//     Employee* temp = (Employee*)realloc(emp, new_size * sizeof(Employee));
//     if(temp == NULL){
//         printf("Memory allocated fail.\n");
//         free(emp);
//         return 1;
//     }
//     emp = temp;
//     printf("----- Enter detail %d employees remain -----\n", new_size - cur_size);
//     for(int i = cur_size; i < new_size; i++){
//         printf("Employee %d name: ", i + 1);
//         scanf("%s", emp[i].name);
//         printf("Employee %d salary: ", i + 1);
//         scanf("%d", &emp[i].salary);
//     }
//     printf("\n");
//     printf("----- ALL EMPLOYEE RECORD -----\n");
//     for(int i = 0; i < new_size; i++){
//         printf("ID: %d | Name: %-15s | Salary: %d$\n", i + 1, emp[i].name, emp[i].salary);
//     }
//     free(emp);
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// typedef struct{
//     int* data;
//     int size;
//     int capacity;
// } List;
// void addToList(List* theList, int item) {
    
//     if (theList->size == theList->capacity) {
//         theList->capacity += 2;
//         printf("--> List is full, resizing to %d\n", theList->capacity);
//         int* temp = (int*)realloc(theList->data, theList->capacity * sizeof(int));
        
//         if (temp == NULL) {
//             printf("Memory reallocation failed! Exiting.\n");
//             exit(1); 
//         }
//         theList->data = temp;
//     }
//     theList->data[theList->size] = item;
//     theList->size++;
// }
// int main() {
//     List myList;
//     myList.size = 0;
//     myList.capacity = 2;
//     myList.data = (int*)malloc(myList.capacity * sizeof(int));
//     if (myList.data == NULL) {
//         printf("Memory allocation failed!\n");
//         return 1; 
//     }
//     printf("Initial list capacity: %d\n", myList.capacity);
//     int items_count;
//     printf("How many items do you want to add? ");
//     scanf("%d", &items_count);
//     for (int i = 0; i < items_count; i++) {
//         int user_value;
//         printf("Enter item #%d: ", i + 1);
//         scanf("%d", &user_value);
//         addToList(&myList, user_value);
//     }
//     printf("\nFinal list contents (%d items):\n", myList.size);
//     for (int j = 0; j < myList.size; j++) {
//         printf("%d ", myList.data[j]);
//     }
//     printf("\n");
//     free(myList.data);
//     myList.data = NULL;

//     return 0;
// }
