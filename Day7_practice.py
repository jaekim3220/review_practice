'''function_statements2.py'''

'''(사용자 정의 함수)
키보드로 반지름의 길이를 입력, 
원의 넓이를 구하는 함수를 만들어 결과 출력'''
# def cirCle(a):
#     return pow(a,2)*3.14
# a = int(input("반지름 : "))
# print(cirCle(a))

'''(입력 값 없는 함수)
hello1() 호출 시 hello1 python 출럭, 
print(hello2()) 호출 시 hello2 python 출력'''
# def hello1():
#     print("hello1 python")
# def hello2():
#     return 'hello2 python'
# hello1()
# print(hello2())
# print(hello1())

'''(입력 값의 수가 정해져 있지 않고 multiple한 함수)
입력한 값을 모두 더하는 함수 함수보다 for문 사용'''
# def mysum(*nums):
#     answer = 0
#     for a in nums:
#         answer += a
#     return answer
# print(mysum(1,2,3,4,5))

'''2개 이상의 리턴 값이 있는 경우
두 값의 합, 차, 곱, 나눗셈 출력 함수'''
# def mycal(a, b):
#     answer1 = a+b
#     answer2 = a-b
#     answer3 = a*b
#     answer4 = a/b
#     return answer1,answer2,answer3,answer4
# a = int(input("1번 "))
# b = int(input("2번 "))
# callvalue = mycal(a, b)
# print(f"첫 번째 값 : {callvalue[0]}")

'''default 값 미리 세팅 전'''
# def myCall(a, b, c):
#     if c == 'plus':
#         result = a+b
#     elif c == 'min':
#         result = a-b
#     elif c == 'multi':
#         result = a*b
#     return result
# result1 = myCall(5, 1, 'plus')
# result2 = myCall(5, 1, 'min')
# result3 = myCall(5, 1, 'multi')
# print(f"덧셈 : {result1}, 뺄셈 : {result2}, 곱셈 : {result3}")

'''default 값 미리 세팅 후
다른 default 값 진행 시 앞의 default 값 덮어쓰기 후 동작'''
# def myCall(a, b, c='plus'):
#     if c == 'plus':
#         result = a+b
#     elif c == 'min':
#         result = a-b
#     elif c == 'multi':
#         result = a*b
#     return result
# result1 = myCall(5, 1)
# result2 = myCall(5, 1, 'min')
# result3 = myCall(5, 1, 'multi')
# print(f"덧셈 : {result1}, 뺄셈 : {result2}, 곱셈 : {result3}")

'''매개변수 input의 순서를 맞추지 않아도
원하는 매개변수 자리에 값을 넣어 함수 호출'''
# def spec(name, age, sex):
#     print(f"이름 : {name}, 나이 : {age}, 성별 : {sex}")
# spec(age = 26, name = '김재현', sex = '남')

'''유용한 기능 end'''
# print(input("입력 : "), end = ' : 안녕')

'''전역/지역변수'''
# a = 100 #전역변수
# def sum(a,b): #지역변수
#     #여기서 a 값은 100인가 10인가?
#     #전역변수인 a=100보다, 함수내에서 선언한 a=10을 우선 인식
#     result = a+b
#     return result
# result = sum(10,20)
# print(result) 
# #함수내의 result라는 변수는 함수 밖에서는 인식 불가
# #result를 print 가능한 이유는 함수내에서 어떤 값을 return 했기 때문
# print(a)

'''함수내에서 전역변수에 영향을 끼치는 방법(global)'''
# result = 0
# def sum(a):
#     global result #존재유무 확인해볼 것(없으면 에러, 이를 통해 global의 역할 확인)
#     result += a
#     return result
# value = sum(10)
# print(value)

'''2중 for문 사용 시 변수에 주의'''
# lista = [10,20,30,40]
# for a in range(len(lista)):
#     for a in range(len(lista)):
#         print(a)
#         print('\n')
#         print(a)

'''선택 함수화
Day6_practice.py for문을 이용한 정렬 알고리즘(sort 미사용)참고'''
# def mySort(lista):  
#     for a in range(len(lista)-1):
#         for b in range(a+1, len(lista)):
#             if lista[a] > lista[b]:
#                 temp = lista[a]
#                 lista[a] = lista[b]
#                 lista[b] = temp
# lst = [56,78,-21,12,5,89,2,-54,87] 
# #객체는 함수 내에서 원본변경 가능 return 선택, 객체 아닌건 함수 내에서 원본변경 불가 return 필수
# mySort(lst)
# #return 필요 없음(lst 값이 아닌 lst의 메모리 주소를 전달), 원본을 바꿀 경우 return 필요
# print(lst)

