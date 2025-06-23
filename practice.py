# # # # print("hello world")
# # # # print("lol")

# # # # a=5
# # # # b=7
# # # # print(a+b)
# # # # a=int(input("enter a number:"))
# # # # while(a<=5):
# # # #     print(a)
# # # #     a+=1
# # # # print("yout given number doesnot fulfill the condition")

# # # expenses=[]
# # # for i in range(5):
# # #     expense=float(input(f"Enter an expense{i+1}: "))
# # #     expenses.append(expense)
# # # print("\nYour expenses are:")
# # # for i, expense in enumerate(expenses, 1):
# # #     print(f"Expense{i}:{expense}")

# # # f=open("file.txt")
# # # data=f.read()
# # # print(data)
# # # f.close
# # a="lalalolaoalaoalal"
# # f=open("file.txt","w")
# # data=f.write(a)
# # print(data)
# # class Dog:
# #     @classmethod
# #     def create(cls, name):
# #         print(f"Creating a dog named {name}")
# #         return cls()

# # Dog.create("Tommy")
# # class Person:
# #     def __init__(self, name):
# #         self.name = name


# # # Create object
# # p = Person("Alice")
# # p.greet()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):  # Using self
#         print(f"Hello, my name is {self.name}")

#     @classmethod
#     def from_input(cls):  # Using cls
#         name = input("Enter your name: ")                                                                                                                                                                                                                                                                                                                                                                                                                     
#         return cls(name)  # same as Person(name)

# # Create object using class method
# p = Person.from_input()
# p.greet()  # From earlier method

# if __name__ == '__main__':
#     N = int(input())
#     nums = []
#     for _ in range(N):
#         command_line = input().split()
#         cmd = command_line[0]
        
#         if cmd == "insert":
#             nums.insert(int(command_line[1]), int(command_line[2]))
#         elif cmd == "print":
#             print(nums)
#         elif cmd == "remove":
#             nums.remove(int(command_line[1]))
#         elif cmd == "append":
#             nums.append(int(command_line[1]))
#         elif cmd == "sort":
#             nums.sort()
#         elif cmd == "pop":
#             nums.pop()
#         elif cmd == "reverse":
#             nums.reverse()
