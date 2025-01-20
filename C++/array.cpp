/* Set 1
#include <iostream>
#include <string>
using namespace std;

int main (){
string car[] = {"toyota", "nissan" ,"bmw", "audi"};
cout << car[3];
return 0;
}

set2


#include <string>
#include <iostream>
using namespace std;

int main (){
string car[] = {"toyota", "nissan" ,"bmw", "audi"};
for (int x=0; x<4; x++) {
cout << car[x] <<"\n";
}
return 0;
}

set 3- sizeof

#include <iostream>
using namespace std;

int main (){
int myNumbers[5] = {10, 20 ,30,40,50};
 cout << sizeof(myNumbers);

return 0;
}*/




//length of array

#include <iostream>
using namespace std;

int main() {
  int myNumbers[5] = {10, 20, 30, 40, 50};
  int lengthArray= sizeof(myNumbers)/sizeof(int);
 
  cout << lengthArray;

  return 0;
}