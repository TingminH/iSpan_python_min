# input() 函數 讓使用者在終端機輸入資料

# 取得使用者輸入的資料

user_input = input("please input a number: ")
# 使用者輸入的值會是string
# 將使用者輸入強制轉型成 int
user_input = int(user_input)
if user_input > 10:
    print("num > 10")
