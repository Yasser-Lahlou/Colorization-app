import os

# Demo images

demo_images_files = ['B&W - Street.jpg', 'B&W - Kitchen.jpg', 'RGB - Mountain.jpg', 'RGB - Woman.jpg']

demo_images_names = ['B&W - Street', 'B&W - Kitchen', 'RGB - Mountain', 'RGB - Woman']

images_path = 'images'

demo_images_dict = {di_name: os.path.join(images_path, di_file) for di_name, di_file in zip(demo_images_names, demo_images_files)}

# model_selection
model_names = ['ECCV 16', 'SIGGRAPH 17']
