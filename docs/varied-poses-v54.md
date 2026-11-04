# 多样 Pose 与角色摆姿扩充

[体态与动作](../index.html?section=pose) · [本轮64项](../index.html?section=clothing_new) · [300项动作总索引](pose-atlas.md) · [提示词与原图路径](../prompts/image-prompts-v54.json)

新增64个动作单帧，编号PO237—PO300，分成16组，每组4项。体态与动作现有300项，另有24项[柔韧、伸展与舞蹈姿态](../index.html?section=flexibility_poses)。旧编号、外观卡与原有图页保留。

本轮用内置 image_gen 制作16张四格图页。站姿与坐姿用竖格，沙发、地面和双人构图用宽格；每页按实际分隔线确定裁剪区域。人物与手足、必要家具及支撑接触完整保留，动作不以训练步骤编排。角色均为25岁以上成年人，穿完整服装。

## 分类索引

| 细分 | 数量 | 浏览 |
| --- | ---: | --- |
| 镜头前站姿与回眸构图 | 4 | [进入](../index.html?section=pose&dimension=%E9%95%9C%E5%A4%B4%E5%89%8D%E7%AB%99%E5%A7%BF%E4%B8%8E%E5%9B%9E%E7%9C%B8%E6%9E%84%E5%9B%BE) |
| 活泼、俏皮与可爱全身摆姿 | 4 | [进入](../index.html?section=pose&dimension=%E6%B4%BB%E6%B3%BC%E3%80%81%E4%BF%8F%E7%9A%AE%E4%B8%8E%E5%8F%AF%E7%88%B1%E5%85%A8%E8%BA%AB%E6%91%86%E5%A7%BF) |
| 优雅礼服、裙摆与小手袋摆姿 | 4 | [进入](../index.html?section=pose&dimension=%E4%BC%98%E9%9B%85%E7%A4%BC%E6%9C%8D%E3%80%81%E8%A3%99%E6%91%86%E4%B8%8E%E5%B0%8F%E6%89%8B%E8%A2%8B%E6%91%86%E5%A7%BF) |
| 椅面、靠背与桌边造型 | 4 | [进入](../index.html?section=pose&dimension=%E6%A4%85%E9%9D%A2%E3%80%81%E9%9D%A0%E8%83%8C%E4%B8%8E%E6%A1%8C%E8%BE%B9%E9%80%A0%E5%9E%8B) |
| 沙发休闲与靠垫构图 | 4 | [进入](../index.html?section=pose&dimension=%E6%B2%99%E5%8F%91%E4%BC%91%E9%97%B2%E4%B8%8E%E9%9D%A0%E5%9E%AB%E6%9E%84%E5%9B%BE) |
| 地面坐卧与斜线构图 | 4 | [进入](../index.html?section=pose&dimension=%E5%9C%B0%E9%9D%A2%E5%9D%90%E5%8D%A7%E4%B8%8E%E6%96%9C%E7%BA%BF%E6%9E%84%E5%9B%BE) |
| 行走回身、摆臂与衣物动态 | 4 | [进入](../index.html?section=pose&dimension=%E8%A1%8C%E8%B5%B0%E5%9B%9E%E8%BA%AB%E3%80%81%E6%91%86%E8%87%82%E4%B8%8E%E8%A1%A3%E7%89%A9%E5%8A%A8%E6%80%81) |
| 急停、躲闪与低位移动 | 4 | [进入](../index.html?section=pose&dimension=%E6%80%A5%E5%81%9C%E3%80%81%E8%BA%B2%E9%97%AA%E4%B8%8E%E4%BD%8E%E4%BD%8D%E7%A7%BB%E5%8A%A8) |
| 舞台歌唱、麦克风与谢幕 | 4 | [进入](../index.html?section=pose&dimension=%E8%88%9E%E5%8F%B0%E6%AD%8C%E5%94%B1%E3%80%81%E9%BA%A6%E5%85%8B%E9%A3%8E%E4%B8%8E%E8%B0%A2%E5%B9%95) |
| 手机、耳机与拍摄手势 | 4 | [进入](../index.html?section=pose&dimension=%E6%89%8B%E6%9C%BA%E3%80%81%E8%80%B3%E6%9C%BA%E4%B8%8E%E6%8B%8D%E6%91%84%E6%89%8B%E5%8A%BF) |
| 穿戴、发绳与袖口整理 | 4 | [进入](../index.html?section=pose&dimension=%E7%A9%BF%E6%88%B4%E3%80%81%E5%8F%91%E7%BB%B3%E4%B8%8E%E8%A2%96%E5%8F%A3%E6%95%B4%E7%90%86) |
| 家务、收纳与厨房操作 | 4 | [进入](../index.html?section=pose&dimension=%E5%AE%B6%E5%8A%A1%E3%80%81%E6%94%B6%E7%BA%B3%E4%B8%8E%E5%8E%A8%E6%88%BF%E6%93%8D%E4%BD%9C) |
| 门框、窗沿与室内倚靠 | 4 | [进入](../index.html?section=pose&dimension=%E9%97%A8%E6%A1%86%E3%80%81%E7%AA%97%E6%B2%BF%E4%B8%8E%E5%AE%A4%E5%86%85%E5%80%9A%E9%9D%A0) |
| 运动重心、投接与落地 | 4 | [进入](../index.html?section=pose&dimension=%E8%BF%90%E5%8A%A8%E9%87%8D%E5%BF%83%E3%80%81%E6%8A%95%E6%8E%A5%E4%B8%8E%E8%90%BD%E5%9C%B0) |
| 施法、召唤与漂浮手势 | 4 | [进入](../index.html?section=pose&dimension=%E6%96%BD%E6%B3%95%E3%80%81%E5%8F%AC%E5%94%A4%E4%B8%8E%E6%BC%82%E6%B5%AE%E6%89%8B%E5%8A%BF) |
| 双人邀请、引导与轻松互动 | 4 | [进入](../index.html?section=pose&dimension=%E5%8F%8C%E4%BA%BA%E9%82%80%E8%AF%B7%E3%80%81%E5%BC%95%E5%AF%BC%E4%B8%8E%E8%BD%BB%E6%9D%BE%E4%BA%92%E5%8A%A8) |

