from typing import Any;

class FixedQueue:
    class Empty(Exception):
        pass;
    class Full(Exception):
        pass;

def __init__(self, capacity: int) -> None:
    self.no = 0; # 現在のデータ数
    self.front = 0; # 先頭要素カーネル
    self.rear = 0; # 末尾要素カーネル
    self.capacity = capacity; # キューの容量
    self.que = [None] * capacity; # キューの本体

def __len__(self) -> int:
    return self.no; # 

def is_empty(self) -> bool:
    return self.no <= 0; # データ数が空

def is_full(self) -> bool:
    return self.no >= self.capacity; # データ数が超える

def enque(self, x: Any) -> None:
    if self.is_full():
        raise FixedQueue.Full;
    self.que[self.rear] = x;
    self.rear += 1;
    self.no += 1;
    if self.rear == self.capacity:
        self.rear = 0;

def deque(self) -> Any:
    if self.is_empty():
        raise FixedQueue.Empty;
    x = self.que[self.front];
    self.front += 1;
    self.no -= 1;
    if self.front == self.capacity:
        self.front = 0;
    return x;
