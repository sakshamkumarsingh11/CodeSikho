 #include <iostream>
using namespace std;
int main(){
    int mathsValue; // The marks of maths are stored here as a variable
    int chemValue; // The marks of chemistry are stored here as a variable
    int englishValue; // The marks of english are stored here as a variable
    int physicsValue; // The marks of physics are stored here as a variable
    int optsubValue; // The marks of other optional subject are stored here as a variable

    cout << "The value of maths";
    cin >> mathsValue;

    cout << "The value of chemistry";
    cin >> chemValue;

    cout << "The value of physics";
    cin >> physicsValue;

    cout << "The value of english";
    cin >> englishValue;

    cout << "The value of optional subject";
    cin >> optsubValue;

    int myPercentage = (mathsValue+ chemValue+ englishValue+ physicsValue+ optsubValue)*100/500;
    cout << "Your percentage is " << myPercentage;

    if (myPercentage> 75)
    {
        cout << " \n You recived distinction";
    }
    else if (myPercentage >= 50)
    {
        cout << "\n You passed";
    }
    else {
        cout << "\n You have failed";
    }

    return 0;
    }