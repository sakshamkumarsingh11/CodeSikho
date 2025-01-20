#include <iostream>
using namespace std;

 int main(){
    int j;
    int x;

    cout << "Enter the value table:";
    cin >> j;

   cout << "Table formation till:";
   cin >> x;

    for (int j= 1; j<=x; j++)
    for (int i= 1; i<=10; i++)
   {
       cout << to_string(j) +"*" + to_string(i) + "=" << j*i<<endl;
    }
   
       return 0;
    }
  