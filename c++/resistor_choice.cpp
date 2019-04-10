// This script will work out the total resistance for a parallel or series resistor network.
#include <iostream>
using namespace std;

int main()
{
    // Listing all variables that are needed.
    float(R1);
    float(R2);
    float(RT);
    string(name);
    string(choice);

    cout << "Hello there what is you're name?\n";
    cin >> name;
    cout << "\n";
    cout << "Hello there " << name << "\n\n";

    cout << "This script will either work out the total resistance of a Parallel Resistor Network or a Series Resistor Network.\n\n";

    // Getting the Value of R1.
    cout << "What is the value of R1\n";
    cin >> R1;
    cout << "\n";

    // Getting the value of R2.
    cout << "What is the value of R2\n";
    cin >> R2;
    cout << "\n";
    
    // Aksing the user if they wish to work out parallel or series total resistance.
    cout << "Would you like to work out the total resitance for a Parallel or Series circuit?\n";
    cout << "Please enter in lower case format\n";
    cin >> choice;

    // Working out the total parallel resistance.
    if(choice == "parallel")
    {
        RT = (R1 * R2) / (R1 + R2);
        cout << "The total resistance for the parallel circuit is " << RT << " ohms" << endl;
    }

    // Working out the total series resistance.
    else if(choice == "series")
    {
        RT = R1 + R2;
        cout << "The total resistance for the series circuit is " << RT << " ohms" << endl;
    }
    // Letting the user know that they have not supplied the correct information for the script.
    else
    {
        cout << "You have not entered either Parallel or Series" << endl;
    }
    system("PAUSE");

    

}
