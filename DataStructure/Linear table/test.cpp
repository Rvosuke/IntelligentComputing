#include <iostream>
using namespace std;

int function1(int x, int n) {
	int result = 1;
	for (int i = 0; i < n; i++) {
		result = result * x;
	}
	return result;
}

int function2(int x, int n) {
	if (n == 0) {
		return 1;
	}
	return function2(x, n - 1) * x;
}

int main()
{
	long a = 0;
	long b = 0;
	a = function1(2, 20);
	b = function2(2, 20);
	cout<<a<<"\n"<<b<<endl;
	return 0;
}