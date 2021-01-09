def selection_sort(data_set):
    for i in range(len(data_set)):
        min_id = i
        for j in range(i+1, len(data_set)):
            if data_set[min_id] > data_set[j]:
                min_id = j
        data_set[i], data_set[min_id] = data_set[min_id], data_set[i]

    return data_set


if __name__ == "__main__":
    data_set = [1, 2, 3, 32, 22, 32, 2, 141, 2412, 2422, 88]
    print(selection_sort(data_set))
