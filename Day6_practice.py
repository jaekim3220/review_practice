'''!while_statements.py'''

'''while 구구단'''
# a = 5
# dan = 0
# while dan < 9:
#     dan += 1
#     print(f"{a}X{dan} = {a*dan}")

'''입력 숫자 계산 구구단'''
# while True:
#     a = int(input("입력 값 : "))
#     if a > 9 or a <= 0:
#         print("다시 입력")
#         continue
#     for dan in range(1,10):
#         print(f"{a}X{dan} = {a*dan}")

'''while 사용한 구구단 5단~9단까지 한꺼번에 출력'''
# dan = 4
# while dan < 9:
#     dan += 1
#     for a in range(1,10):
#         print(f"{dan}X{a} = {a*dan}")

'''for_list_statements.py'''

'''for-break'''
# lista = ['b', 'b', 'ab', 'a', 'b', 'a']
# for a in range(len(lista)):
#     if lista[a] == 'a':
#         print(f"{a+1}번 손님 당첨")
#         break

'''for문을 이용한 구구단'''
# a = 5
# for dan in range(1,10):
#     print(f"{a}X{dan} = {a*dan}")

'''for문을 이용한 정렬 알고리즘(sort 미사용)'''
'''오름차순'''
# lista = [93, 34, 62, 57, 9, 54, 87, 15, 84]
# # for a in range(len(lista)):
# for a in range(len(lista)-1):
#     for b in range(a+1, len(lista)):
#         if lista[a]>lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)
'''내림차순'''
# lista = [93, 34, 62, 57, 9, 54, 87, 15, 84]
# for a in range(len(lista)):
#     for b in range(a+1, len(lista)):
#         if lista[a]<lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)

'''행렬의 덧셈 2중 for문'''
# lista = [[1,2,3],[2,3,4]]
# listb = [[3,4,5],[5,6,7]]

# newlist = []
# for a in range(len(lista)):
#     listval = []
#     for b in range(len(lista[0])):
#         listsum = lista[a][b] + listb[a][b]
#         listval.append(listsum)
#     newlist.append(listval)
# print(newlist)

'''function_statements.py'''

'''사용자의 input을 받아 input 값의 누적 합 더하기
100 입력'''
# def myPlusFunc(myinput):
#     mysum = 0
#     for a in range(1, myinput+1):
#         mysum += a
#     return mysum
# myinput = int(input("입력 값 : "))
# result = myPlusFunc(myinput)
# print(result)

'''input 값 2개를 받아 input을 서로 더한 뒤 *2만큼의 결과를 return
이후 해당 값을 호출해 호출된 결과 값을 result에 담아 출력'''
# def myFunction(myinput1, myinput2):
#     mysum = (myinput1 + myinput2)*2
#     return mysum

# myinput1 = int(input("입력 1 : "))
# myinput2 = int(input("입력 2 : "))
# result = myFunction(myinput1, myinput2)
# print(result)

'''list의 index 함수를 쓰지 않고 for 또는 while문을 통해
몇 번째 인덱스에 있는 값인지 print'''
# lista = [1,4,6,9]
# for a in range(len(lista)):
#     if lista[a] == 9:
#         print(f"index 번호는 {a}")
#         break

'''위의 for문을 활용해 myIndex라는 함수 생성,
input 값이 2개(list, 찾고자 하는 값), 
print는 함수 내에서 하지 않고 return에 값을 담는다'''
# lista = [1,4,6,9]
# def myIndex(myinput1, myinput2):
#     result = -1 #index는 거짓이면 -1 출력
#     for a in range(len(lista)):
#         if lista[a] == myinput2:
#             result = a
#             break
#     return result
# r1 = myIndex(lista, 9)
# print(r1)

'''함수 내에서 print'''
# lista = [1,4,6,9]
# def myIndex(myinput1, myinput2):
#     result = -1 #index는 거짓이면 -1 출력
#     for a in range(len(myinput1)):
#         if lista[a] == myinput2:
#             print(a)
#             break
# myIndex(lista, 9)