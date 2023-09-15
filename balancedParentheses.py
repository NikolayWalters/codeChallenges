"""
Write a function to generate all possible n pairs of balanced parentheses. 

Input: n=1
Output: {}
Explanation: This the only sequence of balanced 
parenthesis formed using 1 pair of balanced parenthesis. 

Input : n=2
Output: 
{}{}
{{}}
Explanation: This the only two sequences of balanced 
parenthesis formed using 2 pair of balanced parenthesis. 

"""

def generate_parenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    res = []
    backtrack()
    return res

# Test for n=3
print(generate_parenthesis(3))