每项标明视角、动作阶段和主要支撑。摆姿先看头、胸廓与骨盆的方向，再看手足位置；持物看手掌与物件接触；坐卧看座面、背垫和地面承重；双人看各自重心与接触手臂。图为单帧绘画参考，动态连续性可按角色和场景另行设计。

## 镜头前站姿与回眸构图

[浏览这一组](../index.html?section=pose&dimension=%E9%95%9C%E5%A4%B4%E5%89%8D%E7%AB%99%E5%A7%BF%E4%B8%8E%E5%9B%9E%E7%9C%B8%E6%9E%84%E5%9B%BE) · [完整原图](../images/sheet-po237-po240.png)

![镜头前站姿与回眸构图 · 4项](../images/sheet-po237-po240.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO237 · 背向肩上回眸摆姿](../index.html?section=pose&q=PO237) | 斜后面 | 双脚脚底 | 回眸定格 |
| [PO238 · 肩髋逆向四分之三站姿](../index.html?section=pose&q=PO238) | 斜前面 | 双脚脚底 | 静止摆姿 |
| [PO239 · 侧身转脸窄站摆姿](../index.html?section=pose&q=PO239) | 正侧面 | 双脚脚底 | 转脸定格 |
| [PO240 · 迈步回首衣摆摆姿](../index.html?section=pose&q=PO240) | 斜后面 | 前脚脚底、后脚前掌 | 回首迈步中段 |

## 活泼、俏皮与可爱全身摆姿

[浏览这一组](../index.html?section=pose&dimension=%E6%B4%BB%E6%B3%BC%E3%80%81%E4%BF%8F%E7%9A%AE%E4%B8%8E%E5%8F%AF%E7%88%B1%E5%85%A8%E8%BA%AB%E6%91%86%E5%A7%BF) · [完整原图](../images/sheet-po241-po244.png)

