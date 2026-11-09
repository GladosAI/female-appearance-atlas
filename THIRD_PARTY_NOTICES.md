# 第三方来源与许可说明

项目代码采用MIT不覆盖以下第三方素材和依赖。本文件核对日期为2026-11-03。

## 馆藏照片

本项目使用的六张Met照片分别对应对象107655、98226、76985、113066、82433、81112。官方对象API均返回`isPublicDomain: true`；具体核验、原图地址、署名与本地文件哈希保存在`source/rights-evidence.json`。本地JPEG有缩放或重编码，不声称与官方原始下载字节一致。

依照[Met Open Access](https://www.metmuseum.org/hubs/open-access)，这些开放的公有领域作品图片按CC0提供。它们沿用原有状态，不改称项目自有MIT图片，也不附加项目CC BY-NC的非商用限制。此结论只涉及已逐项核验的六张图片。

## 构建与测试依赖

`package-lock.json`锁定依赖版本。当前普通网页没有引用远程JavaScript库，也没有分发字体文件；CSS中的字体名使用访问设备的系统字体。

| 包 | 当前安装版本 | 包中声明的许可 | 用途 |
| --- | --- | --- | --- |
| playwright、playwright-core | 1.62.1 | Apache-2.0 | 开发/浏览器验证 |
| sharp | 0.35.5 | Apache-2.0 | 图片处理与导出 |
| @img/sharp-win32-x64 | 0.35.5 | Apache-2.0 AND LGPL-3.0-or-later | 本地sharp原生二进制 |
| @img/sharp-wasm32 | 0.35.5 | Apache-2.0 AND LGPL-3.0-or-later AND MIT | 本地sharp WASM依赖 |
| @img/colour | 1.1.0 | MIT | 图片处理依赖 |
| @emnapi/runtime | 1.11.3 | MIT | 原生/WASM运行支持 |
| tslib | 2.9.1 | 0BSD | 运行辅助 |
| semver | 7.8.5 | ISC | 工具版本处理 |
| detect-libc | 2.1.2 | Apache-2.0 | 原生环境检测 |

源码、图片、离线数据和静态预览包不包含`node_modules`、浏览器或这些原生/WASM二进制；安装依赖时保留各包随附LICENSE/NOTICE。若以后制作携带依赖的桌面安装包或容器镜像，应重新检查对应分发义务，不能把这里的开发依赖清单视为已经批准重新打包二进制。

## 生成工具与输入

AI图页的文件来源、已记录的编辑输入和生成提示词见`source/rights-provenance.json`。生成工具的条款与第三方输入、形象等权利分别核验；输出文件在生成目录中存在不等于获得所有第三方权利。项目有权授权的AI配图现采用CC BY-NC 4.0，按具体文件哈希记录所有者的非商业授权。

相关阅读链接不是图片来源授权。项目没有将AI Pose Gallery的图库作为本项目的图片包；抽象词条、独立文案与具体图片的来源应分别判断。

## GitHub 图标

侧栏 GitHub 标志使用 [Primer Octicons mark-github-16](https://github.com/primer/octicons/blob/main/icons/mark-github-16.svg)，Copyright (c) 2026 GitHub Inc.，采用 MIT 许可。图标以 SVG 内嵌，仅增加随主题配色和辅助功能属性；完整许可见 [OCTICONS-LICENSE.txt](assets/icons/OCTICONS-LICENSE.txt)。该第三方图标保留原许可，不适用项目素材的非商用限制。
