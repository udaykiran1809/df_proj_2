import os
import sys

file_header = {
    'MPG':b'\x00\x00\x01\xB3',
    "PDF": b"\x25\x50\x44\x46",
    "DOCX": b"\x50\x4B\x03\x04\x14\x00\x06\x00",
    "AVI": b"\x52\x49\x46\x46",
    "PNG": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A",
    "JPG": b"\xFF\xD8\xFF\xE0",
    "GIF": b"\x47\x49\x46\x38\x39\x61",
    "BMP": b"\x42\x4D",
    "GZ": b"\x1F\x8B\x08",
    "7Z": b"\x37\x7A\xBC\xAF\x27\x1C",
    "BZ": b"\x42\x5A\x68",
    "PKZ": b"\x50\x4B\x03\x04"
}

file_footer = {
    "MPG": b"\x00\x00\x01\xB7",
    "PDF": b"\x0A\x25\x25\x45\x4F\x46",
    "DOCX": b"\x50\x4B\x05\x06",
    "PNG": b"\x49\x45\x4E\x44\xAE\x42\x60\x82",
    "JPG": b"\xFF\xD9",
    "GIF": b"\x00\x3B",
    "GZ": None,
    "7Z": None,
    "BZ": None,
    "PKZ":"\x50\x4B\x4B"
}

def Find_loc(disk_hex):
    loc = 0
    for fh in file_header:
        fh_bytes = file_header[fh]
        loc = disk_hex.find(fh_bytes)
        print(f'{fh}: {loc}')

if __name__ == "__main__":
    with open("Project2.dd", 'rb') as disk_image:
        disk_data = disk_image.read()
    disk_image.close()
    # disk_data = str(disk_data)
    Find_loc(disk_data)
    # print(type(disk_data))
    

