from collections import deque

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    queue = deque(s)
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
