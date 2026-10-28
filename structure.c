// #include <stdio.h>
// #include <string.h>

// typedef struct{
//     char name[50];
//     int id;
//     float score[5];
// }Student;
// double getScoreAverage(Student student){
//     float score = 0;
//     for(int i = 0; i < 3; i++){
//         score += student.score[i];
//     }
//     return score/3;
// }
// int main(){
//     Student stu1 = {"Mey", 1, {2.5, 10, 5}};
//     Student stu2 = {"Prathpi", 2, {5, 5, 5}};

//     printf("Name: %s, Id: %d, Average Score: %0.2f\n", stu1.name, stu1.id, getScoreAverage(stu1));
//     printf("Name: %s, Id: %d, Average Score: %0.2f", stu2.name, stu2.id, getScoreAverage(stu2));
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// typedef struct{
//     int hour;
//     int min;
//     int sec;
// }Time;
// Time sumTime(Time time1, Time time2){
//     Time total = time1;

//     total.sec += time2.sec;
//     total.min += time2.min;
//     total.hour += time2.hour;

//     if(total.sec > 59){
//         total.min++;
//         total.sec -= 59;
//     }
//     if(total.min >= 59){
//         total.hour++;
//         total.min -= 59;
//     }
//     return total;
// }
// void duration(Time total){
//     printf("%dh%dmn%ds\n", total.hour, total.min, total.sec);
// }
// int compareTime(Time time1, Time time2){
//     if(time1.hour > time2.hour){
//         return 1;
//     }else if(time1.hour < time2.hour){
//         return -1;
//     }else if(time1.min > time2.min){
//         return 1;
//     }else if(time1.min < time2.min){
//         return -1;
//     }else if(time1.sec > time2.sec){
//         return 1;
//     }else if(time1.sec < time2.sec){
//         return -1;
//     }
//     return 0;
// }
// int main(){
//     Time time1 = {1, 45, 00};
//     Time time2 = {1, 30, 00};
//     printf("Time 1: %dh%dmn%ds\n", time1.hour, time1.min, time1.sec);
//     printf("Time 1: %dh%dmn%ds\n", time2.hour, time2.min, time2.sec);
//     duration(sumTime(time1, time2));
//     printf("%d", compareTime(time1, time2));
//     return 0;
// }

// #include <stdio.h>
// #include <string.h>
// typedef struct{
//     int hour;
//     int min;
//     int sec;
// }Time;
// typedef struct{
//     char name[50];
//     Time time;
// }Attendance;
// int compareTime(Time time1, Time time2){
//     if(time1.hour > time2.hour){
//         return 1;
//     }else if(time1.hour < time2.hour){
//         return -1;
//     }else if(time1.min > time2.min){
//         return 1;
//     }else if(time1.min < time2.min){
//         return -1;
//     }else if(time1.sec > time2.sec){
//         return 1;
//     }else if(time1.sec < time2.sec){
//         return -1;
//     }
//     return 0;
// }
// Attendance getLatest(Attendance attendance[5]){
//     Attendance latest = attendance[0];
//     for(int i = 0; i < 5; i++){
//         if(compareTime(attendance[i].time, latest.time) == 1){
//             latest = attendance[i];
//         }
//     }
//     return latest;
// }
// int main(){
//     Attendance list[5];
//     for(int i = 0; i < 5; i++){
//         scanf("%s %d %d %d ", list[i].name, &list[i].time.hour, &list[i].time.min, &list[i].time.sec);
//     }
//     Attendance latestStudent = getLatest(list);
//     printf("The latest student is: %s\n", latestStudent.name);
//     return 0;
    
// }