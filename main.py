# -*- coding: UTF-8 -*-

import data
import image

import resizeInfo

defaultPath = data.imagePath
savePath = data.imageSavePath
names = data.names


resizeInfoData =  resizeInfo.ResizeInfo(data.resize_x_list, data.resize_y_list)

#이미지 전체 삭제
flag = image.deleteAllImage(savePath)

#이미지 생성
image.imageGrayColorResizingWrite(defaultPath, savePath, names, resizeInfoData)

#테스트용 초기화 작업 (deleteAllImage 포함 작업)
# image.init()