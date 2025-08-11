# DepthMapVis 文件夹说明

## 文件夹内容

- `fused_depth/`：融合后的16位深度图像，原始数据，单位通常为毫米或深度值。
- `real_depth/`：真实测量的16位深度图像，原始数据。
- `mono_depth/`：单目估算的16位深度图像，原始数据。
- `rgb/`：对应的彩色图像（8位PNG）。
- `fused_depth_vis/`：由 `visualize_depth_colormap.py` 生成的融合深度图伪彩色可视化结果。
- `real_depth_vis/`：由 `visualize_depth_colormap.py` 生成的真实深度图伪彩色可视化结果。

## 脚本说明

### visualize_depth_colormap.py

用于批量读取 `fused_depth` 和 `real_depth` 文件夹下的16位深度图像，采用科研常用的伪彩色（如 JET）方式进行可视化，并将结果保存到 `fused_depth_vis` 和 `real_depth_vis` 文件夹。

#### 使用方法

1. 安装依赖（如未安装）：
   ```bash
   pip install opencv-python matplotlib
   ```
2. 运行脚本：
   ```bash
   python visualize_depth_colormap.py
   ```
3. 运行后将在 `fused_depth_vis` 和 `real_depth_vis` 文件夹下生成对应的伪彩色PNG图片。

#### 伪彩色说明
- 默认采用 JET 伪彩色（可在脚本中修改为其他 colormap）。
- 支持16位PNG深度图像，自动归一化到0-255后上色。
