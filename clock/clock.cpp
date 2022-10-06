#include<iostream>
using namespace std;
int main() {
    int hr = 0, min = 0, sec = 0;
    while (true) {
        cout << hr << " : " << min << " : " << sec << endl;
        sec++;
        if (sec == 60) {
            min++;
            sec = 0;
            if (min == 60) {
                hr++;
                min = 0;
                if (hr == 24) {
                    hr = 0;
                }
            }
        }
    }
}