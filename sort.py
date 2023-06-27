import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def print_iterations(arr, sort_type):
    print(f"\n{sort_type} Sort - Iterations:")
    num_iterations = len(arr)
    if num_iterations <= 10:
        for i in range(num_iterations):
            print(f"Iteration {i + 1}: {arr[i]}")
    else:
        for i in range(5):
            print(f"Iteration {i + 1}: {arr[i]}")
        print("...")
        for i in range(num_iterations - 5, num_iterations):
            print(f"Iteration {i + 1}: {arr[i]}")


def print_execution_time(execution_time):
    print(f"\nExecution Time: {execution_time} seconds")


def print_before_after(arr, sorted_arr, sort_type):
    print(f"\n{sort_type} Sort - Before:")
    print(arr)
    print(f"\n{sort_type} Sort - After:")
    print(sorted_arr)


def main():
    while True:
        arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
               26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
               17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
               40, 7, 41, 81]

        print("Silahkan pilih metode pengurutan:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Keluar")
        choice = int(input("Masukkan pilihan Anda (1/2/3): "))

        if choice == 1:
            sorted_arr, execution_time = bubble_sort(arr.copy())
            sort_type = "Bubble"
        elif choice == 2:
            sorted_arr, execution_time = insertion_sort(arr.copy())
            sort_type = "Insertion"
        elif choice == 3:
            print("Program selesai. Sampai jumpa kembali.")
            break
        else:
            print("Pilihan tidak valid.")
            continue

        print_iterations(sorted_arr, sort_type)
        print_execution_time(execution_time)
        print_before_after(arr, sorted_arr, sort_type)

        prompt = input("\nIngin keluar? (y/n): ")
        if prompt.lower() == "y":
            print("Terima kasih. Program selesai.")
            break


if __name__ == "__main__":
    main()
