from PIL import Image, ImageDraw


def draw_hangman(stage):
    # Tạo một hình ảnh trống với nền trắng
    img = Image.new('RGB', (200, 200), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Vẽ giá treo
    draw.line((50, 150, 150, 150), fill=(0, 0, 0), width=3)  # Đế
    draw.line((100, 50, 100, 150), fill=(0, 0, 0), width=3)  # Cột
    draw.line((50, 50, 100, 50), fill=(0, 0, 0), width=3)  # Xà ngang
    draw.line((50, 50, 50, 70), fill=(0, 0, 0), width=3)  # Dây thòng lọng

    if stage > 0:  # Vẽ đầu
        draw.ellipse((35, 70, 65, 100), outline=(0, 0, 0), width=3)
    if stage > 1:  # Vẽ thân
        draw.line((50, 100, 50, 130), fill=(0, 0, 0), width=3)
    if stage > 2:  # Vẽ tay trái
        draw.line((50, 110, 30, 120), fill=(0, 0, 0), width=3)
    if stage > 3:  # Vẽ tay phải
        draw.line((50, 110, 70, 120), fill=(0, 0, 0), width=3)
    if stage > 4:  # Vẽ chân trái
        draw.line((50, 130, 30, 150), fill=(0, 0, 0), width=3)
    if stage > 5:  # Vẽ chân phải
        draw.line((50, 130, 70, 150), fill=(0, 0, 0), width=3)

    return img


for i in range(7):
    img = draw_hangman(i)
    img.save(f'hangman{i}.png')
