int maxProfit(vector<int>& prices) {
  int max = 0;

  for (int i = 0; i < prices.size() - 1; i++) {
    for (int m = i + 1; m < prices.size(); m++) {
      if (prices[m] - prices[i] > max) {
        max = prices[m] - prices[i];
      }
    }
  }

  return max;
}