![活泼、俏皮与可爱全身摆姿 · 4项](../images/sheet-po241-po244.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO241 · 头顶双臂大心形摆姿](../index.html?section=pose&q=PO241) | 正面 | 双脚脚底 | 手势完成 |
| [PO242 · 脸旁双剪刀手全身摆姿](../index.html?section=pose&q=PO242) | 斜前面 | 双脚脚底 | 手势定格 |
| [PO243 · 背手单脚后勾俏皮站姿](../index.html?section=pose&q=PO243) | 正侧面 | 单脚脚底 | 单足定格 |
| [PO244 · 张臂迎接轻探身姿态](../index.html?section=pose&q=PO244) | 正面 | 双脚脚底 | 迎接动作中段 |

## 优雅礼服、裙摆与小手袋摆姿

[浏览这一组](../index.html?section=pose&dimension=%E4%BC%98%E9%9B%85%E7%A4%BC%E6%9C%8D%E3%80%81%E8%A3%99%E6%91%86%E4%B8%8E%E5%B0%8F%E6%89%8B%E8%A2%8B%E6%91%86%E5%A7%BF) · [完整原图](../images/sheet-po245-po248.png)

![优雅礼服、裙摆与小手袋摆姿 · 4项](../images/sheet-po245-po248.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO245 · 交步扶裙礼服站姿](../index.html?section=pose&q=PO245) | 斜前面 | 后脚脚底、前脚前掌 | 静止摆姿 |
| [PO246 · 双手低提手袋并脚站姿](../index.html?section=pose&q=PO246) | 正面 | 双脚脚底 | 静止摆姿 |
| [PO247 · 长裙台阶回身摆姿](../index.html?section=pose&q=PO247) | 斜后面 | 高低两级台阶上的双脚 | 回身定格 |
| [PO248 · 收肩交腕侧转裙装姿](../index.html?section=pose&q=PO248) | 斜前面 | 双脚脚底 | 静止摆姿 |

## 椅面、靠背与桌边造型

[浏览这一组](../index.html?section=pose&dimension=%E6%A4%85%E9%9D%A2%E3%80%81%E9%9D%A0%E8%83%8C%E4%B8%8E%E6%A1%8C%E8%BE%B9%E9%80%A0%E5%9E%8B) · [完整原图](../images/sheet-po249-po252.png)

![椅面、靠背与桌边造型 · 4项](../images/sheet-po249-po252.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO249 · 侧坐单臂搭椅背摆姿](../index.html?section=pose&q=PO249) | 正侧面 | 座面、双脚脚底 | 静止坐姿 |
| [PO250 · 前倾双肘扶膝坐姿](../index.html?section=pose&q=PO250) | 斜前面 | 座面、双脚脚底与双前臂 | 前倾定格 |
| [PO251 · 高凳侧坐单脚踩档](../index.html?section=pose&q=PO251) | 斜侧面 | 座面、一脚横档与另一脚脚尖 | 静止坐姿 |
| [PO252 · 桌边回身扶椅坐姿](../index.html?section=pose&q=PO252) | 斜后面 | 座面、双脚脚底与单手椅背 | 回身中段 |

## 沙发休闲与靠垫构图

[浏览这一组](../index.html?section=pose&dimension=%E6%B2%99%E5%8F%91%E4%BC%91%E9%97%B2%E4%B8%8E%E9%9D%A0%E5%9E%AB%E6%9E%84%E5%9B%BE) · [完整原图](../images/sheet-po253-po256.png)

![沙发休闲与靠垫构图 · 4项](../images/sheet-po253-po256.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO253 · 沙发收腿环抱靠垫](../index.html?section=pose&q=PO253) | 斜前面 | 沙发座垫与背垫 | 静止休息 |
| [PO254 · 沙发横坐单腿伸展](../index.html?section=pose&q=PO254) | 正侧面 | 沙发座垫、靠背与单脚 | 静止休息 |
| [PO255 · 沙发边坐双臂上伸](../index.html?section=pose&q=PO255) | 斜前面 | 座面与双脚脚底 | 伸展定格 |
| [PO256 · 沙发高跪回头扶背](../index.html?section=pose&q=PO256) | 斜后面 | 座垫、双膝小腿与双手 | 回头定格 |

## 地面坐卧与斜线构图

