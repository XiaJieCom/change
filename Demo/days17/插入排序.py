import time,random
def bubble_sort(arry):
    for i in range(1,len(array)):
        #默认从第二个元素开始
        position = i
        curent_val = array[i]
        while position > 0 and curent_val < array[position-1]:
            #如果后面的数字小于前面的
            array[position] = array[position-1]
            #把前面的小的值给后面
            position -= 1
        array[position] = curent_val
        #如果不满足上述条件,说明此时已经是最小的值




if __name__ == '__main__':

    array = [12,3,3,5,56,77,78,89,2,342,435,36,546,467,67,7,8787,87]
    # array = []
    # for i in range(10000):
    #     array.append(random.randrange(10000))
    t1 = time.time()
    bubble_sort(array)
    t2 = time.time()
    print(t1,t2)
    print(t2 - t1)
    # print(array)
