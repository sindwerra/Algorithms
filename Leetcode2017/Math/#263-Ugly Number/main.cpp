// 小于等于0的数肯定不是ugly number，溢出的数也不是，溢出的解决办法就是把输入改成
// 长型数再用INT_MAX解决

// 本题思路就是非ugly number肯定在剥去所有能整除的2，3，5因子外衣后最后在个位数
// 肯定等于7或者直接不能被2，3，5的任意一个数整除

bool isUgly(int num) {
  if (num <= 0) { return false;}
  long result = long(num);
  if (result >= INT_MAX) { return false; }
    while (result > 10) {
      if (result % 2 != 0 && result % 3 != 0 && result % 5 != 0) { return false; }
      if (result % 2 == 0) { result /= 2; }
      if (result % 3 == 0) { result /= 3; }
      if (result % 5 == 0) { result /= 5; }
    }

    return result != 7;
}
