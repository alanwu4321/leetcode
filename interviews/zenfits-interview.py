# https://www.1point3acres.com/bbs/interview/software-engineer-132619.html
# https://www.1point3acres.com/bbs/interview/software-engineer-169237.html

# TODO:
# merge k sorted arrays
#我就是inplace的方法，这题其实是careercup上面的18.2 shuffle a deck of cards，从最后一个字符开始和前面字符中随机一个调换，然后i--，复杂度是O（n）。

# #第一轮：
# 国人小哥
# Question1: print
#       *
#     ***
#   *****
# *******
#   *****
#    ***
#      *

# Question2: LeetCode 六三五 https://leetcode.com/problems/design-log-storage-system/description/

# 第二轮:
# ABC
# Given a string, find the length of longest palindrome, the characters in the string can

x = [('parker', 'parker'), ('laks', 'parker'), ('avinash', 'laks'), ('jonathan', 'avinash'), ('jason', 'laks'), ('david', 'parker'), ('arisa', 'david') ]
#def buildGraph(inputs):
#for element in x:
#        print element[1]

from collections import defaultdict
def buildGraph(x):
        graph = defaultdict(list)
        for element in x:
                print (graph)
                if element[0] == element[1]:
                        graph['boss'] = [element[0]]
                else:
                    graph[element[1]].append(element[0])
               
        return graph

graph = buildGraph(x)

def dfs(graph):
        stack = []
        visited = set()
        for boss in graph['boss']:
                stack.append([0, boss])
                #visited.add(boss)
        while stack:
                count, boss = stack.pop()
                if boss not in visited:
                        visited.add(boss)
                        print(' '*count, boss)
                        if graph.get(boss, None):
                                for employee in graph[boss]:
                                        if employee not in visited:
                                                stack.append([count+1, employee])
        #print visited
dfs(graph)