def binarysearch(data, target, low, high):
    if low >= high:
        return False
    else:
        mid = (low + high)//2
        if data[mid]==target:
            return True
        else:
            if data[mid] > target:
                return binarysearch(data, target, low, mid-1)
            else:
                return binarysearch(data, target, mid+1, high)


if __name__ == "__main__":
    L=[2,3,4,5,7,9,15]
    binarysearch(L, 5, 0, 4)
