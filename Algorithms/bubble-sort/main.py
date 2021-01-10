def bubble_sort(data_set):
    while True:
        did_swap = False
        for i in range(len(data_set)-1):
            if data_set[i] > data_set[i + 1]:
                did_swap = True
                data_set[i+1], data_set[i] = data_set[i],  data_set[i+1]
        if not did_swap:
            break

    return data_set


if __name__ == "__main__":
    data_set = [1, 2, 3, 32, 22, 32, 2, 141, 2412]
    print(bubble_sort(data_set))
