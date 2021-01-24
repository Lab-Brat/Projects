#include <cstdio>

int main()
{
	int a,b=0,c=10;
	
	// E(69)-64=5, str is a string of
	// consecutive 5 ' 's and 5 '!'s
	const char *str="@EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE";

	do{
		a=str[b];
		b++; //1st char will always be ' ', 2nd '!' and so on

		int len=a-64;   //execute loop a-64 times
		while(len>0){
			len--;
			c++;        
			char ch;
			if(c==50){  //print \n on every 80th char
				c=10;   
				ch='\n';
			}
			else{
				if(b%2==1)  //if b is odd, print spaces
					ch=' ';
				else
					ch='!'; //if b is even, print !
			}
			putchar(ch);
		}
	} while(a>0);
}

