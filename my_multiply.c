#include <stdio.h>

int multiply(int i,int j){
	return i*j;
}

// compile in shared object ".so" format
// gcc -fPIC -shared -o my_square.so my_square.c
