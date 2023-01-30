from PIL import Image
print('Welcome to FlyWay Bookers')

try:
    filename = Image.open("logo.jpg")
    filename.show()
    with Image.open(filename) as image:
        width, height = image.size

        print('File Found.')
except FileNotFoundError:
    print('File Not Found')


def crop_image(path, cropped_path):
    images = Image.open("logo.jpg")
    cropped = images.crop((40, 590, 979, 1500))
    cropped.save(cropped_path)
if __name__ == '__main__':
    crop_image('logo.jpg', 'logo_cropped.jpg')