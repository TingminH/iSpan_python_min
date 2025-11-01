# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
print("終極密碼")
answer = 25
while True:
# 如果不小心進入無限迴圈 用Ctrl+C跳出迴圈

# 告訴使用者需要輸入的數字範圍 input()
    user_input = int(input("請輸入1~100的數字: "))

# 超出範圍要顯示「超出範圍請重新輸入」
    if user_input < 1 or user_input > 100:
        print("超出範圍請重新輸入") 
# 數字太大 要提示「請輸入更小的數字」
    elif user_input > answer:
        print("請輸入更小的數字") 
# 數字太小 要提示「請輸入更大的數字」
    elif user_input < answer:
        print("請輸入更大的數字") 
# 使用者猜對要回傳「恭喜中獎」
    elif user_input == answer:
        print("恭喜中獎")
        break

