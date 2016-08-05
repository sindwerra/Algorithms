// 快乐数即使一位也要继续计算，10以内的快乐数只有1和7必须要记住

bool isHappy(int n) {
  int store = 0;

  while (true) {
    store += (n % 10) * (n % 10);
    n = (n - (n % 10)) / 10;

    if (n == 0 && store < 10) { break; }
    else if (n == 0 && store >= 10) {
      n = store;
      store = 0;
    }
  }

  return store == 1 || store == 7;
}
