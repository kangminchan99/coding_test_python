def solution(picture, k):
    # 원본 그림 파일의 행과 열의 개수를 구합니다.
    rows = len(picture)
    cols = len(picture[0])

    # 가로와 세로를 k배로 늘린 행과 열의 개수를 계산합니다.
    new_rows = rows * k
    new_cols = cols * k

    # 새로운 그림 파일을 담을 리스트를 생성합니다.
    new_picture = []

    # 원본 그림 파일을 k배로 늘립니다.
    for row in picture:
        new_row = ''
        for pixel in row:
            new_row += pixel * k
        new_picture.extend([new_row] * k)

    return new_picture