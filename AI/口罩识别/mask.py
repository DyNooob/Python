import paddlehub as hub
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

test_img_path = ["E:\Python\AI\口罩识别\待检测\yes.jpg"]

module = hub.Module(name="pyramidbox_lite_mobile_mask")

input_dict = {"image": test_img_path}

print(input_dict)

results = module.face_detection(data=input_dict)

img = mpimg.imread("E:\Python\AI\口罩识别\检测结果\yes.jpg")
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')
plt.show()
