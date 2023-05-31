'''function_statements3.py review'''

'''review 
재귀함수 아님(다중 for문) lista의 3개씩의 조합을 구해 리스트에 담아 출력'''
# lista = [10,20,30,40,50]
# new_list = []
# count = 0
# for a in range(len(lista)):
#     for b in range(a+1, len(lista)):
#         # new_list.append([lista[a], lista[b]])
#         for c in range(a+2, len(lista)):
#             new_list.append([lista[a], lista[b], lista[c]])
# print(new_list)

'''재귀함수화
lista의 3개씩의 조합을 구해 리스트에 담아 출력'''
# def recur(lista, total_list, temp_list, n, m):
#     if m == 0:
#         total_list.append(temp_list[:]) #list의 count값을 물어볼 경우 이 부분을 count로
#         return
#     for a in range(len(lista)):
#         temp_list.append(lista[a])
#         recur(lista, total_list, temp_list, a+1, m-1)
#         temp_list.pop()

# input1 = [10,20,30,40,50]
# total_list = []
# input2 = 3
# print(input1, total_list, [], input2)

'''class_statements.py'''

'''객체를 생성한 사칙 연산 계산기'''
# class Calculator():
#     def __init__(self):
#         self.result = 0 #초기 값 설정
#     def plus(self, a):
#         self.result += a
#     def minus(self, a):
#         self.result -= a
#     def multiply(self, a):
#         self.result *= a #초기 값 0(0*n)
#     def divide(self, a):
#         self.result /= a #초기 값 0(0/n)
# answer1 = Calculator()
# answer1.multiply(50)
# print(answer1.result) 

'''초기 값(매개 변수)설정 class
(초기 값 설정 가능)'''
# class Calculator():
#     def __init__(self, result):
#         self.result = result
#     def plus(self, a):
#         self.result += a
#     def minus(self, a):
#         self.result -= a
#     def multiply(self, a):
#         self.result *= a
#     def divide(self, a):
#         self.result /= a
# inputa = int(input("입력 값 : "))
# Calculatora = Calculator(inputa) #초기 값 설정(self와는 관계 없음)
# # Calculatora = Calculator(100)
# Calculatora.minus(10)
# print(Calculatora.result)

'''연습문제
Person이라는 클래스 생성, 생성자(__init__)로 name, age, gender, email이라는 
매개변수를 받아서 각각의 객체 변수를 생성
register 매서드를 만들고 해당 매서드에서는 myInfo라는 객체 변수에 이름,나이,성별,email 정보를 
문자열로 담는다
2명의 person을 만들어 print(p1.myInfo), print(p2.myInfo) + 오늘 날짜 추출'''
# class Person():
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.naemailme = email
#     def register(self): #객체변수를 받는다, class 동작을 위해 반드시 register가 필요한건 아님 
#         self.myInfo = (self.name, self.age, self.gender, self.naemailme)
# personal1 = Person('김재현', 26, '남', 'jehyunkim21')
# personal1.register()
# print(personal1.myInfo)

'''class의 상속 - 부모 class에서의 기능을 자식 class에서 물려받음
class 자식클래스명(부모클래스명) 형식으로 선언
본 내용은 저장된 폴더, 파일이 존재해야하는 것이므로 직접 가서 확인, 풀이'''


'''exception.py (예외 처리는 다시보기)'''


'''file_example.py(file 시스템 입/출력 라이브러리)
복잡하니 직접 가서 확인'''