def draw_xyz(N):
    pattern = ["X", "Y", "Z"]
    for i in range(N):
        for j in range(N):
            if (i * N + j + 1) % 3 == 0:
                print(pattern[0], end=" ")
            elif (i * N + j + 1) % 2 == 0:
                print(pattern[2], end=" ")
            else:
                print(pattern[1], end=" ")
        print()

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """

    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """