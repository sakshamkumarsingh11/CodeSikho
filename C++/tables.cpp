#include <iostream>
 
 using namespace std;

 int main(){
    int numbValue1;
    cout<<"Enter Table number: ";
    cin>>numbValue1;
    // >> "The number of multiples of 2" >> "i";
    // Learning 4 loop
    for (int i= 1; i<=10; i++)
    {
        //cout<< to_string(numbValue1) + "*" + to_string(i) + "="<< numbValue1*i<<endl;
        cout<< to_string(numbValue1) + "*" + to_string(i) + "="<< numbValue1*i<<endl;

    }

    return 0;
 }