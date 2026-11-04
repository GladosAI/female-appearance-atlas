# 在线阅览与发布

技术方案检查日期：2026-11-02；许可更新：2026-11-03。正式源码仓库为[GladosAI/female-appearance-atlas](https://github.com/GladosAI/female-appearance-atlas)，在线阅览尚未部署。下述命令只产生本地产物，不创建账号、远程仓库或付费服务。当前项目素材仅非商业使用，不预先授权商业性质的收费或广告盈利镜像。

## 两种在线包

```sh
python tools/build_atlas.py --skip-package
python tools/release_atlas.py web --output dist/web-original
python tools/release_atlas.py web --image-mode webp --output dist/web-preview
```

第一种保留原始 PNG；第二种使用 quality=88 的有损 WebP，不缩小像素尺寸，页面标注为预览版。原图不被覆盖。源码和完整离线包仍保留原图；预览站导出的图片由预览图解码，不能称为无损原图。

在线包将数据抽离为可独立缓存的带哈希 JS，删去运行时不用的生成 prompt，保留检索、外观卡、详情和图片下载。不携带约1.3GiB的本地图片读取 sidecar；HTTP 同源可直接读取图片。词条缩略图接近可见区域才加载，而不是为全部已排版卡片下载整张图页。

## 优先考虑免费静态托管

不需要数据库、登录服务器或生图 API。Cloudflare Pages / Workers Static Assets 是可选部署目标；发布包内有 `_headers` 与静态资产配置，上传整个目录即可。按官方当前说明，静态请求免费；Pages Free 单站20,000文件、单文件25MiB，构建500次/月。发布工具输出大小和数量预检，部署前仍应以账号当时规则为准。

GitHub Pages 发布站点上限1GB，是否能用取决于实际生成包大小，不能把下载 ZIP 的压缩后大小当作站点大小。GitHub 代码仓库和 Pages 是不同服务，仓库超过1GB不代表 Pages 也允许同样体积。

R2 可用于原图另存，当前 Standard 免费额度10GB-month、每月100万次A类与1000万次B类操作、无出站带宽费；它是按量计费产品，超免费额度仍可能收费，不作为零账单方案默认开启。先试纯静态托管，资源过大时再评估是否需要 R2。

海外免费服务的中国大陆访问速度、可用性不可保证。部署后需从目标网络实测。国内镜像可由愿意承担运维的社区成员提供，清楚标明独立运营者；不承诺官方长期付费CDN，不以源码仓库/raw地址代替正式图片CDN。大陆机房和域名的接入要求，应按选定服务核实后再部署。

## 源码与离线包

```sh
python tools/release_atlas.py packages --output dist/release-review
```

生成 source、images、offline-copy 三个 ZIP 和 CHECKSUMS.json；三包解压到同一位置组合成完整本地图鉴。每个包必须小于 GitHub Release 的单文件2GiB限制。图片包包含当前图页和照片需要的原始文件，不重复分发未被引用的旧修订；源码包不含个人缓存、node_modules、原图和图片 sidecar，普通贡献者无需先克隆全部图片。

代码采用MIT，项目有权授权的素材与编辑内容采用CC BY-NC 4.0，第三方例外保留原条件。三个ZIP均附带许可正文、范围说明、第三方说明及逐项素材证据，单独取得图片资源包也能查清许可。公开发布前执行`python tools/validate_atlas.py --release`；发布清单分别记录代码与内容许可。工具不会自动push或部署。

## 对方项目的情况

本地克隆的 AI Pose Gallery 将数千张 img/、thumbs/ 图片作为普通 Git 对象跟踪，并通过 .gitignore 排除部分原始PNG备份和构建目录；它的下载体积并不小。`wrangler.jsonc` 指向 dist 静态资产，并为 `/api/*` 配置 Worker 优先处理。这说明它把“Git 存放什么”和“网站如何托管”分开处理；无法仅凭配置推定其实际账单或国内访问质量。我们的素材包更适合与日常代码协作分离。

依据：[Pages 限制](https://developers.cloudflare.com/pages/platform/limits/)、[Pages 定价](https://developers.cloudflare.com/pages/functions/pricing/)、[Workers 静态资产费用](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/)、[R2 定价](https://developers.cloudflare.com/r2/pricing/)、[GitHub Pages 限制](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)、[Release 限制](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)。
