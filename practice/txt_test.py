source_file_path = r"C:\Users\Benjamin\Desktop\python用.txt data\Human being.txt"

try:
    # 读取文件内容
    with open(source_file_path, 'r') as file_object:
        content = file_object.read()
        print("文件内容:\n", content)

    # 追加写入新内容
    with open(source_file_path, 'a') as file_object:
        file_object.write(' is just a shit\n')
        file_object.write('gg\n')
        print("新内容已追加。")
        print(content)

except FileNotFoundError:
    print("文件未找到，请检查路径是否正确。")
except PermissionError:
    print("权限不足，请检查文件权限或关闭占用该文件的其他程序。")
except Exception as e:
    print(f"发生错误: {e}")


