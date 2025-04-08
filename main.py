import sys
import random
import pyperclip as clip
import argparse as arg
from colorama import init, Fore, Style

init()  # coloramaの初期化

VERSION = "1.0.0"

def main():
    pass_material = (("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),
                     ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"),
                     ("^", "$", "+", "-", "*", "/", "|", "(", ")", "[", "]", "{", "}", "<", ">", ".", "?", "!", "_", "=", "&", "@", "~", "%", "#", ":", ";", "'", '"'))
    sym_state = 2  # 記号を入れるか否か（2 = 入れない, 3 = 入れる）
    word_count = []  # 各pass_materialの文字数
    pass_list = []  # 結合前のパスワード

    parser = arg.ArgumentParser(description="generate password")

    parser.add_argument("arg1", help="文字数を決める場合はその数、範囲を指定したい場合は最小値", type=int)
    parser.add_argument("-r", "--rnd", help="お好みの範囲の最大値、これを指定しなかったら第一引数で指定した文字数で固定される", type=int)
    parser.add_argument("-s", "--symbols", help="記号を含めるかどうか、指定しない場合記号は含まれない", action="store_true")
    parser.add_argument("-c", "--clip", help="クリップボードに保存するかどうか", action="store_true")
    args = parser.parse_args()

    length0 = args.arg1
    length1 = args.rnd
    include_symbol = args.symbols
    strage_clip = args.clip
    
    pass_length = length0 if length1 == None else int(random.uniform(length0, length1))
    sym_state = 3 if include_symbol == True else 2
    current_count = pass_length // 2

    sub = 0
    for i in range(sym_state):
        if sym_state == 3 and i < 2:
            word_count.append(int(random.uniform(current_count//2,current_count)))
            sub = sub + word_count[i]
            continue
        elif i==0:
            word_count.append(int(random.uniform(current_count//2,current_count)))
            sub = word_count[0]
            continue
        word_count.append(pass_length - sub)

    for i in range(len(word_count)):
        for _ in range(word_count[i]):
            pass_list.append(pass_material[i][int(random.uniform(0,len(pass_material[i])))])

    random.shuffle(pass_list)

    password = "".join(pass_list)

    print(password)

    if strage_clip: 
        clip.copy(password)
        print("クリップボードにコピーしました")


if __name__ == "__main__":
    main()