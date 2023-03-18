# python3


def build_heap(data):
    swaps = []
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    n = len(data)
    for i in range(n // 2, -1, -1):
        j = i
        while j * 2 + 1 < n:
            k = j * 2 + 1
            if k + 1 < n and data[k + 1] < data[k]:
                k += 1
            if data[j] > data[k]:
                swaps.append((j, k))
                data[j], data[k] = data[k], data[j]
                j = k
            else:
                break
    return swaps

def main():
        
    # TODO : add input and corresponding checks
    # add another input for I or F 
    text = str(input())
    
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in text:
        filename = str(input())
        if 'a' in filename:
            print("Invalid filename")
            exit()
        filename = "test/" + filename
        with open(filename, 'r') as file:
            n = int(file.readline())
            data = [int(x) for x in file.readline().split()]
            
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    
    # calls function to assess the data 
    swaps = build_heap(data)
    # and give back all swaps
    
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
