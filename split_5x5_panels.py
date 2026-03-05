import os
from PIL import Image

# 配置（根据你的习惯改路径）
INPUT_DIR = './raw_panels'          # ← 把你的 5×5 大图放这里（可以多张）
OUTPUT_DIR = './dist/split'         # 输出切割后的小图
GRID_ROWS = 5                       # 行数
GRID_COLS = 5                       # 列数

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_image(image_path, basename):
    """切割单张图片成 5×5 网格"""
    with Image.open(image_path) as img:
        # 如果有透明通道，转 RGB（可选，根据需要注释掉）
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        width, height = img.size
        tile_width = width // GRID_COLS
        tile_height = height // GRID_ROWS
        
        # 如果不是完美整除，会自动截取到边界（丢弃多余像素）
        print(f"处理 {basename} | 尺寸: {width}x{height} | 每格约: {tile_width}x{tile_height}")
        
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                left = col * tile_width
                top = row * tile_height
                right = left + tile_width
                bottom = top + tile_height
                
                # 裁剪
                tile = img.crop((left, top, right, bottom))
                
                # 文件名：原文件名_编号.png（001-025）
                tile_number = row * GRID_COLS + col + 1
                tile_name = f"{basename}_panel_{tile_number:03d}.png"
                tile_path = os.path.join(OUTPUT_DIR, tile_name)
                
                tile.save(tile_path, "PNG")  # 输出 PNG，保留质量
                # 如果想输出 WebP： tile.save(tile_path.replace('.png', '.webp'), "WEBP", quality=95)
                
                print(f"  保存 {tile_name}")

def main():
    print("开始切割 5×5 面板图片...")
    processed = 0
    
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(INPUT_DIR, filename)
            basename = os.path.splitext(filename)[0]  # 去掉扩展名
            split_image(img_path, basename)
            processed += 1
    
    if processed == 0:
        print("警告：raw_panels 文件夹里没有找到图片！请放进去再试。")
    else:
        print(f"\n完成！共处理 {processed} 张大图，切割出 {processed * 25} 张小图。")
        print(f"所有小图保存在：{os.path.abspath(OUTPUT_DIR)}")

if __name__ == '__main__':
    main()