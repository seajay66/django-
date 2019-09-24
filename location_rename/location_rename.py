import os
import exifread
import time
import re
import requests
import json
import shutil

# 经纬度格式转换为小数
def convert(*arg):
    """
    经纬度转为小数, param arg:
    :return: 十进制小数
    """
    return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

#经纬度转为城市区县
def geocode_to_city(lng,lat):
    url = 'https://apis.map.qq.com/jsapi?qt=rgeoc&lnglat={0}%2C{1}'.format(lat,lng)
    response = requests.get(url)
    result = response.json()
    city = result['detail']['results'][0]['c']+ result['detail']['results'][0]['d']
    return city

#把时间戳转化为时间: 1479264792  to    2016 - 11 - 16    10: 53:12
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    # return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
    return time.strftime('%Y-%m-%d',timeStruct)

# 根据一个类似 D：/a.txt的绝对文件路径进行对文件重命名。包含拍摄地点及时间信息，如无拍摄时间，则用修改时间代替，输出结果信息。
def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    print(tags)
    fd.close()
    #注意new_names 路径应该加上dirpath与斜杠。rename函数是可以附带并识别路径的。
    if FIELD in tags:
        GPS = {}
        for tag, value in tags.items():
            if re.match('GPS GPSLatitudeRef', tag):
                GPS['GPSLatitudeRef'] = str(value)  # -->  (0x0001) ASCII=N @ 811
            elif re.match('GPS GPSLongitudeRef', tag):
                GPS['GPSLongitudeRef'] = str(value)  # -->  (0x0003) ASCII=E @ 835
            elif re.match('GPS GPSAltitudeRef', tag):
                GPS['GPSAltitudeRef'] = str(value)  # -->  (0x0005) Byte=0 @ 859
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLatitude'] = convert(deg, min, sec)
            elif re.match('GPS GPSLongitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLongitude'] = convert(deg, min, sec)
            elif re.match('GPS GPSAltitude', tag):
                GPS['GPSAltitude'] = str(value)
            elif re.match('.*Date.*', tag):
                date = str(value)
        print(GPS)
        try:
            city = geocode_to_city(GPS['GPSLatitude'], GPS['GPSLongitude'])
            # print(str(tags[FIELD]))
            new_name = dirpath+"/"+str(tags[FIELD]).replace(':', '年',1).replace(':', '月',1).replace(' ', '日').replace(':', '点',1).replace(':', '分')
            new_name = new_name+ "秒摄于"+city+ os.path.splitext(filename)[1]
            os.rename(filename, new_name)
            # print(filename_1,"修改为",new_name,"修改成功")
        except KeyError:
            mtime = os.stat(filename).st_mtime
            file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
            new_name = dirpath+"/"+ file_modify_time.replace('-', '年',1).replace('-', '月',1).replace(' ', '日').replace(':', '点',1).replace(':', '分')
            new_name = new_name + "-修改时间"+ os.path.splitext(filename)[1]
            # print("{0} 修改时间是: {1}".format(filename, file_modify_time))
            print(filename_1,'KeyError错误，修改失败，没有拍摄时间属性,但进行了修改时间补充成功')
            os.rename(filename, new_name)

    else:
        mtime = os.stat(filename).st_mtime
        file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        new_name = dirpath+"/"+ file_modify_time.replace('-', '年',1).replace('-', '月',1).replace(' ', '日').replace(':', '点',1).replace(':', '分')
        new_name = new_name + "-修改时间"+ os.path.splitext(filename)[1]
        # print("{0} 修改时间是: {1}".format(filename, file_modify_time))
        print(filename_1,'修改失败，没有拍摄时间属性,但进行了修改时间补充成功')
        os.rename(filename, new_name)


# 待修改文件夹或照片路径
path = r'/Users/fujinghai 1/Documents/项目文件'

# -->  walk函数获取每个文件的绝对路径及文件名  导入到上面getexif函数；筛选JPEG格式文件。
if __name__ == '__main__':
    for dirpath,dirnames,filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith("jpeg") or filename.endswith("jpg")or filename.endswith("png") \
                    or filename.endswith("JPG")or filename.endswith("mts")or filename.endswith("mp4")\
                    or filename.endswith("avi")or filename.endswith("MTS") or filename.endswith("mov")\
                    or filename.endswith("gif") or filename.endswith("MOV"):
                filename_1 = filename
                t = os.path.splitext(filename)[0]
                filename = dirpath+"/"+filename
                getExif(filename)
    # 遍历到所有文件夹，进行重命名为原名+创建时间
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            # shutil.move(dirpath+"/"+dirname,dirpath+"/"+dirname+"shop111")
            full_name = os.path.getctime(dirpath+"/"+dirname)
            timestamp = TimeStampToTime(full_name)
            os.rename(dirpath+"/"+dirname,dirpath+"/"+timestamp+"-"+dirname)