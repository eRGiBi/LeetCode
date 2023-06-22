def edit_distance(A: str, B: str) -> int:
    x = [[None] * len(A) for _ in range(len(B))]

    print(x)

    x[0][0] = 0
    for i in range(1, len(A)):
        [i][0] = x[i - 1][0] + 1
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                x[i][j] = x[i - 1][j - 1]
            else:
                ed_del = 1 + x[i - 1][j]
                ed_ins = 1 + x[i][j - 1]
                ed_rep = 1 + x[i - 1][j - 1]
                x[i][j] = min(ed_del, ed_ins, ed_rep)

    return x[len(A) - 1][len(B) - 1]


if __name__ == '__main__':
    print(edit_distance("wisdom", "intellect"))
