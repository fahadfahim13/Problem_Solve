class MergeSort:
    def merge(self, left_arr, right_arr, arr):
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                k += 1
                j += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1

        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            arr1 = arr[:len(arr) // 2]
            arr2 = arr[len(arr) // 2:]
            self.merge_sort(arr1)
            self.merge_sort(arr2)
            self.merge(arr1, arr2, arr)


if __name__ == '__main__':
    arr = [23, 13, 5, 16, 3, 2, 1, 10, 9]
    merge_sort = MergeSort()
    merge_sort.merge_sort(arr)
    print(arr)