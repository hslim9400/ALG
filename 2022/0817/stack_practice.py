class Stack:  # 클래스 생성
    def __init__(self):  # 파이썬 list로 데이터를 담을 바구니를 만든다.
        self.basket = []

    def push(self, data):  # Stack의 행동은 push와 pop
        self.basket.append(data)

    def pop(self):  # 먼저 들어온 데이터가 나중에 나간다.
        return self.basket.pop()


bag = Stack()
bag.push(1)
bag.push('asdf')
bag.push([1,2,3])
print(bag.pop())
print(bag.pop())
print(bag.pop())