# На вход поступает число n. Необходимо создать матрицу размером n x n и заполнить ее нулями.
# Далее, начиная с левого верхнего угла, необходимо спиралью заполнить матрицу единицами так,
# чтобы единицы не соприкасались, аналогично игре "морской бой".

def main():
  n = int(input())
s = [[0 for j in range(n)] for i in range(n)]
i, j, t, flag = 0, 0, 0, False
road = ((0, 1), (1, 0), (0, -1), (-1, 0))
while True:
    if 0 <= i + road[t][0] * 2 < n and 0 <= j + road[t][1] * 2 < n:
        if s[i + road[t][0] * 2][j + road[t][1] * 2] == 0:
            s[i][j] = 1
            i, j = i + road[t][0], j + road[t][1]
            flag = False
        else:
            s[i][j] = 1
            if not flag:
                t = (t+1) % 4
            else:
                break
            flag = True
    elif (t in [1,3] and (i + road[t][0] * 2 == n or i + road[t][0] == 0)) or (t in [0,2] and (j + road[t][1] * 2 == n or j + road[t][1])) == 0:
        s[i][j] = 1
        i, j = i + road[t][0], j + road[t][1]
        if not flag:
            t = (t+1) % 4
        else:
            break
        flag = True
    else: break
for i in s:
    print(i)

if __name__ == '__main__':
  main()
