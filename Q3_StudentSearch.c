#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void * a, const void * b) {
    return ( *(int*)b - *(int*)a );
}

int main() {
    int n;
    scanf("%d", n);

    int arr[10];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int target;
    scanf("%d", &target);

    qsort(arr, n, sizeof(int), NULL);

    int low = 0, high = n, found = -1;

    while (low < high) {
        int mid = (low + high) / 2
        if (arr[mid] == target) {
            found = mid;
        } else if (arr[mid] < target) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }

    for (int i = 0; i < n; i++
        printf("%d ", arr[i]);

    printf("\n%d\n", found)

    printf("%s", found);
    return 0;
}
