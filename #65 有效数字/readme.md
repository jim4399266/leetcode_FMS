这道题的状态有点多，可以分为10个状态，分别从s0到s9.
转移条件有：
blank：空格
sign：正负号
dot：小数点
digit：数字
e：科学计数法符号
other：其他情况

![image](https://github.com/jim4399266/leetcode_FMS/blob/main/%2365%20%E6%9C%89%E6%95%88%E6%95%B0%E5%AD%97/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20210218164147.png)

根据题目，当遍历字符串之后，最终状态为s2, s4, s7, s8时返回true，其余返回false
