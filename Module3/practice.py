# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 如果不小心進入無限迴圈 用Ctrl+C跳出迴圈
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 我寫的

print("終極密碼")
answer = 25
user_ans = int(input("請輸入你的密碼: "))


while True:
    if user_ans > answer:
        print("猜錯了![提示]請輸入更小的數字") 
        user_ans = int(input("請再試一次: "))
    elif user_ans < answer:
        print("猜錯了![提示]請輸入更大的數字") 
        user_ans = int(input("請再試一次: "))
    elif user_ans == answer:
        print("恭喜中獎")
        break
    
    









