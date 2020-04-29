import shutil

f = open("pytorch-semseg/voc2012/VOCdevkit/VOC2012/ImageSets/Segmentation/trainval.txt", "r")

src_jpg_dir = "pytorch-semseg/voc2012/VOCdevkit/VOC2012/JPEGImages/"
src_pre_encode_dir = "pytorch-semseg/voc2012/VOCdevkit/VOC2012/SegmentationClass/pre_encoded/"
dst_jpg_dir = "datasets/JPEGImagesTrimmed/"
dst_pre_encode_dir = "datasets/SegmentationClassTrimmed/pre_encoded/"

for line in f:
    name = line.rstrip()
    src_jpg = src_jpg_dir + name + ".jpg"
    src_pre_encode = src_pre_encode_dir + name + ".png"
    dst_jpg = dst_jpg_dir + name  + ".jpg"
    dst_pre_encode = dst_pre_encode_dir + name + ".png"
    shutil.copy2(src_jpg, dst_jpg)
    shutil.copy2(src_pre_encode, dst_pre_encode)
