# even_odd.py (プロ版)

def get_judge_text(num):
    """入力された数値を判定し、履歴用の文字列を作成する"""
    if num % 2 == 0:
        return f"{num}(偶数)"
    else:
        return f"{num}(奇数)"
    
def get_judge_text_sos(num):

    return num / 2

def main():
    """メインのループ処理を行う関数"""
    history = []
    print("--- 判定マシン (DocString実装版) ---")

    while True:
        user_input = input("\n数字を入力 ('q'で終了): ")
        if user_input.lower() == 'q':
            break

        try:
            val = int(user_input)
            result = get_judge_text_sos(val) # 関数を呼び出す
            print(f"結果: {result}")
            history.append(result)
        except ValueError:
            print("エラー: 数字を入れてね")

    print("\n履歴を表示します...")
    for h in history:
        print(h)

if __name__ == "__main__":
    main()
