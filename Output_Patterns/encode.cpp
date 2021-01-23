#include <cstdio>

int main()
{
	int a,b=0,c=10;

	const char *str=
		"TFy!QJu ";

	do{
		a=str[b];
		b++;

		int len=a-64;   //execute loop a-64 times
		while(len>0){
			len--;
			c++;        
			char ch;
			if(c==90){  //print \n on every 80th char
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

