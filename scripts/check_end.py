import os
import sys

# 指定目录路径
directory_path = os.path.dirname(sys.argv[0])
# directory_path = '/path/to/your/directory'

# 获取目录中的所有文件
files = os.listdir(directory_path)

all_passed = True
# 遍历文件列表
for txt_file in files:
    if txt_file.endswith('.txt'):
        # 构建对应的 vtt 文件名
        vtt_file = txt_file.replace('.txt', '.vtt')

        # 拼接完整路径
        txt_path = os.path.join(directory_path, txt_file)
        vtt_path = os.path.join(directory_path, vtt_file)

        # 打开并读取 txt 文件的最后一个字符
        with open(txt_path, 'r', encoding='utf-8') as txt_file:
            last_char_txt = txt_file.read().strip()[-2:]

        try:
            # 打开并读取 vtt 文件的最后一个字符
            with open(vtt_path, 'r', encoding='utf-8') as vtt_file:
                last_char_vtt = vtt_file.read().strip()[-1]
        except Exception as e:
            print(f"\033[31m{vtt_file} not found")
            all_passed = False
            continue

        # 进行比对或其他操作
        if last_char_vtt in last_char_txt:
            # print(f"\033[34mpassed:\t\033[0m{vtt_path}")
            pass
        else:
            print(f"\033[33mfailed:\t\033[0m{vtt_path}")
            all_passed = False

print("\033[32myes" if all_passed else "\033[31mno")
