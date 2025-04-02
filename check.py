import os

# 配置文件相对于项目根目录的预期路径
config_relative_path = "configs/sam2.1_training/heart_chambers_finetune.yaml"

# 获取当前工作目录
current_working_directory = os.getcwd()
print(f"当前工作目录是: {current_working_directory}")
print(f"正在检查是否存在文件: {config_relative_path}")

# 构建文件的绝对路径
config_absolute_path = os.path.join(current_working_directory, config_relative_path)

# 检查文件是否存在
if os.path.exists(config_absolute_path):
    print(f"\n成功! 文件找到了。")
    print(f"文件的绝对路径是: {os.path.abspath(config_absolute_path)}")
    print("\n请确认这个路径与你运行时 Hydra 报错信息中提到的路径一致。")
else:
    print(f"\n错误：在当前目录下找不到文件 '{config_relative_path}'。")
    print(f"请确认：")
    print(f"1. 你当前是否在 SAM 2 项目的 **根目录** 下运行此脚本？")
    print(f"2. 文件路径 '{config_relative_path}' 是否拼写完全正确？")
    print(f"3. 该文件是否确实存在于预期的子目录中？")

# 补充：检查 configs 目录本身是否存在
configs_dir = os.path.join(current_working_directory, "configs")
if not os.path.isdir(configs_dir):
    print(f"\n警告：连 'configs' 目录在当前位置都找不到！请务必在项目根目录运行。")

