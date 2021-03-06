#include <stdio.h>
#define MAXS 30

char *search(char *s, char *t);
void ReadString( char s[] ); /* 裁判提供，细节不表 */

int main()
{
	char s[MAXS], t[MAXS], *pos;

	ReadString(s);
	ReadString(t);
	pos = search(s, t);
	if ( pos != NULL )
		printf("%d\n", pos - s);
	else
		printf("-1\n");

	return 0;
}

/* 你的代码将被嵌在这里 */
#include <string.h>
char *search(char *s, char *t)
{
	int slen, tlen;
	slen = strlen(s);
	tlen = strlen(t);
	for (int i = 0; i < slen - tlen + 1; i++) {
		int j;
		for (j = 0; j < tlen; j++) {
			if (s[j+i] != t[j]) break;
		}
		if (j == tlen) return &s[i];
	}
	return NULL;
}


/*
本题要求实现一个字符串查找的简单函数。
函数接口定义：

char *search( char *s, char *t );

函数search在字符串s中查找子串t，返回子串t在s中的首地址。若未找到，则返回NULL。
裁判测试程序样例：



输入样例1：

The C Programming Language
ram

输出样例1：

10

输入样例2：

The C Programming Language
bored

输出样例2：

-1

*/
