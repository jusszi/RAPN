
import os
print(os.getcwd())
os.chdir("./Pen")
path = "./harm"
procap = [[],[],[],[]]
prompthate = [[],[],[],[]]
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)):
        name = file.split('.')[0]
        if len(name)>3:
            thisbox = procap
        else:
            thisbox = prompthate

        with open(os.path.join(path,file), "r", encoding="utf-8") as f:
            f.seek(0,2) # 移动指针到末尾
            position = f.tell() # 获取当前文件指针位置
            count = 1

            while position >= 0:
                f.seek(position)
                char=f.read(1) # 读取一个字符

                if char == "\n" and position != f.tell():
                    if count != 0:
                        count-=1
                    else:
                        last_line = f.readline().strip()
                        left = right = 0
                        cur = 0
                        while left<len(last_line):
                            
                            if ord("0")<=ord(last_line[left])<=ord("9"):
                                right = left
                                while right!=len(last_line) and last_line[right] != ",":
                                    right+=1
                                thisbox[cur].append(last_line[right-5:right])
                                left = right-1
                                cur += 1
                            left += 1

                        print(file,last_line)
                        break
                position -= 1
print("procap:")
for item in procap:
    add = 0
    for temp in item:
        add += float(temp)
    print(add/10)
print("prompthate:")
for item in prompthate:
    add = 0
    for temp in item:
        add += float(temp)
    print(add/10)