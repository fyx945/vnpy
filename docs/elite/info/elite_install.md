# Elite安装配置

本文档中安装步骤适用的操作系统包括：

- Windows 10/11
- Windows Server 2019/2022

> 其他版本的Windows系统安装时可能遇到各种依赖库问题，不推荐使用。


## 安装流程

### 安装

下载AI智能量化软件 Elite安装包后，双击安装包进入AI智能量化软件 Elite安装向导（推荐点击右键，选择【使用管理员身份运行】进行安装），点击【下一步】按钮即可进行安装目录选择，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/elite/install/1.png)

> 推荐将AI智能量化软件 Elite安装在默认路径的C:\veighna_elite，其他AI智能量化软件 Elite文档和教程中均使用该目录作为AI智能量化软件 Elite安装目录进行讲解。

选择完安装目录之后，点击【安装】即可进行AI智能量化软件 Elite安装，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/elite/install/2.png)

安装完成后，会转换到安装成功页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/elite/install/3.png)

此时桌面会出现AI智能量化软件 Elite Trader和AI智能量化软件 Elite Lab的图标，双击图标即可运行对应程序。

### 卸载

如果想卸载AI智能量化软件 Elite， 可以在Windows系统中打开【设置】-【应用】-【应用和功能】，找到AI智能量化软件 Elite进行卸载。


## 注意事项

### 独立环境

AI智能量化软件 Elite不会与AI智能量化软件 Studio等其他Python环境冲突，如需使用其他模块，可以通过PYTHONPATH环境变量加载。

### 用户信息

用户信息缓存在用户目录下的.vntrader文件夹中。如果卸载时需要清除用户数据及配置信息，需要将.vntrader文件夹删除。如果只是重新安装，只卸载程序即可，重装之后配置信息无需重新填写。
