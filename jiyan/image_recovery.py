from PIL import Image


def picture_recovery(file_path):
    img = Image.open(file_path)
    width = 260
    height = 160
    target = Image.new("RGB", (width, height))
    SEQUENCE = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,
                12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    a = height / 2
    for j in range(0, 52):
        crop_left = SEQUENCE[j] % 26 * 12 + 1
        crop_up = a if 25 < SEQUENCE[j] else 0
        crop_right = crop_left + 10
        crop_down = crop_up + 80
        crop_img = img.crop((crop_left, crop_up, crop_right, crop_down))

        left = j * 10 if j < 26 else (j - 26) * 10
        up = 0 if j < 26 else 80
        right = left + 10
        down = up + 80
        target.paste(crop_img, (left, up, right, down))
    target.save("recovery.png".format(file_path.split(".")[0]))


# picture_recovery("/Users/mac/Documents/9dba16e28.png")
picture_recovery("yuantu1.png")