[浏览这一组](../index.html?section=pose&dimension=%E5%9C%B0%E9%9D%A2%E5%9D%90%E5%8D%A7%E4%B8%8E%E6%96%9C%E7%BA%BF%E6%9E%84%E5%9B%BE) · [完整原图](../images/sheet-po257-po260.png)

![地面坐卧与斜线构图 · 4项](../images/sheet-po257-po260.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO257 · 地面侧坐双手环单膝](../index.html?section=pose&q=PO257) | 斜前面 | 坐骨、屈腿外侧与前脚 | 静止坐姿 |
| [PO258 · 仰卧双手枕后踝交叠](../index.html?section=pose&q=PO258) | 侧面略俯视 | 背部、双肘与腿后侧 | 静止休息 |
| [PO259 · 侧卧上下腿错位休息](../index.html?section=pose&q=PO259) | 正侧面 | 身体侧面、下侧肘与前脚 | 静止休息 |
| [PO260 · 地面俯坐手撑侧后方](../index.html?section=pose&q=PO260) | 斜前面 | 坐骨、单手掌与双脚 | 静止支撑 |

## 行走回身、摆臂与衣物动态

[浏览这一组](../index.html?section=pose&dimension=%E8%A1%8C%E8%B5%B0%E5%9B%9E%E8%BA%AB%E3%80%81%E6%91%86%E8%87%82%E4%B8%8E%E8%A1%A3%E7%89%A9%E5%8A%A8%E6%80%81) · [完整原图](../images/sheet-po261-po264.png)

![行走回身、摆臂与衣物动态 · 4项](../images/sheet-po261-po264.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO261 · 长外套横向快步摆臂](../index.html?section=pose&q=PO261) | 正侧面 | 前脚脚跟与后脚前掌 | 双脚交接支撑 |
| [PO262 · 行走半转身抬手示意](../index.html?section=pose&q=PO262) | 斜后面 | 前脚脚底与后脚前掌 | 抬手回身中段 |
| [PO263 · 轻提购物袋小步行走](../index.html?section=pose&q=PO263) | 斜前面 | 前脚脚底 | 单足支撑中段 |
| [PO264 · 裙摆随转身弧形展开](../index.html?section=pose&q=PO264) | 斜前面 | 双前脚掌 | 小幅转身中段 |

## 急停、躲闪与低位移动

[浏览这一组](../index.html?section=pose&dimension=%E6%80%A5%E5%81%9C%E3%80%81%E8%BA%B2%E9%97%AA%E4%B8%8E%E4%BD%8E%E4%BD%8D%E7%A7%BB%E5%8A%A8) · [完整原图](../images/sheet-po265-po268.png)

![急停、躲闪与低位移动 · 4项](../images/sheet-po265-po268.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO265 · 侧移急停单掌平衡](../index.html?section=pose&q=PO265) | 斜前面 | 双脚脚底 | 急停缓冲 |
| [PO266 · 低头侧身穿过窄隙](../index.html?section=pose&q=PO266) | 正侧面 | 双脚脚底 | 低位移动中段 |
| [PO267 · 扶栏侧跨低障碍](../index.html?section=pose&q=PO267) | 斜侧面 | 一手掌、支撑脚脚底 | 跨越中段 |
| [PO268 · 弯膝后撤抬手避让](../index.html?section=pose&q=PO268) | 斜前面 | 后脚脚底与前脚前掌 | 后撤中段 |

## 舞台歌唱、麦克风与谢幕

[浏览这一组](../index.html?section=pose&dimension=%E8%88%9E%E5%8F%B0%E6%AD%8C%E5%94%B1%E3%80%81%E9%BA%A6%E5%85%8B%E9%A3%8E%E4%B8%8E%E8%B0%A2%E5%B9%95) · [完整原图](../images/sheet-po269-po272.png)

