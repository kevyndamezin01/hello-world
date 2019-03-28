#include <iostream>
using namespace std;

int main()
{
    int(number);
    int(even);
    string(name);

    cout << "Hello there what is you're name?\n";
    cin >> name;

    cout << "Hello there " << name << " this script will work out if you're chosen number is odd or even\n";

    cout << "Please provide the number that you wish to check if it is an odd or even number\n";
    cin >> number;

    if(number % 2 == 0)
    {
        cout << number << " is an even number" << endl;
    }

    else if(number % 2 != 0)
    {
        cout << number << " is an odd number" << endl;
    }

    else
    {
        cout << "who knows what number you have chosen but " << number << " is not even or odd!!!" << endl;
    }
}