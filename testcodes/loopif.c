int main() {
    int a;
    int b;
    a = 0;
    b = 3;

    while (a < 5) {
        if (b > a) {
            b = b - 1;
        } else {
            a = a + 2;
        }endif
        a = a + 1;
    }
}
