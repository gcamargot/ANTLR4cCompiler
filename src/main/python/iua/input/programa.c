int main () {
    int y;
    int x = 5;
    int p, q, r, t;
    int as = 1, bs = 2, c = 3;
    int l, m = 1, n = 0, o;

    y = sumar(x, 10);

    {
        int a = 5;
        int b = a + x;
    }

    if (y == 14) {
        x = 2 * x;
        y = x + 2;
    }
    else {
        y = -2;
    }
    return 0;
}


int sumar (int a, int b) {
    int r = a + b;
    return r;
}


