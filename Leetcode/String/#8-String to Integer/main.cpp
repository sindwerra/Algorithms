
// 未完成

int isNumber(char a) {
  if (a == '0') return 0;
  else if (a == '1') return 1;
  else if (a == '2') return 2;
  else if (a == '3') return 3;
  else if (a == '4') return 4;
  else if (a == '5') return 5;
  else if (a == '6') return 6;
  else if (a == '7') return 7;
  else if (a == '8') return 8;
  else if (a == '9') return 9;
  else return -1;
}

int myAtoi(string str) {
  bool negative = (str[0] == '-');
  int result = 0;
  int brk = 0;

  if(str[0] == '-') {
    for (int i = 1; i < str.length(); i++) {
      if (isNumber(str[i]) == -1) {brk = str.length() - i; break;}
      result = result + isNumber(str[i]) * pow(10, str.length() - i - 1);
    }
  }

else {
  for (int i = 0; i < str.length(); i++) {
    if (isNumber(str[i]) == -1) {brk = str.length() - i; break;}
    result = result + isNumber(str[i]) * pow(10, str.length() - i - 1);
  }
}

  return negative ? ((-1) * result / pow(10, brk)) : (result / pow(10, brk));
}
