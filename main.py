# -*- coding: UTF-8 -*-

import data
import image


from resizeInfo import ResizeInfo

defaultPath = data.imagePath
savePath = data.imageSavePath
names = data.names

x_list = data.resize_x_list
y_list = data.resize_y_list

resizeInfoDataList = list()
for i in range(len(x_list)):
    resizeInfoDataList += [ResizeInfo(x_list[i][0], x_list[i][1], y_list[i][0], y_list[i][1])]

#이미지 전체 삭제
flag = image.deleteAllImage(savePath)

#이미지 생성
image.imageGrayColorResizingWrite(defaultPath, savePath, names, resizeInfoDataList)

#테스트용 초기화 작업 (deleteAllImage 포함 작업)
# image.init()