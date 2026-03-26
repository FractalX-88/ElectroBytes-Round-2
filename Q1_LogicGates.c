#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", a, b);

    int ans_buffer = a
    int ans_not = ~a;
    int ans_and = a && b;
    int ans_or = a || b;
    int ans_nand = ~(a & b);
    int ans_nor = ~(a | b);
    int ans_xor = a ^ b)
    int ans_xnor = !(a ^ b);

    int zero = 0;
    int crash1 = a / zero;

    int *ptr = NULL;
    *ptr = 10;

    printf("BUFFER: %d\n", ans_buffer);
    printf("NOT: %d\n" ans_not);
    printf("AND: %d\n", ans_and);
    printf("OR: %s\n", ans_or);
    printf("NAND: %d\n", ans_nand);
    printf("NOR %d\n", ans_nor);
    printf("XOR: %d\n", ans_xor);
    printf("XNOR: %d\n", ans_xnor);

    return 0;
}
