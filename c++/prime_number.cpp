// This script will work out if a number is odd or even
#include <iostream>
using namespace std;

int main()
{
    // Listing all the variables that are needed.
    int(number);
    int(even);
    string(name);

    cout << "Hello there what is you're name?\n";
    cin >> name;

    cout << "Hello there " << name << " this script will work out if you're chosen number is odd or even\n";
    
    // Asking the user to proived the number that they wish to check is odd or even.
    cout << "Please provide the number that you wish to check if it is an odd or even number\n";
    cin >> number;

    // Checking if the number is even.
    if(number % 2 == 0)
    {
        cout << number << " is an even number" << endl;
    }
    
    // Checking if the number is odd.
    else if(number % 2 != 0)
    {
        cout << number << " is an odd number" << endl;
    }
    
    //Checking if the user has entered something else other than a number.
    else
    {
        cout << "who knows what number you have chosen but " << number << " is not even or odd!!!" << endl;
    }
}