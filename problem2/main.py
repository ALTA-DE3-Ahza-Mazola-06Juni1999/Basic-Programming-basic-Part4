def draw_xyz(N): 
    pattern = ["X","Y","Z"]
    for i in range(N):
        for j in range (N):
            if (i + j) % 3 == 1:
                print(pattern[1], end ="")
            elif (i + j) % 3 == 2:
                print(pattern[2], end ="")
            elif (i + j) % 3 == 0:
                print(pattern[0], end = "")
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