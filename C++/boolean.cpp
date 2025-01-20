/* #include <iostream>
using namespace std;

int main(){
    bool canHumanFly = false;
    bool canHumanSwim = true;
    cout << canHumanFly << "\n";
    cout << canHumanSwim;
    return 0;
} */

#include <iostream>
using namespace std;

int main(){
    int myAge;
    int votingAge = 18;
    cout << "Enter your age:";
    cin >> myAge;
    if (myAge>= votingAge)
    cout << "You can vote";
    else{
        cout << "You are not eligible to vote";

    }


}


