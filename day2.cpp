#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> checksums;
    int in = 0;
    for(int i = 0; i < 3; i++){ //prob better ways to do this
        int currL, currS;
        for(int j = 0; j < 4; j++){
            cin >> in;
            currS = (in < currS) ? in : currS;
            currL = (in > currL) ? in : currL;
        }
        cout << "nums: " << currL << " " <<currS << "  " << currL - currS << endl;
        checksums.push(currL-currS);
    }
    long long total = 0;
    while(!checksums.empty()){
        total += checksums.top();
        checksums.pop();
    }
    cout << total;
}