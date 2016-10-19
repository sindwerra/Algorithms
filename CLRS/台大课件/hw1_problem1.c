#include<stdio.h>
#include<stdlib.h>

int count = 0;
struct Point{
	int x;
	int y;
	int count;
};
int cmp(const void *a,const void *b){
	return (((struct Point *)a)->x > ((struct Point *)b)->x); // x increasing
}
int cmpf(const void *a,const void *b){
	return (((struct Point *)a)->y < ((struct Point *)b)->y); // y decreasing
}
struct Stack{
	struct Point *data;
	int cur;
};
int search(const struct Stack stack,const int y);
void divide(struct Point *point,int n){
	struct Point *left,*right;
	struct Stack lstack,rstack;
	int ln,rn,curL,curR,i;
	int flag1 = 1,flag2 = 1;
	if(n==0||n==1)	// base case
		return;
	if(n==2){
		count++;
		return;
	}
	
	ln = n/2;
	rn = n-ln;
	left = point;
	right = &point[ln];
	qsort(left,ln,sizeof(struct Point),cmpf);	// sort the left half and right half by y-coordinate
	qsort(right,rn,sizeof(struct Point),cmpf);
	
	lstack.data = (struct Point *)malloc(sizeof(struct Point)*ln);	// stack for the blocking curve
	rstack.data = (struct Point *)malloc(sizeof(struct Point)*rn);
	lstack.cur = -1;
	rstack.cur = -1;
	curL = 0;
	curR = 0;
	int c=0;
	while(flag1||flag2){	// flag means the left half or right half hasn't been finished yet
		
		if(flag1&&(left[curL].y>=right[curR].y||!flag2)){	// if the left half hasn't been finished and the top of not finishing points in left side is higher than right side
			
			while(lstack.cur!=-1&&left[curL].x>lstack.data[lstack.cur].x)	// pop up the points in the stack if the x-coordinate of current point is greater than stack's top
				lstack.cur--;
			lstack.cur++;
			lstack.data[lstack.cur] = left[curL];	
			lstack.data[lstack.cur].count = lstack.cur+1;	//update the stack

			if(rstack.cur==-1);
			//	puts("rstack empty");
			else if(lstack.cur==0)
				count+=rstack.data[rstack.cur].count;
			else	// 	half-search
				count+=(rstack.data[rstack.cur].count-search(rstack,lstack.data[lstack.cur-1].y));
			
			curL++;
			if(curL==ln)
				flag1 = 0;
		}
		else if(flag2&&(right[curR].y>=left[curL].y||!flag1)){	//similar to line 49
			while(rstack.cur!=-1&&right[curR].x<rstack.data[rstack.cur].x)
				rstack.cur--;
			
			rstack.cur++;
			rstack.data[rstack.cur] = right[curR];
			rstack.data[rstack.cur].count = rstack.cur+1;
			
			if(lstack.cur==-1);
				//puts("lstack empty");
			if(rstack.cur==0)
				count+=lstack.data[lstack.cur].count;
			else
				count+=(lstack.data[lstack.cur].count-search(lstack,rstack.data[rstack.cur-1].y));
			curR++;
			if(curR==rn)
				flag2 = 0;
		}
	}
	free(lstack.data);
	free(rstack.data);
	qsort(left,ln,sizeof(struct Point),cmp);
	qsort(right,rn,sizeof(struct Point),cmp);
	divide(left,ln);
	divide(right,rn);
}
int main(){
	int n,i;

	scanf("%d",&n);
	struct Point point[n];
	
	for(i=0;i<n;i++)
		scanf("%d%d",&point[i].x,&point[i].y);
	qsort(point,n,sizeof(struct Point),cmp);	// sort the points by x-coordinate
	
	divide(point,n);	// divide the problem into half and recursive
	
	printf("%d\n",count);
}
int search(const struct Stack stack,const int y){	//O(lg n) search time for lowerbound
	int L = 0;
	int R = stack.cur-1;
	int M=(L+R)/2;
	
	if(stack.data[0].y<y)
		return 0;
	if(stack.data[R+1].y>y)
		return stack.data[R+1].count;
	while(L<R){
		if(stack.data[M].y>y && stack.data[M+1].y<y)
			return stack.data[M].count;
		else if(stack.data[M].y>y)
			L = M+1;
		else
			R = M-1;
		M = (L+R)/2;
	}

	return stack.data[M].count;
}