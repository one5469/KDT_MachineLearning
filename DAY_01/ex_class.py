# 클래스 생성 (1)
# - 구성 요소 : 속성 + 메소드 => 모두 없는 클래스
# - 기본 상속 : Object ==> __속성명__, __메소드명__()
class A:
    pass

# 객체/인스턴스 생성
# => 생성 함수: 클래스이름()
# => A()

a1 = A()

# 객체/인스턴스의 속성/메소드 사용
# => 사용 방법 : 객체/인스턴스 변수명.속성
#               객체/인스턴스 변수명.메소드()
print("A 인스턴스 a1의 속성과 메소드 => ", a1.__dict__)
print("A 클래스의 속성과 메소드      => ", a1.__dir__())
# print("A 클래스의 속성과 메소드      => ", A.__dir__())

a1.__dir__()

# 클래스 생성 (2)
# - 구성 요소 : 속성 + 메소드 => 인스턴스 변수와 메소드
# - 기본 상속 : Object ==> __속성명__, __메소드명__()
class B:

    # 인스턴스 객체 생성 및 속성 초기화 메소드
    def __init__(self, num, name):
        # self로 지정된 힙 메모리 주소에서 부터 속성 저장
        self.num = num
        self.name = name

    # 인스턴스 메소드
    def printInfo(self):
        print(f'num  : {self.num}'
              f'name : {self.name}')

    # 연산자 맵핑 메소드 구현
    def __add__(self, other):
        print('__add__')
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

# 객체/인스턴스 생성
# => 생성 함수: 클래스이름(__init__메소드 매개변수)
# => A()
b1 = B(100, 'BB')
b2 = B(30, 'BBB')

# 객체/인스턴스의 속성/메소드 사용
# => 사용 방법 : 객체/인스턴스 변수명.속성
#               객체/인스턴스 변수명.메소드()
print("B 인스턴스 b1의 속성과 메소드 => ", b1.__dict__)
print("B 인스턴스 b1의 속성과 메소드 => ", b1.__dir__())
print("B 클래스의 속성과 메소드      => ", B.__dict__)

# 클래스 생성 (3)
# - 구성 요소 : 속성 + 메소드 => 인스턴스 변수와 메소드, 클래스 변수
# - 기본 상속 : Object ==> __속성명__, __메소드명__()
class C:
    # 클래스 변수 => c 클래스로 생성된 모든 인스턴스에서 공유
    loc = 0

    def __init__(self, num, name):
        # self로 지정된 힙 메모리 주소에서 부터 속성 저장
        self.num = num
        self.name = name

    # 인스턴스 메소드
    def printInfo(self):
        print(f'num  : {self.num}'
              f'name : {self.name}')

# 객체/인스턴스 생성
# => 생성 함수: 클래스이름(__init__메소드 매개변수)
# => A()
c1 = C(1000, name='CCC')

# 인스턴스 메소드 사용
c1.printInfo()

# 인스턴스 속성 사용
print(c1.name)

# 클래스 속성 사용
print(C.loc)

# 클래스 생성 (4)
# - 구성 요소 : 속성 + 메소드 => 인스턴스 변수와 메소드, 클래스 변수
# - 기본 상속 : Object ==> __속성명__, __메소드명__()
class DCalc:
    # 클래스 변수 => 클래스로 생성된 모든 인스턴스에서 공유
    #           => 인스턴스 생성 없이 사용 가능
    name = 'CASIO'

    # 클래스 메소드
    @classmethod
    def addNum(cls, a, b):
        return a + b

    def minusNum(cls, a, b):
        return a - b

d1 = DCalc()

# 객체/인스턴스의 연산

print(b1+b2)
print(b1-b2)