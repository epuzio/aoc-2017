#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> nums;
    char in;
    while(cin >> in){
        nums.push_back(in - '0');
    }
    int total = 0;
    for(int i = 0; i < nums.size()/2; i++){
        if(nums[i] == nums[i+(nums.size()/2)]){
            total += nums[i]*2;
        }
    }
    cout << total;
}