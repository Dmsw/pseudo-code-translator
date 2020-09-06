#include <stdio.h>
#include <stdlib.h>
#define MAXLENGTH 10
#define INF 0x3f3f3f3f
typedef struct graph graph;
struct graph {
	int x;
	int y;
	graph g;
};
graph fun(graph a);

int main(int argc, char *argv[]){
	graph a;
	memset(a, 0, sizeof(struct graph));
	a.y = 1;
	
	a.a = 0;
	return 0;
}

graph fun(graph a){
	return a;
}


