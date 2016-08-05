int maxProfit(vector<int>& prices) {
    if (prices.size() == 0) return 0;
    if (prices.size() == 1) return prices[0];

    int max = INT_MIN;
    int i_max = 0;
    int min = prices[0];
    int i_min = INT_MAX;
    int result = 0;

    for (int m = 0; m < prices.size(); m++) {
      if (prices[m] > max) max = prices[m];
    }

    for (int i = 1; i < prices.size(); i++) {
      if (i_max >= i) {
        if (prices[i] >= min) continue;
        else result = max - prices[i]; i_min = i; min = prices[i]; continue;
      }

      else {
        max = INT_MIN;
        for (int m = i; m < prices.size(); m++) {
          if (prices[i] > max) {
            max = prices[i];
            i_max = i;
            if (max - min > result) result = max - min;
          }
        }
      }
    }

    return result;
}
