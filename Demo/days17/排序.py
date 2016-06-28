import time,random
def bubble_sort(arry):
    for i in range(len(array)):
        #首先大循环,循环整个列表
        for j in range(len(array)-1-i):#len(array)-1 表示从整个列表,再-i 就可以从下一个循环
            if array[j] > array[j+1]:
                #如果第一个值大于第二个
                tmp = array[j]
                #把第一个值给tmp
                array[j] = array[j+1]
                #把小的值给上一个
                array[j+1] = tmp
                #把tmp的值给后面的一个



if __name__ == '__main__':

    # array = [12,3,34,5,56,77,78,89,2,342,435,36,546,467,67,7,8787,87]
    array = []
    for i in range(10000):
        array.append(random.randrange(10000))
    t1 = time.time()
    bubble_sort(array)
    t2 = time.time()
    print(t1,t2)
    print(t2 - t1)
    # print(array)
