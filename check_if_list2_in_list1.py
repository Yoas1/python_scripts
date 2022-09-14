with open('file1.txt', 'r') as f:
    check_list = [line.strip() for line in f]

print(check_list)

with open('file2.txt', 'r') as f:
    check_in_list = [line.strip() for line in f]

print(check_in_list)


for n in range(len(check_in_list)):
    if check_in_list[n] in check_list:
        print("yes, " + str(check_in_list[n]) + " in list")
        with open('in.txt', 'a') as f:
            f.write(check_in_list[n])
            f.write('\n')
    else:
        print(str(check_in_list[n]) + " no in list")
        with open('out.txt', 'a') as f:
            f.write(check_in_list[n])
            f.write('\n')
