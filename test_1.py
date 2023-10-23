import os
import sys
import math

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
        if loc%512 == 0:
            print(f'{fh}: {loc}')


def FileRecovery(disk_hex):
    loc = 0
    s_loc = 0
    total_found = 0
    for fh in file_header:
        fh_bytes = file_header[fh]
        loc = disk_hex.find(fh_bytes)
        if fh == 'JPG':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer['JPG'], loc)
                file_name = 'File' + str(total_found)+ '.jpg'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                print(start_offset, end_offset, filesize)
                print(ff_loc)
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                s_loc = loc+8
                    # print("Not found")
        elif fh == 'MPG':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["MPG"], loc)
                file_name = 'File' + str(total_found)+ '.mpg'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass
        elif fh == 'PDF':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["PDF"], loc)
                file_name = 'File' + str(total_found)+ '.pdf'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'DOCX':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["DOCX"], loc)
                file_name = 'File' + str(total_found)+ '.docx'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'avi':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["avi"], loc)
                file_name = 'File' + str(total_found)+ '.avi'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'AVI':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["AVI"], loc)
                file_name = 'File' + str(total_found)+ '.avi'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'PNG':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["PNG"], loc)
                file_name = 'File' + str(total_found)+ '.png'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'GIF':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["GIF"], loc)
                file_name = 'File' + str(total_found)+ '.gif'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        elif fh == 'BMP':
            if loc%512 == 0:
                total_found = total_found + 1
                ff_loc = disk_hex.find(file_footer["BMP"], loc)
                file_name = 'File' + str(total_found)+ '.bmp'
                start_offset = int(loc/2)
                end_offset = int(math.ceil(ff_loc/2))
                filesize = end_offset - start_offset
                # extract function
                File_Extract(start_offset,filesize,file_name)
            else:
                # need to write logic for else
                pass

        # Need to write logic for zip 

def File_Extract(start_offset,count, file_name):
    extraction_command = 'dd if =Project2.dd of=' + str(file_name) + ' bs=1 skip=' + str(start_offset) + ' count='+ str(count)
    os.system(extraction_command)


if __name__ == "__main__":
    with open("Project2.dd", 'rb') as disk_image:
        disk_data = disk_image.read()
    disk_image.close()
    # disk_data = str(disk_data)
    # Find_loc(disk_data)
    FileRecovery(disk_data)
    # print(disk_data)
    # print(type(disk_data))
    