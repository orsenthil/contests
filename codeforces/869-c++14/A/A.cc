#include <iostream>
#include <vector>

typedef long long ll;
const size_t mx = 5000006;
using namespace std;

ll mapping[mx];

int main() 
{
        int n;

        std::cin >> n;
        std::vector<int> xi(n);
        std::vector<int> yi(n);

        for (int i=0; i< n; i++){
                std::cin>>xi[i], mapping[xi[i]] = 1;
        }
        for (int i=0; i<n; i++) {
                std::cin>>yi[i], mapping[yi[i]] = 1;
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                        int xored = xi[i] ^ yi[j];
                        if (mapping[xored]) {
                                count++;
                        }
                }
        }

        if ((count % 2) == 0) {
                cout << "Karen" <<endl;
        } else {
                cout << "Koyomi" <<endl;
        }
}
