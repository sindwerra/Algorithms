#include <iostream>

using namespace std;

// 此代码溢出问题解决不了

int reverse(int x) {
  bool zf = true;
  int result = 0;
  int count = 0;

  if (x > 0) {zf = true;}
  else if (x < 0){
    zf = false;
    x = abs(x);
  }
  else { return x; }

  queue<int> store;

  while (x != 0) {
    int rem = x % 10;
    x = (x - rem) / 10;
    store.push(rem);
    count++;
  }

  while (!store.empty()) {
    int temp = store.front();
    store.pop();
    result = power(count - 1) * temp + result;
    count--;
  }

  if (zf) { return result > INT_MAX ? 0 : result; }
  else { return result > INT_MAX ? 0 : result * (-1); }
}

int power(int x) {
        int result = 1;
        while (x > 0) {
            result = 10*result;
            x--;
        }
        return result;
}

// 可用正解

int reverse(int x) {
  long returnInt = 0;
  while (x) {
    returnInt = returnInt*10+x%10;
    x/=10;
  }
  
  if (returnInt>0)
    return returnInt > INT_MAX ? 0 : returnInt;
  else return returnInt < INT_MIN ? 0 : returnInt;
}
