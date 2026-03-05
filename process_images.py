import os
from PIL import Image
# 配置
INPUT_DIR = './raw_images'  # 你放 4K 原图的地方 (PNG/JPG)
OUTPUT_THUMB = './dist/thumbs'  # 输出小图的地方
OUTPUT_FULL = './dist/full'  # 输出大图的地方
# 确保输出目录存在
os.makedirs(OUTPUT_THUMB, exist_ok=True)
os.makedirs(OUTPUT_FULL, exist_ok=True)
def process_images():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(INPUT_DIR, filename)
            with Image.open(img_path) as img:
                # 转换色彩模式 (防止 PNG 透明度报错)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                # 1. 保存大图 (高质量 WebP)
                # 质量 95，几乎无损，体积减少一半
                full_name = os.path.splitext(filename)[0] + '.webp'
                img.save(os.path.join(OUTPUT_FULL, full_name), 'WEBP', quality=95)
                print(f"[Full] {full_name} saved.")
                # 2. 生成缩略图 (800x800, 中等质量)
                # thumbnail 方法会自动保持比例缩放
                img.thumbnail((800, 800))
                img.save(os.path.join(OUTPUT_THUMB, full_name), 'WEBP', quality=85)
                print(f"[Thumb] {full_name} saved.")
if __name__ == '__main__':
    print("开始处理图片资产...")
    process_images()
    print("处理完成！")