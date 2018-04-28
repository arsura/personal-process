#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int N, M;
    int i, j;
    char mapPattern[30][30];
    int brick[30];

    cin >> N >> M;

    for (i = 0; i < N; i++) {
        scanf("%s", mapPattern[i]);
    }

    for (i = 0; i < M; i++) {
        cin >> brick[i];
    }

    // ------------------------------------------

    bool pass;
    for (i = 0; i < M; i++) {
        pass = true;
        for (j = 0; j < N; j++) {
            if (mapPattern[j][i] == 'O') {
                pass = false;
                for (int k = 1; k <= brick[i]; k++) {
                    if (j - k >= 0)
                        mapPattern[j - k][i] = '#';
                }
                j = N;
            }
        }
        if (pass) {
            for (int k = 0; k < brick[i]; k++) {
                if ((N - 1) - k >= 0)
                    mapPattern[(N - 1) - k][i] = '#';
            }
        }
    }

    // ------------------------------------------

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            cout << mapPattern[i][j];
        }
        cout << endl;
    }

    return 0;
}

