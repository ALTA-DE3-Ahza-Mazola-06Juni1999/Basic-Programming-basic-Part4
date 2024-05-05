def play_with_asterisk(n):
    for i in range (n):
        for k in range (n-i):
            print(' ',end='')
        for j in range (i+1):
            print('* ',end='')
        print()

# Contoh penggunaan:
# draw_pyramid(5)


if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
