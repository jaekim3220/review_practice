'''!dictionary.py'''

'''comprehension example'''
# product_list = ["풀", "가위", "크래파스"]
# price_list = [800, 2500, 5000]
# product_dic = {product_list : price_list \
#                for product_list, price_list in zip(product_list, price_list)}
# print(product_dic)
'''for문을 사용해 key 값, value 값이 담긴 list 생성 1'''
# dic = {'one' : 1, 'two' : 2}
# keyList = dic.keys()
# key_value_list = []
# for k in keyList:
#     key_value_list.append((k, dic[k]))
# print(key_value_list)
'''key을 출력해주는 for문 안에서 value도 같이 출력 1'''
# dic1 = {'one' : 1, 'two' : 2}
# for k,v in dic1.items():
#     print("key 값 : {}, value 값 : {}".format(k,v))
'''리스트를 딕셔너리로 변환'''
# lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
# dica = {}
# for a in lista:
#     if a not in dica.keys():
#         dica[a] = lista.count(a)
# print(dica)
'''완주하지 못한 선수'''
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# for person in participant:
#     if person in completion:
#         completion.remove(person)
#     else:
#         print(person)

'''!list_string_statements.py'''

'''특정 값 삭제 list'''
# listb=[]
# lista = [1,9,3,4,9,6,7,8,9]
# for n in range(0, len(lista)):
#     if lista[n] != 9:
#         listb.append(lista[n])
# print(listb)
'''홀짝'''
# a = int(input("입력 값 : "))
# print(f"{a}는 짝수") if a %2 ==0 else print(f"{a}는 홀수")
'''리스트 병합'''
# lista = ['hello', 'world', 'python']
# st1 = ' '.join(lista)
# print(st1) 
'''문자열 -> 리스트, 리스트 -> 문자열'''
# lista = ['hello', 'world', 'python']
# print(''.join(lista))
# sta = 'hello world python'
# mysta1 = list(sta)
# mysta2 = sta.split()
# print(mysta1)
# print(mysta2)

'''!set_statements.py 넘어감(다시 보기만)'''

'''!tuple.py 넘어감(다시 보기만)'''

'''if_statements.py 넘어감(다시 보기만)'''

'''string_calculators.py'''

'''특정 단어 출력 (for)'''
# a = "python's fun python's fun python's fun python's fun"
# for char in a:
#     if char == 'p':
#         print(char)

'''특정 단어 출력 (if)'''
# a = "python's fun python's fun python's fun python's fun"
# for char in a:
#     if char != 'p':
#         continue
#     print(char)



