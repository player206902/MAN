import copy
import random

def MatchingAlgoA(users):
    users_copy  = copy.deepcopy(users)
    random.shuffle(users_copy)
    for i in range(len(users)):
        print(users[i])
        print(users_copy[i])
        print()

def MatchingAlgoB (users):
    for i in range (len(users)):
        len_count = list()
        for j in range (len(users)):
            len_count.append(0)
            if i == j:
                continue
            else:
                count_right_letters = 0
                for t in range(min(len(users[i][2]), len(users[j][5]))):
                    if users[i][2][t] == users[j][5][t]:
                        count_right_letters += 1
                if ((min(len(users[i][2]), len(users[j][5]))) / 4 * 3)  < count_right_letters:
                    len_count[j] += 4

                count_right_letters = 0
                for t in range(min(len(users[j][2]), len(users[i][5]))):
                    if users[j][2][t] == users[i][5][t]:
                        count_right_letters += 1
                if (min(len(users[j][2]), len(users[i][5])) / 4 * 3)  < count_right_letters:
                    len_count[j] += 4

                if (abs(users[i][3] - users[j][3])) <= 1:
                    len_count[j] += 3
                elif (abs(users[i][3] - users[j][3])) <= 2:
                    len_count[j] += 2
                elif (abs(users[i][3] - users[j][3])) <= 3:
                    len_count[j] += 1

                count_right_letters = 0
                for t in range(min(len(users[i][4]), len(users[j][4]))):
                    if users[i][4][t] == users[j][4][t]:
                        count_right_letters += 1
                if (min(len(users[i][4]), len(users[j][4])) / 4 * 3)  < count_right_letters:
                    len_count[j] += 5
        
        max_count = 0
        max_ind = 0
        for t in range(len(users)):
            if max_count < len_count[t]:
                max_count = len_count[t]
                max_ind = t
        print(users[i])
        print(users[max_ind])
        print()


def MatchingAlgoC(users):
    arr_match_1 = list()
    arr_match_2 = list()
    for i in range(9):
        arr_match_1.append([])
        arr_match_2.append([])
    
    for i in range (len(users)):
        if (users[i][2] == "piano"):
            arr_match_1[0].append(i) 
        elif (users[i][2] == "guitar"):
            arr_match_1[1].append(i)
        elif (users[i][2] == "violin"):
            arr_match_1[2].append(i)
        elif (users[i][2] == "drums"):
            arr_match_1[3].append(i)
        elif (users[i][2] == "bass-guitar"):
            arr_match_1[4].append(i)
        elif (users[i][2] == "vocal"):
            arr_match_1[5].append(i)
        elif (users[i][2] == "cello" or users[i][2] == "viol"):
            arr_match_1[5].append(i)
        elif (users[i][2] == "accordion" or users[i][2] == "harmonica"):
            arr_match_1[6].append(i)
        elif (users[i][2] == "saxophone"):
            arr_match_1[7].append(i)
        elif (users[i][2] == "electro"):
            arr_match_1[8].append(i)

    for i in range (len(users)):
        if (users[i][5] == "piano"):
            arr_match_2[0].append(i) 
        elif (users[i][5] == "guitar"):
            arr_match_2[1].append(i)
        elif (users[i][5] == "violin"):
            arr_match_2[2].append(i)
        elif (users[i][5] == "drums"):
            arr_match_2[3].append(i)
        elif (users[i][5] == "bass-guitar"):
            arr_match_2[4].append(i)
        elif (users[i][5] == "vocal"):
            arr_match_2[5].append(i)
        elif (users[i][5] == "cello" or users[i][5] == "viol"):
            arr_match_2[5].append(i)
        elif (users[i][5] == "accordion" or users[i][5] == "harmonica"):
            arr_match_2[6].append(i)
        elif (users[i][5] == "saxophone"):
            arr_match_2[7].append(i)
        elif (users[i][5] == "electro"):
            arr_match_2[8].append(i)

    for i in range(9):
        for j in range(0, min(len(arr_match_1[i]),len(arr_match_2[i])), 2):
            print(users[arr_match_1[i][j]])
            print(users[arr_match_2[i][j]])
            print()


print ("How users we have?")
users = int(input())
arr_users = []

for i in range (users):
    arr = []
    print("1) Name:")
    t = input()
    arr.append(t)
    print("2) Surname:")
    t = input()
    arr.append(t)
    print("3) Your instrument:")
    t = input()
    arr.append(t)
    print("4) Your skills (please, send a number):")
    print("      1. Beginner")
    print("      2. Pre-intermediate")
    print("      3. Intermediate")
    print("      4. Upper intermediate")
    print("      5. Advanced")
    t = int(input())
    arr.append(t)
    print("5) Your music style:")
    t = input()
    arr.append(t)
    print("6) Whom are you looking for?")
    t = input()
    arr.append(t)
    arr_users.append(arr)


print("How groups we have?")
groups = int(input())
arr_groups = []

for i in range(groups):
    arr = []
    print("1)Name:")
    t = input()
    arr.append(t)
    print("2)Your skills (please, send a number):")
    print("    1. Beginner")
    print("    2. Pre-intermediate")
    print("    3. Intermediate")
    print("    4. Upper intermediate")
    print("    5. Advanced")
    t = int(input())
    arr.append(t)
    print("3)Your music style:")
    t = input()
    arr.append(t)
    print("4)How musicians you want?")
    a =  int(input())
    print("5)Please say their musical instruments:")
    mus = []
    for i in range(a):
        mus.append(input())
    arr.append(mus)
    arr_groups.append(arr)

print(arr_groups)
'''
print("Please, select the number of algo:")
n = int(input())    
print("User to user:")
if n == 1:
    MatchingAlgoA(arr_users)
elif n == 2:
    MatchingAlgoB(arr_users)
else:
    MatchingAlgoC(arr_users)
print("User to group:")
if n == 1:
    MatchingAlgoD(arr_users, arr_groups)
elif n == 2:
    MatchingAlgoE(arr_users, arr_groups)
else:
    MatchingAlgoF(arr_users, arr_groups)
'''    
