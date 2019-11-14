i = 0

while i < 10:

    if i == 3:
        # 注意：循环中使用continue时
        # 需要在在该关键字之前确认循环的技术是否修改
        # 否则会出现死循环
        i += 1
        continue

    print(i)

    i += 1
