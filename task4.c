#include <stdio.h>

struct return_value {
    int mx;
    int cnt;
};

void sequencer(struct return_value* rv) {
    int num;
    scanf("%d", &num);
    if (num == 0) {
        return;
    }
    if (num > rv->mx) {
        rv->mx = num;
        rv->cnt = 1;
    } else if (num == rv->mx) {
        rv->cnt++;
    }
    sequencer(rv);
}

int main() {
    struct return_value ans = {-1e9, 0};
    sequencer(&ans);
    printf("%d %d", ans.mx, ans.cnt);
}