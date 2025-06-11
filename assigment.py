import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Helper function to display images side by side
def display_images(images, titles, filename):
    plt.figure(figsize=(15, 5))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Step 1: Print image dimensions and calculate compression rate
img = Image.open("baby.jpg")
width, height = img.size
print(f"Image Dimensions: {width} x {height} pixels")

# Uncompressed size (RGB, 3 bytes per pixel)
original_size = width * height * 3
# Actual file size
compressed_size = os.path.getsize("baby.jpg")
compression_rate = original_size / compressed_size
print(f"Compression Rate: {compression_rate:.2f}")

# Step 2: Brighten the image using Y component
img_ycbcr = img.convert("YCbCr")
y, cb, cr = img_ycbcr.split()

y_np = np.array(y)
y_np = np.clip(y_np + 50, 0, 255)  # Increase brightness by 50
y = Image.fromarray(y_np.astype(np.uint8))

img_bright = Image.merge("YCbCr", (y, cb, cr)).convert("RGB")
img_bright.save("baby_bright.jpg")

# Step 3: Detect and remove red shades
img_ycbcr = img.convert("YCbCr")
y, cb, cr = img_ycbcr.split()
y_np = np.array(y)
cb_np = np.array(cb)
cr_np = np.array(cr)

# Mask for red tones (Cr between 140 and 180)
mask = (cr_np > 140) & (cr_np < 180)
cr_np[mask] = 0

y_img = Image.fromarray(y_np)
cb_img = Image.fromarray(cb_np)
cr_img = Image.fromarray(cr_np)

img_no_red = Image.merge("YCbCr", (y_img, cb_img, cr_img)).convert("RGB")
img_no_red.save("baby_no_red.jpg")

# Step 4: JPEG compression simulation (Cb and Cr downsampling)
cb_small = cb.resize((width // 2, height // 2), Image.BILINEAR)
cr_small = cr.resize((width // 2, height // 2), Image.BILINEAR)

cb_up = cb_small.resize((width, height), Image.BILINEAR)
cr_up = cr_small.resize((width, height), Image.BILINEAR)

img_jpeg_sim = Image.merge("YCbCr", (y, cb_up, cr_up)).convert("RGB")
img_jpeg_sim.save("baby_jpeg_simulated.jpg")

# Step 5: Downsample all components (Y, Cb, Cr)
y_small = y.resize((width // 2, height // 2), Image.BILINEAR)
y_up = y_small.resize((width, height), Image.BILINEAR)

img_all_low = Image.merge("YCbCr", (y_up, cb_up, cr_up)).convert("RGB")
img_all_low.save("baby_all_downsampled.jpg")

# Visualize results: Display all images side by side
images = [img, img_bright, img_no_red, img_jpeg_sim, img_all_low]
titles = ["Original", "Brightened", "Red Tones Removed", "JPEG Simulation", "All Components Downsampled"]
display_images(images, titles, "results_comparison.jpg")

print("Results saved: baby_bright.jpg, baby_no_red.jpg, baby_jpeg_simulated.jpg, baby_all_downsampled.jpg")
print("Comparison image saved: results_comparison.jpg")