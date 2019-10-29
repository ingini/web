class Person(): #클래스 (집단)
    name = '사람의 고유한 속성' #멤버 변수(속성)
    age = '출생 이후부터 삶을 마감할때 까지의 기간'

    def greeting(self): # 멤버 메서드 (행동)
        print(f'{self.name}이 인사합니다. ㅎㅇ')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

daegeon = Person() #인스턴스 생성

print(daegeon.name)
print(daegeon.age)

daegeon.name = 'daegeon'
daegeon.age = '27'

print(daegeon.name)
print(daegeon.age)

daegeon.greeting()

