#include <stdio.h>

int summer(int number) {
    if (number == 0) {
        return 0;
    } else {
        return number % 10 + summer(number / 10);
    }   
}

int main() {
    printf("%d", summer(123456789));
}