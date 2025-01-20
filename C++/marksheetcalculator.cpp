#include <iostream>

using namespace std;
int main (){
    int mathsValue;
    int scienceValue;
    int englishValue;

    cout<< "The marks of maths are: ";
    cin >> mathsValue;
       
    cout << "The marks of science are:";
    cin >> scienceValue;

    cout << "The marks of english are: ";
    cin >> englishValue;

    int myPercentage = (mathsValue + scienceValue + englishValue)*100/ 300;

    cout << "The total percentage is: " << myPercentage;

     return 0;
}