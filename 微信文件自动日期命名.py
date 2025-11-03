import sys
import os
from datetime import date
import shutil

def main():
    if len(sys.argv) < 2:
        print("请将文件拖放到本程序上。")
        input("按回车键退出...")
        return

    # 固定保存路径
    target_folder = r"E:\博士\磊的生活日\2025年11月"
    os.makedirs(target_folder, exist_ok=True)  # 确保文件夹存在

    # 中文日期
    today = date.today().strftime("%Y年%m月%d日")

    # 获取已有编号
    existing_numbers = []
    for f in os.listdir(target_folder):
        name, ext = os.path.splitext(f)
        if name.startswith(today) and '(' in name and ')' in name:
            try:
                num = int(name.split('(')[-1].split(')')[0])
                existing_numbers.append(num)
            except:
                pass

    counter = max(existing_numbers) + 1 if existing_numbers else 1

    # 处理拖入的每个文件
    for filepath in sys.argv[1:]:
        if not os.path.isfile(filepath):
            print(f"⚠️ 跳过：{filepath}（不是文件）")
            continue

        ext = os.path.splitext(filepath)[1]
        new_name = os.path.join(target_folder, f"{today} ({counter}){ext}")

        print("─────────────────────────────")
        print(f"📄 原文件路径：{filepath}")
        shutil.move(filepath, new_name)  # 移动到目标文件夹
        print(f"✅ 新文件路径：{new_name}")
        print("─────────────────────────────\n")

        counter += 1

    input("🎉 操作完成。按回车键退出...")

if __name__ == "__main__":
    main()