![舞台歌唱、麦克风与谢幕 · 4项](../images/sheet-po269-po272.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO269 · 单手握麦前倾演唱](../index.html?section=pose&q=PO269) | 斜前面 | 双脚脚底 | 演唱中段 |
| [PO270 · 扶麦架侧身演唱](../index.html?section=pose&q=PO270) | 正侧面 | 双脚脚底、单手轻扶麦架 | 演唱中段 |
| [PO271 · 持麦高举手臂互动](../index.html?section=pose&q=PO271) | 正面 | 双脚脚底 | 手臂最高点 |
| [PO272 · 一手覆心持麦谢幕](../index.html?section=pose&q=PO272) | 斜前面 | 双脚脚底 | 浅鞠躬定格 |

## 手机、耳机与拍摄手势

[浏览这一组](../index.html?section=pose&dimension=%E6%89%8B%E6%9C%BA%E3%80%81%E8%80%B3%E6%9C%BA%E4%B8%8E%E6%8B%8D%E6%91%84%E6%89%8B%E5%8A%BF) · [完整原图](../images/sheet-po273-po276-v2.png)

![手机、耳机与拍摄手势 · 4项](../images/sheet-po273-po276-v2.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO273 · 举手机全身自拍摆姿](../index.html?section=pose&q=PO273) | 斜前面 | 双脚脚底 | 取景定格 |
| [PO274 · 双手低持手机阅读](../index.html?section=pose&q=PO274) | 正侧面 | 双脚脚底 | 阅读定格 |
| [PO275 · 单手按耳罩听音姿](../index.html?section=pose&q=PO275) | 斜前面 | 双脚脚底 | 聆听定格 |
| [PO276 · 横持手机半蹲取景](../index.html?section=pose&q=PO276) | 斜侧面 | 双脚脚底 | 取景定格 |

## 穿戴、发绳与袖口整理

[浏览这一组](../index.html?section=pose&dimension=%E7%A9%BF%E6%88%B4%E3%80%81%E5%8F%91%E7%BB%B3%E4%B8%8E%E8%A2%96%E5%8F%A3%E6%95%B4%E7%90%86) · [完整原图](../images/sheet-po277-po280.png)

![穿戴、发绳与袖口整理 · 4项](../images/sheet-po277-po280.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO277 · 双手扣外套前襟](../index.html?section=pose&q=PO277) | 正面 | 双脚脚底 | 扣合中段 |
| [PO278 · 单手提领双手理围巾](../index.html?section=pose&q=PO278) | 斜前面 | 双脚脚底 | 整理中段 |
| [PO279 · 背向双手扎低马尾](../index.html?section=pose&q=PO279) | 背面 | 双脚脚底 | 固定发绳中段 |
| [PO280 · 站姿拉袖口轻低头](../index.html?section=pose&q=PO280) | 斜前面 | 双脚脚底 | 整理中段 |

## 家务、收纳与厨房操作

[浏览这一组](../index.html?section=pose&dimension=%E5%AE%B6%E5%8A%A1%E3%80%81%E6%94%B6%E7%BA%B3%E4%B8%8E%E5%8E%A8%E6%88%BF%E6%93%8D%E4%BD%9C) · [完整原图](../images/sheet-po281-po284.png)

![家务、收纳与厨房操作 · 4项](../images/sheet-po281-po284.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO281 · 双手擀面桌前站姿](../index.html?section=pose&q=PO281) | 正侧面 | 双脚脚底、双手操作台面 | 操作中段 |
| [PO282 · 俯身叠衣双手压平](../index.html?section=pose&q=PO282) | 斜侧面 | 双脚脚底、双掌台面 | 叠衣中段 |
| [PO283 · 侧跪收纳下层柜格](../index.html?section=pose&q=PO283) | 正侧面 | 后膝、小腿与前脚脚底 | 放置中段 |
| [PO284 · 抱衣篮回身归置](../index.html?section=pose&q=PO284) | 斜前面 | 双脚脚底、双前臂托篮 | 回身定格 |

## 门框、窗沿与室内倚靠

[浏览这一组](../index.html?section=pose&dimension=%E9%97%A8%E6%A1%86%E3%80%81%E7%AA%97%E6%B2%BF%E4%B8%8E%E5%AE%A4%E5%86%85%E5%80%9A%E9%9D%A0) · [完整原图](../images/sheet-po285-po288.png)

