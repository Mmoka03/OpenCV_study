
import cv2
import numpy as np
import os

# defaultPath: 기본 이미지 경로
# savePath: 이미지가 저장될 경로
# names: 확장자까지 포함한 이미지 파일명 리스트
# resizeInfoList 이미지를 자르기 위한 주소 지정 클래스 리스트
def imageGrayColorResizingWrite(defaultPath: str, savePath: str, names: list, resizeInfoList: list):
    for i in range(len(names)):
        
        #완성형 path
        path = defaultPath + '/' + names[i]

        #OpenCV에서 한글은 인식이 안되기 때문에 다음과 같은 과정을 거칩니다.
        # 1. numpy.fromfile 함수를 사용하여 binary data를 numpy array 형태로 읽습니다.
        # 2. cv2.imdecode 함수로 복호화를 하여 OpenCV에서 사용가능한 형태로 변환합니다. (이 과정에서 GRAYSCALE를 적용합니다)
        img_array = np.fromfile(path, np.uint8)
        full_path = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

        x1 = resizeInfoList[i].getX1()
        x2 = resizeInfoList[i].getX2()
        y1 = resizeInfoList[i].getY1()
        y2 = resizeInfoList[i].getY2()

        #numpy를 사용하여 이미지를 자릅니다.
        dst = full_path[x1:y1, x2:y2].copy()
        
        #이미지를 지정된 경로에 저장합니다.
        write(savePath, names[i], dst)

# savePath: 이미지가 저장될 경로
# name: 확장자까지 포함한 이미지 파일명
# dst: numpy.ndarray 타입의 디코딩된 이미지 파일입니다.
def write(savePath: str, name: str, dst: np.ndarray):

    #확장자
    extension = os.path.splitext(name)[1]
    
    # result: bool
    # encoded_img: numpy.ndarray 인코딩된 이미지
    result, encoded_img = cv2.imencode(extension, dst)

    # 저장경로가 없을 시 생성
    if not pathExists(savePath):
        os.mkdir(savePath)

    # numpy.ndarray 타입을 이미지 파일로 저장
    if result: # 만약 인코딩이 정상적으로 된 경우
        with open(savePath + '/' + name, mode='w+b') as f:
            encoded_img.tofile(f)

#테스트 편의성용 초기화
def init(path: str = './save_image'):    
    
    #사용자 입력을 대기 (0 또는 인자값이 없을 경우 시간 제한없이 대기)
    cv2.waitKey(0)
    
    #테스트 편의성을 위해 경로 직접지정
    deleteAllImage(path)

    #실행중인 모든 프로그램 종료
    cv2.destroyAllWindows()

#이미지 전체 삭제
def deleteAllImage(directoryPath: str):    
    
    #경로 존재 확인 후 전체 삭제
    if pathExists(directoryPath):
        for file in os.scandir(directoryPath):
            os.remove(file.path)
        return True
    return False

#경로 존재여부 확인
def pathExists(path: str): 
    if os.path.exists(path):
        return True
    return False