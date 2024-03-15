

# ĐỀBÀI: Nhập vào số m, tính tổng các số chẵn từ 1 to m và in ra tổng đó.

"""
m=int(input("Nhap so m: "))
tong=0

print("Các số chẵn từ 1 đến", m, "là: ")
for i in range(1, m + 1):  # Duyệt qua các số từ 1 đến m
    if i % 2 == 0:  # Kiểm tra xem số hiện tại có phải là số chẵn không
        print(i)  # In số chẵn

# In tổng các số chẵn
print("tổng các số chẵn là: ",tong)
for i in range(2, m+1, 2):
    tong = tong + i

"""

"""m=int(input("Nhập vào số m: "))
tong=0

print("Các Số chẵn từ 1 đến",m, "là: ")
for i in range(1, m + 1):
    if i % 2 == 0:
       print(i)


for i in range(2, m+1, 2):
    tong = tong + i
print("tổng các số chẵn tìm được ở trên là: ",tong)"""





#ĐềBài: Nhập vào số n, tính và in ra n! (giai thừa)
"""
def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)

n = int(input("Nhập vào số n: "))
result = tinh_giai_thua(n)
print(f"{n}! =", result)

# def tinh_giai_thua(n): Định nghĩa một hàm tinh_giai_thua() để tính giai thừa của số n.
# Trong hàm tinh_giai_thua(), nếu n bằng 0, trả về 1 vì 0! = 1.
# Nếu n không bằng 0, hàm sẽ gọi đệ quy để tính giai thừa của n - 1 và nhân với n.
# n = int(input("Nhập vào số n: ")): Yêu cầu người dùng nhập vào số n.
# result = tinh_giai_thua(n): Gọi hàm tinh_giai_thua() với đối số n và gán kết quả vào biến result.
# print(f"{n}! =", result): In ra kết quả của giai thừa n.

"""
#ĐèBài: Viết chương trình nhập số nguyên dương n, in ra tất cả các ước của n.
"""
n=int(input("Nhập vào số nguyên dương n:"))

print(f"các ước của {n} là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

"""
# Đề bài: Viết ra chương trình nhập vào số nguyên dương n, tính tổng tất cả các ước của n.


"""
n=int(input("Nhập vào số nguyên dương n: "))
total = 0

print(f"các ước của {n} là: ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        total += i

print (f"tổng các ước của {n} là: ", total)

"""

#cách2
"""
n=int(input("Nhập vào số nguyên dương n: "))
mang = []


for i in range(1, n + 1):
    if n % i == 0:
        mang.append(i)

print(f"các ước của {n} là: ",mang)
print (f"tổng các ước của {n} là: ",sum(mang))

"""
# ĐềBài: Với một số đã có sẵn, player nhập vào số để dựng đoán, nếu đoán đúng với số đã có sẵn thì print "Yu won",
# ngược lại player nhập lại tối đa 3 lần, vẫn kh đoán đc thì print "Yu lose".

"""
turn = 3
lucky_num = 6

while turn > 0:
    n = int(input("text your lucky number: "))
    if n == lucky_num:
        print("You Win !!")
        break
    else:
        print("Opss you Lose :(( ")
        turn -= 1
        if turn == 0:
            print("Better luck next time <3")
"""
# Đề bài: tìm tất cả các số trog đoạn từ 10 to 200 (gồm cả 2 số 10, 200) chia hết cho 7 nhưng không chia hết cho 5.

"""arr = []

for i in range(10,201):
        if i % 7 == 0 and i % 5 != 0:
            arr.append(i)
print("Các số trong khoảng từ 10 đến 200 chia hết cho 7 và không chia hết cho 5 là:",arr)"""

"""
arr = [] 
for i in range(10,201):
     if i % 7 == 0 and i % 5 != 0:
         arr.append(i)
print("các số trong khoảng từ 10 to 200 là:", arr)

"""

#Đề bài: Viết chươg trình liệt kê các số nguyên tố nhỏ hơn n, số nguyên dương n nhập từ keyboard

"""
n = int(input("Nhập vào số nguyên dương n: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Các số nguyên tố nhỏ hơn {n} là:")
for i in range(2, n):
    if is_prime(i):
        print(i, end=" ")

"""



#Đề bài: nhập vào một số, kiểm tra số nhập vào có phải là số đối xưng không.
        
"""
def SoDoiXung(n): 
    flag =0
    if ( n[::-1] == n):
      flag = 1
    return flag


n = input("Nhập vào n: ")
check = SoDoiXung(n)
 
if check == 1:
    print(n,"Là số đối xứng")
else:
    print(n,"Không phải số đối xứng")

"""
#Đề bài:nhạp vào 2 chuỗi, in ra chuỗi có độ dài lớn hơn.

"""
string_num1 = input("Nhập vào chuỗi thứ nhất: ")
string_num2 = input("Nhập vào chuỗi thứ hai: ")

if len(string_num1) > len(string_num2):
    print(f"Chuỗi dài hơn là: {string_num1}")
elif len(string_num2) > len(string_num1):
    print(f"Chuỗi dài hơn là: {string_num2}")
else:
    print("Hai chuỗi có độ dài bằng nhau ")

"""

#Đề bài buổi2 /13/03/2024: viết hàm tính tổng từ 1 to n, với n đc nhập vào từ keyboard.

"""
n=int(input("nhập vào n: "))
arr = []

def ham(**kwargs):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

for i in range(1, n + 1):
    arr.append(i)

print(f"các số từ 1 đến {n} là: ",arr)
print(f"kết quả tính tổng các số từ 1 đến {n} là:",ham())

"""


#Đề bài buổi2 /13/03/2024: tính dãy số fibonaci theo côg thức

"""
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]

n = int(input("nhap vào số n: "))
print(f"F({n}) = ", fibonacci(n))
"""
#Đề bài buổi2 /13/03/2024: Viết chươg trình tính: F(n)=F(n-1)+100 (khi n > 0)
#                          khi n = 0, thì F(0)=0,
#                          với n là số được nhập vào (n >= 0).
"""
def F(n):
    if n == 0:
        return 0
    return 100 + F(n-1)

n = int(input("Nhập số nguyên dương n: "))
print("Kết quả là: ", F(n))
"""
#Đề bài buổi2 /13/03/2024: lấy link yt.


"""
string = "https://www.youtube.com/watch?v=q3ts3TjWHsY"
print(string.split("/")[3].split("=")[1])

"""


#Bài tập string:
#bai1:

"""
age = 222
str = "tom {} year old "
print(f"{str} {age}")
print(str.format(age))

"""


def reverse_string(si):
    return si[::-1]

s = input("nhập vào chuỗi: ")
print(reverse_string(s))

#bai2




