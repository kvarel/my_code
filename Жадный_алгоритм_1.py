def main():
    s = sorted([list(map(int, input().split())) for _ in range(int(input()))], key= lambda x: x[1])
    s1 = [s[0][1]]
    for i in s:
        if i[0] >= s1[-1]:
            s1.append(i[1])
    print(len(s1), ' '.join([str(i) for i in s1]), sep= '\n')

if __name__ == '__main__':
    main()
