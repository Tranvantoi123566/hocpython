import time 
# chuoi = "Hello, World! , tôi là hacker"
# print("Hello" in chuoi)


# ten = " hoa , trang , thảo , hương"
# while True :
#     doan = input("Nhập tên: ")
#     if doan in ten:
#         print("Tên hợp lệ.")
#         break
#     else:
#         print("Tên không hợp lệ.")

chuoi1 = "0123456789"
print(chuoi1[-1])# lấy ký tự cuối cùng
print(chuoi1[0])# lấy ký tự đầu tiên

# print(chuoi1[đầu: cuối: bước nhảy])
print(chuoi1[0:7:2])
print(chuoi1[::-1])  # Lấy tất cả ký tự nhưng đảo ngược
print(chuoi1[2:])  # Lấy từ ký tự thứ 2 đến hết
print(chuoi1[:3]) # Lấy từ đầu đến ký tự thứ 3

chuoi= input("Nhập chuỗi: ")
print(chuoi,chuoi[0],chuoi[-1])
if len(chuoi) % 2 == 0:
    print(chuoi[1:len(chuoi):2])
else:
    print(chuoi[1:len(chuoi):3])