![门框、窗沿与室内倚靠 · 4项](../images/sheet-po285-po288.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO285 · 单臂扶门框侧探身](../index.html?section=pose&q=PO285) | 斜前面 | 双脚脚底、单掌门框 | 探身定格 |
| [PO286 · 侧坐低窗台向外看](../index.html?section=pose&q=PO286) | 正侧面 | 窗台座面与双脚脚底 | 静止观察 |
| [PO287 · 双肘撑窗沿托下颏](../index.html?section=pose&q=PO287) | 斜侧面 | 双脚脚底与双前臂窗沿 | 静止观察 |
| [PO288 · 门前回身握门柄](../index.html?section=pose&q=PO288) | 斜后面 | 双脚脚底与单手门柄 | 回身暂停 |

## 运动重心、投接与落地

[浏览这一组](../index.html?section=pose&dimension=%E8%BF%90%E5%8A%A8%E9%87%8D%E5%BF%83%E3%80%81%E6%8A%95%E6%8E%A5%E4%B8%8E%E8%90%BD%E5%9C%B0) · [完整原图](../images/sheet-po289-po292.png)

![运动重心、投接与落地 · 4项](../images/sheet-po289-po292.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO289 · 双手胸前准备接球](../index.html?section=pose&q=PO289) | 斜前面 | 双脚脚底 | 接球准备 |
| [PO290 · 单手肩上传球定格](../index.html?section=pose&q=PO290) | 正侧面 | 前脚脚底、后脚前掌 | 传球出手后 |
| [PO291 · 前脚落地后腿回收](../index.html?section=pose&q=PO291) | 斜前面 | 前脚脚底 | 单足落地缓冲 |
| [PO292 · 弓步双手持球侧转](../index.html?section=pose&q=PO292) | 斜前面 | 双脚脚底 | 转体定格 |

## 施法、召唤与漂浮手势

[浏览这一组](../index.html?section=pose&dimension=%E6%96%BD%E6%B3%95%E3%80%81%E5%8F%AC%E5%94%A4%E4%B8%8E%E6%BC%82%E6%B5%AE%E6%89%8B%E5%8A%BF) · [完整原图](../images/sheet-po293-po296.png)

![施法、召唤与漂浮手势 · 4项](../images/sheet-po293-po296.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO293 · 单掌托光另一手引导](../index.html?section=pose&q=PO293) | 斜前面 | 双脚脚底 | 施法定格 |
| [PO294 · 双掌相向凝聚光环](../index.html?section=pose&q=PO294) | 正面 | 双脚脚底 | 双手聚合中段 |
| [PO295 · 单膝跪地掌触法阵](../index.html?section=pose&q=PO295) | 斜侧面 | 后膝、前脚与单掌 | 接触地面定格 |
| [PO296 · 漂浮屈膝双臂低展](../index.html?section=pose&q=PO296) | 斜前面 | 无接触支撑，幻想漂浮 | 漂浮定格 |

## 双人邀请、引导与轻松互动

[浏览这一组](../index.html?section=pose&dimension=%E5%8F%8C%E4%BA%BA%E9%82%80%E8%AF%B7%E3%80%81%E5%BC%95%E5%AF%BC%E4%B8%8E%E8%BD%BB%E6%9D%BE%E4%BA%92%E5%8A%A8) · [完整原图](../images/sheet-po297-po300.png)

![双人邀请、引导与轻松互动 · 4项](../images/sheet-po297-po300.png)

| 编号与动作 | 视角 | 支撑 | 阶段 |
| --- | --- | --- | --- |
| [PO297 · 双人挽臂并肩站姿](../index.html?section=pose&q=PO297) | 正面 | 两人各自双脚脚底 | 静止互动 |
| [PO298 · 双人牵手一前一后引路](../index.html?section=pose&q=PO298) | 斜侧面 | 两人各自前脚脚底 | 引路迈步中段 |
| [PO299 · 双人并肩比心合影](../index.html?section=pose&q=PO299) | 正面 | 两人各自双脚脚底 | 手势完成 |
| [PO300 · 双人一手示路一人点头](../index.html?section=pose&q=PO300) | 斜前面 | 两人各自双脚脚底 | 交流定格 |

