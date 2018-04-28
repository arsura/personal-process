#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    int v = 0;
    int x = 0;
    int l = 0;
    int c = 0;

    int d;
    cin >> d;

    int n;
    for (int j = 1; j <= d; j++) {

        // 100 - 400
        n = j % 1000;
        n = n / 100;
        if (n == 1) { c++; }
        if (n == 2) { c+=2; }
        if (n == 3) { c+=3; }
        if (n == 4) {}

        // 10 - 99
        n = j % 100;
        n = n / 10;
        if (n == 1) { x++; }
        if (n == 2) { x+=2; }
        if (n == 3) { x+=3; }
        if (n == 4) { x++; l++; }
        if (n == 5) { l++; }
        if (n == 6) { l++; x++; }
        if (n == 7) { l++; x+=2; }
        if (n == 8) { l++; x+=3; }
        if (n == 9) { x++; c++; }

        // 1-9
        n = j % 10;
        if (n == 1) { i++; }
        if (n == 2) { i+=2; }
        if (n == 3) { i+=3; }
        if (n == 4) { i++; v++; }
        if (n == 5) { v++; }
        if (n == 6) { v++; i++; }
        if (n == 7) { v++; i+=2; }
        if (n == 8) { v++; i+=3; }
        if (n == 9) { i++; x++; }

    }

    cout << i << " " << v << " " << x << " " << l << " " << c << endl;

    return 0;
}