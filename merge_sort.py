import random

def merge_sort(integer_list):
    if len(integer_list) > 1:
        # we need to find the middle of he array
        middle_point = len(integer_list) // 2

        # we split the array into 2
        array1 = integer_list[:middle_point]
        array2 = integer_list[middle_point:]

        # sort the sub_lists
        array1 = merge_sort(array1)
        array2 = merge_sort(array2)

        sorted_list = []
        while len(array1) != 0 or len(array2) != 0:
            if len(array1) == 0:
                sorted_list.append(array2[0])
                del array2[0]
            elif len(array2) == 0:
                sorted_list.append(array1[0])
                del array1[0]
            elif array1[0] <= array2[0]:
                sorted_list.append(array1[0])
                del array1[0]
            else:
                sorted_list.append(array2[0])
                del array2[0]
        return sorted_list
    else:
        return integer_list



def random_list():
    lenght = random.randint(0, 2000)
    return [random.randint(0, 10000) for i in range(lenght)]


if __name__ == '__main__':
    array = random_list()
    print("Random array generated is")
    print(array, end='\n\n\n')
    array = merge_sort(array)
    print("Sorted array is: ")
    print(array)
