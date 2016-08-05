#include <iostream>

using namespace std;

// 算法速度比较慢，while loop过多了

bool isPalindrome(int x) {
    int rem = 0;
    int temp = x;
    int count = 0;
    if (x < 0) {return false; }  // 题目不允许负数为对称数
    stack<int> comp;

    while (x != 0) {
      x = (x - x % 10) / 10;
      count++;
    }

    int mid = count / 2;

    while (mid != 0) {
      comp.push(temp % 10);
      temp = (temp - temp % 10) / 10;
      mid--;
    }

    mid = count / 2;

    if (count % 2 == 1) {
      temp = (temp - temp % 10) / 10;
    }

    while (mid != 0) {
      int digit = temp % 10;
      if (comp.top() != digit) {return false;}
      comp.pop();
      temp = (temp - digit) / 10;
      mid--;
    }

    return true;
}
