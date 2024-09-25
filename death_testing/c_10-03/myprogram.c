#include <stdio.h>

int main() {
    int grade = 85;

    if (grade >= 90) {
        printf("Excellent! Grade: A\n");
    } else if (grade >= 80) {
        printf("Good job! Grade: B\n");
    } else if (grade >= 70) {
        printf("Satisfactory. Grade: C\n");
    } else if (grade >= 60) {
        printf("Needs improvement. Grade: D\n");
    } else {
        printf("You have failed the course.\n");
    }

    return 0;
}
