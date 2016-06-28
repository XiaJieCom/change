import time,random
def bubble_sort(arry):
    for i in range(len(array)):
        small_index = i
        #首先大循环,循环整个列表
        for j in range(i,len(array)):
            if array[small_index] > array[j]:
                small_index = j
            tmp = array[i]
            array[i] = array[small_index]
            array[small_index] = tmp




if __name__ == '__main__':

    #array = [12,3,34,5,56,77,78,89,2,342,435,36,546,467,67,7,8787,87]
    array = []
    for i in range(50000):
        array.append(random.randrange(50000))
    t1 = time.time()
    bubble_sort(array)
    t2 = time.time()
    print(t1,t2)
    print(t2 - t1)
    # print(array)


