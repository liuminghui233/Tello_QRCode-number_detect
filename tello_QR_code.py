# coding:utf8
import cv2
import pyzbar.pyzbar as pyzbar


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    barcodeData = ''
    barcodeType = ''
    for barcode in barcodes:
        # 条形码数据为字节对象，先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 向终端打印条形码数据和条形码类型
        print "[INFO] Found {} barcode: {}".format(barcodeType, barcodeData)
    return barcodeType, barcodeData


def QR_code_detect(frame):
    while True:
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        barcodeType, barcodeData = decodeDisplay(gray)

        return barcodeType, barcodeData
