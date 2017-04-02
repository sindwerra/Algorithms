# coding=utf-8

'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to 
the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the 
form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the 
form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will 
both belong to the range of [-100, 100]. And the output should be also in this form.
'''

'''
公司：Amazon
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        real_a, vir_a = a.split('+')
        real_b, vir_b = b.split('+')
        
        real_a, real_b = int(real_a), int(real_b)
        vir_a, vir_b = int(vir_a[:len(vir_a) - 1]), int(vir_b[:len(vir_b) - 1])
        
        real_res = real_a * real_b - vir_a * vir_b
        vir_res = real_a * vir_b + real_b * vir_a
        
        return str(real_res) + '+' + str(vir_res) + 'i'