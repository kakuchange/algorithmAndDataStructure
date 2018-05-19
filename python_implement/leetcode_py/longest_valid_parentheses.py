"""
valid parenthese eg:
    () 最长合法括号为(), 长度为2
    (()) 最长合法括号为(()), 长度为4
    ()()( 最长合法括号为(), 长度为2

暴力解法:
    从头开始一遍遍, 遍历一样能找到最长合法括号,
时间复杂度分析:
    最好情况: 从头开始全串即为合法, 1 次就找到;
    最差情况: 前面没有合法, 至到最后一对才确定最长合法长度, 0 或者2,
              遍历(n-1) + (n-2) + ... + 1 次,
    平均情况: O(n**2)

动态规划:
    还是从头开始, 只遍历一遍, 具体做法

"""

