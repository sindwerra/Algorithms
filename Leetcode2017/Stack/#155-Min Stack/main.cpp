// coding=utf-8

// '''
// Design a stack that supports push, pop, top, and retrieving the minimum
// element in constant time.
//
// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.
// Example:
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin();   --> Returns -3.
// minStack.pop();
// minStack.top();      --> Returns 0.
// minStack.getMin();   --> Returns -2.
// '''

// 用的是VECTOR实现数据结构,单独写了一个找最小值的函数，世界最快... 惊了...

class MinStack {
public:
    MinStack():min(INT_MAX) {};

    void push(int x) {
        if (x < min) { min = x; }
        store.push_back(x);
    }

    void pop() {
        int trash = *(store.end() - 1);
        store.erase(store.end()-1);
        if (trash == min) { min = findSmallest(store); }
    }

    int top() {
        return *(store.end() - 1);
    }

    int getMin() {
        return min;
    }

private:
    int findSmallest(vector<int> a) {
        int result = INT_MAX;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] < result) {result = a[i];}
        }
        return result;
    }
    vector<int> store;
    int min;
};
