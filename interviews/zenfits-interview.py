# # https://www.1point3acres.com/bbs/interview/software-engineer-132619.html
# # https://www.1point3acres.com/bbs/interview/software-engineer-169237.html

# # TODO:
# # merge k sorted arrays
# #我就是inplace的方法，这题其实是careercup上面的18.2 shuffle a deck of cards，从最后一个字符开始和前面字符中随机一个调换，然后i--，复杂度是O（n）。

# # #第一轮：
# # 国人小哥
# # Question1: print
# #       *
# #     ***
# #   *****
# # *******
# #   *****
# #    ***
# #      *

# def p(n):
#         # 000
#         # 00
#         # 0

#         # 0
#         for i in range(1, n, 2):
#                 spaceNum =  (n - i)//2
#                 print(spaceNum * "0" + i * "*")
#         for i in range(n, 0, -2):
#                 spaceNum =  (n//2 - i//2)
#                 print(spaceNum * " " + i * "*")

# p(9)
# # Question2: LeetCode 六三五 https://leetcode.com/problems/design-log-storage-system/description/

# # 第二轮:
# # ABC
# # Given a string, find the length of longest palindrome, the characters in the string can

# x = [('parker', 'parker'), ('laks', 'parker'), ('avinash', 'laks'), ('jonathan', 'avinash'), ('jason', 'laks'), ('david', 'parker'), ('arisa', 'david') ]
# #def buildGraph(inputs):
# #for element in x:
# #        print element[1]

# from collections import defaultdict
# def buildGraph(x):
#         graph = defaultdict(list)
#         for element in x:
#                 print (graph)
#                 if element[0] == element[1]:
#                         graph['boss'] = [element[0]]
#                 else:
#                     graph[element[1]].append(element[0])
               
#         return graph

# graph = buildGraph(x)

# def dfs(graph):
#         stack = []
#         visited = set()
#         for boss in graph['boss']:
#                 stack.append([0, boss])
#                 #visited.add(boss)
#         while stack:
#                 level, boss = stack.pop()
#                 if boss not in visited:
#                         visited.add(boss)
#                         print(' '*level, boss)
#                         if graph[boss]:
#                                 for employee in graph[boss]:
#                                         if employee not in visited:
#                                                 stack.append([level+1, employee])
#         #print visited
# dfs(graph)


def swap(s):
        temp = list(s)
        left, right = 0, len(s)-1
        while left < right:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
        return "".join(temp)

def rev(s):
        index = 0
        temp = res = ""
        while index < len(s):
                if s[index] != "0":
                        temp += s[index]
                else:
                        res += swap(temp) + "0"
                        temp = ""
                        while index + 1 < len(s) and s[index + 1] == "0":
                                res += "0"
                                index += 1
                index += 1

        res += swap(temp)
        return res
                        
                        


print(rev("abc00000bc00dc00ca00000"))