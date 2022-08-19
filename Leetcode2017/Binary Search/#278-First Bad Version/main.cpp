bool isBadVersion(int version);

int firstBadVersion(int n) {
  int lo = 1;
  int result = 1;
  int original = n;

  while (lo <= n) {
    if (isBadVersion(n)) { result = n; n = lo + (n - lo) / 2; }
    else { lo = n + 1; n *= 1.5; if (n > original) n = original; }
  }

  return result;
}
