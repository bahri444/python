#include <iostream>
using namespace std;
void calculator()
{
    int a, b, hasil;
    char aritmatika;
    cout << "silahkan input angka pertama :";
    cin >> a;
    cout << "silahkan input operator :";
    cin >> aritmatika;
    cout << "silahkan input angka kedua :";
    cin >> b;
    switch (aritmatika)
    {
    case '+':
        hasil = a + b;
        break;
    case '-':
        hasil = a - b;
        break;
    case '*':
        hasil = a * b;
        break;
    case '/':
        hasil = a / b;
        break;

    default:
        cout << "operator salah";
        break;
    }
    cout << "hasil operasi aritmatika " << a << aritmatika << b << " = " << hasil << endl;
}
int main()
{
    calculator();
}
