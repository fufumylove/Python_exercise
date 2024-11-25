# Calculate square root of a number using math module

import math

def calculate_square_root():
    while True:
        # 获取用户输入，添加清晰的中文提示
        user_input = input("请输入一个非负数 (输入 'q' 退出程序): ")
        
        # 检查是否退出程序
        if user_input.lower() == 'q':
            print("程序已退出，谢谢使用！")
            break
            
        try:
            number = float(user_input)
            
            # 检查是否为负数
            if number < 0:
                print("错误：请输入非负数！")
            else:
                # 计算平方根并格式化输出，保留4位小数
                square_root = math.sqrt(number)
                print(f"数字 {number} 的平方根是: {square_root:.4f}")
                print(f"计算结果已四舍五入到小数点后4位")
                
        except ValueError:
            print("错误：请输入有效的数字！")
        
        print("\n" + "="*50 + "\n")  # 添加分隔线

if __name__ == "__main__":
    print("欢迎使用平方根计算器！")
    print("="*50)
    calculate_square_root()