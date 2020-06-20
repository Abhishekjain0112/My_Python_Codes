def count_substring(string, sub_string):
    count = 0
    sl = len(sub_string)
    for i in range(len(string) - sl + 1):
        if string.find(sub_string, i, i + sl) != -1:
            count = count + 1
            # print(string.find(sub_string,i, i+sl))

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)