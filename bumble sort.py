def bubbleSort(array):
    length = len(array)
    for i in range(length):
        isSwap = False  # Khởi tạo lại mỗi vòng lặp ngoài
        for j in range(length - 1 - i):  # Tối ưu: không cần so sánh phần đã được sắp xếp
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                isSwap = True
        if not isSwap:
            break  # Nếu không có hoán đổi, mảng đã được sắp xếp
        disp(array)

def disp(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()  # Xuống dòng sau khi in xong

array = [3, 4, 5, 6, 7, 8, 2]
print("Bubble sort:")
bubbleSort(array)