#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int BASE_PAIRS = 4;

char max(int consensus[], int size) {
    int mostCommon = 0;
    int mostCommon_position = 0;
    for (int i = 0; i < size; i++) {
        if (consensus[i] > mostCommon) {
            mostCommon = consensus[i];
            mostCommon_position = i;
        }
    }
    switch (mostCommon_position) {
        case 0:
            return 'A';
            break;
        case 1:
            return 'C';
            break;
        case 2:
            return 'G';
            break;
        default:
            return 'T';
            break;
    }
}

int main() {
    //Read DNAs 
    vector<string> DNAs(0);
    string DNA = "";
    while(cin >> DNA) DNAs.push_back(DNA);
    //Build consensus matrix P
    int n, m;
    m = DNAs.size();
    n = int(DNA.size());
    vector< vector<int> > cons (BASE_PAIRS, n);
    int result[n];
    for (int i = 0; i < n; i++) result[i] = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            switch (DNAs[i][j]) {
                case 'A':
                    cons[0][j]++;
                    break;
                case 'C':
                    cons[1][j]++;
                    break;
                case 'G':
                    cons[2][j]++;
                    break;
                case 'T':
                    cons[3][j]++;
            }
        }
    }
    //Determine the most common BP
    for (int i = 0; i < n; i++)
    {
        int acgt[BASE_PAIRS];
        for (int j = 0; j < BASE_PAIRS; j++)
            acgt[j] = cons[j][i];
        cout << max(acgt, BASE_PAIRS);
    }
    cout << endl;
}