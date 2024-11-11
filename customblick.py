import cv2
import os

# Set paths
positive_images_path = 'path_to_positive_images_folder'
negative_images_path = 'path_to_negative_images_folder'
output_path = 'output_path_for_custom_cascade_xml_file'

# Create positive and negative description files
def create_description_files():
    with open('positives.txt', 'w') as f:
        for img_name in os.listdir(positive_images_path):
            if img_name.endswith('.jpg') or img_name.endswith('.png'):
                f.write(os.path.join(positive_images_path, img_name) + '\n')

    with open('negatives.txt', 'w') as f:
        for img_name in os.listdir(negative_images_path):
            if img_name.endswith('.jpg') or img_name.endswith('.png'):
                f.write(os.path.join(negative_images_path, img_name) + '\n')

# Create positive and negative description files
create_description_files()

# Run opencv_traincascade command
cmd = f"opencv_traincascade -data {output_path} -vec positives.vec -bg negatives.txt -numPos 1000 -numNeg 500 -numStages 10 -w 20 -h 20"
os.system(cmd)
