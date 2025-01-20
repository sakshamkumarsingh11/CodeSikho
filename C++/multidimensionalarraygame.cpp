#include <iostream>
using namespace std;

int main (){
bool score[4][4]={
    {1, 0, 1, 0},
    {0, 0, 0, 0},
    {1, 0, 0, 1},
    {0, 0, 0, 1}
};

int hits=0;
int numberOfturns=0;
int row; 
int column;

while(hits<4){
    cout << "Select coordinates"<< "\n";

    cout << "Select the number of row between 0 to 3";
    cin >> row;

    cout << "Select the number of column from between 0 to 3";
    cin >> column;

}

    if(score [row][column]= 1);
    {hits++;

    cout << "Excellent!" <<(4-hits) << "left \n";
    

    } 
    else: {
    cout << "Try again";
    numberOfturns++;
    }
    cout << "Victory"<< "\n";
    cout << "You won by"<< numberOfturns <<"turns";
    return 0;
}
