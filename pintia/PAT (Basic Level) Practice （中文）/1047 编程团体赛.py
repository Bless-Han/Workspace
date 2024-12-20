'''
   @pintia psid=994805260223102976 pid=994805277163896832 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1047 编程团体赛
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805277163896832
   
'''
# @pintia code=start
n = int(input())

score_dict = {}
for i in range(n):
    s = input().split()
    score = int(s[1])
    team = s[0].split("-")[0]
    if team not in score_dict:
        score_dict[team] = 0
    score_dict[team] += score

max_value = max(score_dict.items(), key=lambda x: x[1])
print(max_value[0], max_value[1])



# @pintia code=end