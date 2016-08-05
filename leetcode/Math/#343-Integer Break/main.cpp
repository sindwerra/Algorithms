// 规律简而言之就是整除三的次数作为要拆分的数的个数

int integerBreak(int n) {
        int rem = n % 3;
        int count = (n - rem) / 3;
        int result = 1;

        // 这一段是不是可以有办法优化一下？

        if (n == 2) { return 1; }
        else if (n == 3) { return 2; }
        else if (n == 4) { return 4; }
        else if (n == 5) { return 6; }

        /////////////////////////////

        while (count > 1) {
            result = result * 3;
            count--;
        }

        if (rem == 2) {
            return result * 6;
        }

        else if (rem == 1) {
            return result * 4;
        }

        else { return result * 3; }

    }
