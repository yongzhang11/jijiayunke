# @Time��2024/8/3 15:49
# @Author: Allan
import time
from config.BrowserDriver.drissionpage_driver import DrissionpageDriverConfig
import cv2
import os
import numpy as np

page = DrissionpageDriverConfig().driver_config()


"""
ORIGINAL_IMAGE: ԭʼ��ͼ·��
COMPARISON_FOLDER: �ȶԽ�ͼ·��
"""

class PublicPage:

    def page_screenshot_comparison(self, COMPARISON_FOLDER, ORIGINAL_IMAGE):
        screenshot_path = os.path.join(COMPARISON_FOLDER, "actual_screenshot.png")
        time.sleep(3)
        page.get_screenshot(path=COMPARISON_FOLDER, name='actual_screenshot.png', full_page=True)
        actual_image = cv2.imread(screenshot_path)
        # ���زο���ͼ
        reference_image_path = os.path.join(ORIGINAL_IMAGE, "reference_screenshot.png")
        if not os.path.exists(ORIGINAL_IMAGE):
            os.makedirs(ORIGINAL_IMAGE)
        reference_image = cv2.imread(reference_image_path)

        # ��ͼƬת��Ϊ�Ҷ�ͼ��
        gray_image1 = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

        # �������ŻҶ�ͼ��Ĳ���
        diff_image = cv2.absdiff(gray_image1, gray_image2)

        threshold = 0.001
        diff_mask = diff_image > threshold
        total_pixels = gray_image1.size
        diff_pixels = np.count_nonzero(diff_image)
        percentage_diff = diff_pixels / total_pixels
        if percentage_diff > threshold:
            result_image = reference_image.copy()
            result_image[diff_mask] = [0, 0, 255]  # ��ɫ
            # ������ͼ��ָ���ļ���
            output_folder = "tmp\\output_images"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_file = os.path.join(output_folder, "result_image.png")
            cv2.imwrite(output_file, result_image)
            print("�ȶԽ�ͼʧ��")
        else:
            print("�ȶԽ�ͼ�ɹ�")
