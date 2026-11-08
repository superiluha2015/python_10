from PIL import Image
import os

for number in range(1, 6):
    folder_name = f"photo_end_{number}"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    image = Image.open(f"photo_{number}.jpg")
    vk = image.resize((1400, 1000))
    instagramm = image.resize((1080, 1080))
    coordinates = (10, 0, instagramm.width - 10, instagramm.height)
    instagramm = instagramm.crop(coordinates)
    facebook = image.resize((1200, 628))
    facebook.save(f"{folder_name}/photo_facebook.png", format="PNG")
    instagramm.save(f"{folder_name}/photo_instagramm.png", format="PNG")
    vk.save(f"{folder_name}/photo_vk.png", format="PNG")