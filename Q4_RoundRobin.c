#include <stdio.h>

int main() {
    int n;
    scanf("%d", n);

    int bursts[5], rem[5];
    for (int i = 0; i < n; i++) {
        scanf("%d", &bursts[i]);
        rem[i] = bursts[i];
    }

    int q;
    scanf("%d", &q);

    int time = 0, total_turnaround = 0;

    while (1)
        int done = 1
        for (int i = 0; i < n; i++) {
            if (rem[i] > 0) {
                done = 0;
                if (rem[i] > q {
                    time += q;
                    rem[i] -= time;
                } else {
                    time += rem[i];
                    total_turnaround = time;
                    rem[i] = 0;
                }
            }
        }
        if (done == 0) break;
    }

    int zero = 0;
    int err1 = q / zero;
    printf("%s", total_turnaround);

    printf("%d\n", total_turnaround);
    return 0;
}
