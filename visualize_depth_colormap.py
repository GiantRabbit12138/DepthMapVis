import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_colormap(depth_img, colormap=cv2.COLORMAP_JET):
    # 归一化到0-255
    depth_normalized = cv2.normalize(depth_img, None, 0, 255, cv2.NORM_MINMAX)
    depth_normalized = np.uint8(depth_normalized)
    # 应用伪彩色
    color_img = cv2.applyColorMap(depth_normalized, colormap)
    return color_img

def visualize_folder(folder_path, output_folder, colormap=cv2.COLORMAP_JET):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            depth_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            if depth_img is None or depth_img.dtype != np.uint16:
                print(f"跳过非16位深度图像: {filename}")
                continue
            color_img = apply_colormap(depth_img, colormap)
            out_path = os.path.join(output_folder, filename)
            cv2.imwrite(out_path, color_img)
            # 可选：显示
            plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
            plt.title(filename)
            plt.axis('off')
            plt.show()

if __name__ == "__main__":
    # 可视化 fused_depth
    visualize_folder('fused_depth', 'fused_depth_vis', colormap=cv2.COLORMAP_JET)
    # 可视化 real_depth
    visualize_folder('real_depth', 'real_depth_vis', colormap=cv2.COLORMAP_JET)
