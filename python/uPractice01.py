# 사람 이름 받아와서 삭제하는 메소드 하나 만들기  O
# 모든 사람들의 나이를 1살씩 더하는 메소드 만들기 O
# 하나 생각해서 알아서 만들기                   
# 현재 있는 메소드
# 휴대폰 번호 업데이트, 나이 업데이트, 사람 삭제
# 검색을 만드는 것으로 결정

class Address:
    def __init__(self, str1, str2, str3, num):
        self.name = str1
        self.phone = str2
        self.res = str3
        self.age = num
    def show(self):
        print(self.name, self.phone, self.res, self.age)
    def updatePhone(self, newPhone):
        self.phone = newPhone
    def updateAge(self):
        self.age += 1


class Book:
    def __init__(self):
        self.list = []

    def add(self, addr):
        self.list.append(addr)

    def show(self):
        for x in self.list:
            x.show()
    def updatePhone(self, name, phone):
        for x in self.list:
            if x.name == name:
                x.updatePhone(phone)
                break
    def delete(self, name):
        for x in self.list:
            if x.name == name:
                self.list.remove(x)
    def updateAge(self):
        for x in self.list:
            x.updateAge()
    def find(self, name):
        for x in self.list:
            if name in x.name:
                x.show()
add = Address ('김성현', '010-9246-1739', 'suwon', 17)
add1 = Address('김영훈', '010-0000-0000', 'hawseong', 18)
add3 = Address('안현석', '010-9246-1739', 'suwon', 17)
add4 = Address('이현석', '010-0000-0000', 'hawseong', 18)
book = Book()
book.add(add)
book.add(add1)
book.add(add3)
book.add(add4)
book.show()
print('------------------')
book.updateAge()
book.show()
# print('------------------')
# book.delete('김영훈')
# book.show()
print('------------------')
book.find('김성현')
print(digit, "는 ", cnt, '번 들어있습니다.')