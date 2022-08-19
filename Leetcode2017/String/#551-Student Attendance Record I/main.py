# coding=utf-8

'''
You are given a string representing an attendance record for a student. 
The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' 
(absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''

'''
Beat 95.86%
公司：Google
'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent, late = [], []

        for record in s:
            if record == 'A':
                if absent:
                    return False
                else:
                    absent.append(record)
                late = []
            elif record == 'L':
                late.append(record)
                if len(late) == 3:
                    return False
            else:
                late = []
        
        return True