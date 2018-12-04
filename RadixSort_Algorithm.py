def radix_sort(arr):
    arr_int_type = list(map(int, arr))
    # 確認最大樹的digit數
    digit_num = len(str(max(arr_int_type)))
    print('max is ', max(arr_int_type))
    print('digit_num is ', digit_num)
    for i in range(digit_num)[::-1]:
        bucket = [[], [], [], [], [], [], [], [], [], []]
        temp = list()
        for target in arr:
            # 先確認有無需要補0
            if len(target) != digit_num:
                for x in range(digit_num-len(target)):
                    target = '0' + target

            bucket[int(target[i])].append(target)

        # 將bucket中值取出，把arr洗掉
        for x in range(len(bucket)):
            for y in bucket[x]:
                temp.append(y)
        for m in range(len(temp)):
            arr[m] = temp[m]

        # 將補上去的0去除
        for clean in arr:
            index = arr.index(clean)
            while (clean[0] == '0') and (len(clean) != 1):
                clean = clean[1:]
            arr[index] = clean

        print(" ".join(str(i) for i in arr))


arr_num = input("欲排列數字個數：")
target_arr = input("輸入欲排列數字(以空白鍵分隔)：").split(' ')
radix_sort(target_arr)
