def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("The list length must be a multiple of 10")

    # Remove items at positions which are a multiple of 2 or 3
    # Note that list positions are zero-based, hence the off-by-one
    processed_list = [item for index, item in enumerate(input_list, start=1) if index % 2 != 0 and index % 3 != 0]

    return processed_list

def main():
    try:
        input_list = [int(item) for item in input("Enter a list of integers separated by space: ").split()]
        result = process_list(input_list)
        print("Processed list:", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
