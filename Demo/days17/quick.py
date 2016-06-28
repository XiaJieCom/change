import time,random
def quick_sort(arry,start,end):
    print('-->',start,end)
    if start >= end:
        return
    k = array[start]
    left_flag = start
    right_flag = end
    while left_flag < right_flag:
        while left_flag < right_flag and array[right_flag] > k:
            right_flag -= 1
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp

        while left_flag < right_flag and array[left_flag] <= k:
            left_flag += 1
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp
        print(array,left_flag,right_flag)

    quick_sort(array,start,left_flag-1)
    quick_sort(array,left_flag+1,end)

if __name__ == '__main__':

    array = [12,4,9,10,6,3,5]
    # array = []
    # for i in range(100000):
    #     array.append(random.randrange(50000))
    t1 = time.time()
    quick_sort(array,0,len(array)-1)
    t2 = time.time()
    print(t1,t2)
    print(t2 - t1)
    # print(array)
