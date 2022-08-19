// 二分法才能节省时间，O（lgn），如果用linear这题没有出的意义了

double myPow(double x, int n) {
        if (n == 0) return 1;
        return pow(x, n % 2) * myPow(x * x, n / 2);
    }
