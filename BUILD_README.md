# AI量化软件 Windows 打包指南

## 准备工作

### 1. 安装 Python 依赖

```bash
# 安装 PyInstaller
pip install pyinstaller

# 安装 PySide6 (如未安装)
pip install PySide6

# 安装 vnpy 及相关插件 (根据需要)
pip install vnpy vnpy_ctp vnpy_ctastrategy vnpy_ctabacktester vnpy_datamanager
```

### 2. 文件说明

| 文件 | 说明 |
|------|------|
| `app.spec` | PyInstaller 配置文件 |
| `build.bat` | Windows 打包脚本 |

## 打包步骤

### 方法一：使用打包脚本（推荐）

```bash
# 在项目根目录执行
build.bat
```

### 方法二：手动执行

```bash
# 清理旧构建
pyinstaller app.spec --clean

# 执行打包
pyinstaller app.spec
```

## 输出

打包完成后，EXE 文件位于：

```
dist\AI量化软件\AI量化软件.exe
```

## 常见问题

### Q: 打包后运行报错缺少 xxx.dll
A: 需要安装 Visual C++ Redistributable

### Q: 打包后图标显示不正确
A: 修改 `app.spec` 中的 `icon=None` 为 `icon='app.ico'`

### Q: 某些网关/插件无法使用
A: 在 `app.spec` 的 `hiddenimports` 中添加对应的模块名

### Q: 想添加更多应用模块
A: 编辑 `examples/veighna_trader/run.py`，取消注释需要的模块

## 自定义配置

### 修改入口文件

编辑 `app.spec` 中的：

```python
a = Analysis(
    ['examples/veighna_trader/run.py'],  # 修改这里
    ...
)
```

### 添加更多隐藏导入

```python
hiddenimports = [
    ...
    'vnpy_xxx',  # 添加你的模块
]
```

### 设置应用图标

```python
exe = EXE(
    ...
    icon='app.ico',  # 取消注释并设置图标路径
)
```

### 启用控制台窗口

```python
exe = EXE(
    ...
    console=True,  # 调试时可设为 True
)
```
