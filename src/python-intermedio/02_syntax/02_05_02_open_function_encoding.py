# https://python-intermedio.readthedocs.io/es/latest/open_function.html

import io

if __name__ == '__main__':
    file_name_photo_jpg = 'photo-01'
    file_name_photo_png = 'photo-02'
    file_name_text = 'test-03.txt'

    print('=== Open JPEG image ===')
    # Read the file as binary data.
    with open(file_name_photo_jpg, 'rb') as f_photo:
        jpg_data = f_photo.read()

    # Check if the file is a JPEG.
    if jpg_data.startswith(b'\xff\xd8'):
        text = u'It is a JPEG image (%d bytes long) it starts with: 0x%x 0x%x\n'
    else:
        text = u'It is not a JPEG image (%d bytes long) it starts with: 0x%x 0x%x\n'

    # Write the result to a text file.
    with io.open(file_name_text, 'w', encoding='utf-8') as f_text:
        message = text % (len(jpg_data), jpg_data[0], jpg_data[1])
        f_text.write(message)
        print(message, end='')

    print()
    print('=== Open PNG image ===')
    # Read the file as binary data.
    with open(file_name_photo_png, 'rb') as f_photo:
        jpg_data = f_photo.read()

    # Check if the file is a JPEG.
    if jpg_data.startswith(b'\xff\xd8'):
        text = u'It is a JPEG image (%d bytes long) it starts with: 0x%x 0x%x\n'
    else:
        text = u'It is not a JPEG image (%d bytes long) it starts with: 0x%x 0x%x\n'

    # Write the result to a text file.
    with io.open(file_name_text, 'a', encoding='utf-8') as f_text:
        message = text % (len(jpg_data), jpg_data[0], jpg_data[1])
        f_text.write(message)
        print(message, end='')
