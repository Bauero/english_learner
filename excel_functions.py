def colToLetter(column: int) -> str:

    #   if the value is below 0 stop -> EXCEL uses numeration from 1
    if column <= 0:
        return None

    letters = []
    while column % 26 > 0:
        r = column % 26 
        letters.insert(0,chr(r + 64))
        column //= 26
    return "".join(letters)