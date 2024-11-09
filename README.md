# Flask 应用 README

## 概述
这个 Flask 应用程序旨在与各种 API 进行交互，包括聊天机器人 API 和图像生成 API，以提供动态和互动的用户体验。该应用程序由多个路由组成，处理不同的用户请求和响应。

## 特性
- **聊天机器人交互**：用户可以与由 Kimi API 支持的聊天机器人进行基于文本的对话。
- **图像生成**：用户可以输入提示词，使用 replicate API 和 Stable Diffusion 模型生成图像。
- **模板渲染**：应用程序使用 Flask 的 `render_template` 函数来服务 HTML 模板，提供清晰友好的用户界面。

## 先决条件
在运行应用程序之前，请确保已安装以下先决条件：

- Python 3.x
- Flask
- requests
- replicate（用于图像生成）

您可以使用 pip 安装所需的包：

```bash
pip install Flask requests replicate
```

## 环境变量

应用程序需要设置以下环境变量：

- `REPLICATE_API_TOKEN`：用于访问图像生成模型的 Replicate API 令牌。
- `Authorization`：Kimi 聊天机器人 API 的 API 密钥。

在操作系统中设置这些环境变量，或直接在代码中传递。

## 运行应用程序

要运行应用程序，请在终端执行以下命令：

```bash
python app.py
