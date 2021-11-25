"""
For inference output of MMdetection

from pickle file(*.pkl) to csv file (*.csv)
pickle_path is where the pickle file located
image_path is used for loading the image name
"""


import os
import csv
import pickle
import glob
# pickle file path
# something like 'D:/Project/mmdetection-master/inference_output/output.pkl'
pickle_path = ''
# image file path
# something like 'D:/Project/mmdetection-master/test_image/'
image_path = ''

# load pickle
with open(pickle_path, 'rb') as f:
    data = pickle.load(f)

# list image path *.jpg file name
image_list = [os.path.basename(x) for x in glob.glob(image_path + '*.jpg')]
# print(image_list)


# write csv
with open('submission.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    # first row
    spamwriter.writerow(['image_filename', 'label_id', 'x', 'y', 'w', 'h', 'confidence'])

    for img in range(len(data)):  # ith image
        for cls in range(len(data[img])):  # xth class
            for bbox in range(len(data[img][cls])):  # yth bbox
                # since pixel are integer
                x1 = int(data[img][cls][bbox][0])
                y1 = int(data[img][cls][bbox][1])
                x2 = int(data[img][cls][bbox][2])
                y2 = int(data[img][cls][bbox][3])
                conf = data[img][cls][bbox][4]
                # print(x1, y1, x2, y2)
                w = x2 - x1
                h = y2 - y1

                spamwriter.writerow([image_list[img], cls + 1, x1, y1, w, h, conf])

