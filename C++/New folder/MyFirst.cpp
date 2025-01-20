#include <iostream>

using namespace std;


int a = 23;
int b = 32;

int Add()
{ 
  int z;
  z=a+b;
  return z;
  //cout<< "Add Result:  "<<z<<"\n";
}

void Subtract()
{
  int z;
  z=a-b;
  cout<< "Subtract Result: "<<z<<"\n";
}

void Multiply()
{
  int z;
  z=a*b;
  cout<< "Multiply Result:  "<<z<<"\n";
}

int main(){
   int m; 
   m=Add();
   cout<< "Add Result:  "<<m<<"\n";
   Subtract();
   Multiply();
return 0;
}


