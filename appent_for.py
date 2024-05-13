n=[]
v=0
s=int(input("Enter Number: "))
for i in range(0,s):
   a=int(input( "Enter number:"))
   n.append(a)
print(n)
for i in n:
    v+=i
print(v)

# n = []
# s = int(input("Enter Number: "))
# for i in range(s):
#     number = input(f"Enter number {i+1} ")
#     if number.strip():  # Check if the input is not empty
#         a = int(number)
#         n.append(a)
# print(n)