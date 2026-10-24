# research/ · 研究过程资料（v1.5 全套原始记录）

> 这里是 2026-10-24 那次语料扩充的**完整工作痕迹**：逐条拆解笔记、采集元数据、可运行脚本。分析结论见 `references/logic-表达逻辑.md` 与 `references/samples-标杆拆解.md`（那是整理稿）；**本目录是原始稿**——更啰嗦、更细，含每条的分钟级问答链表和未被结论收录的观察。

| 文件 | 内容 |
|---|---|
| `研究笔记-33条逐条拆解.md` | 33 条的逐条逻辑拆解原始笔记：官方号 7 条（每条含分钟级问答链、核心论点与论据清单、过桥句实录、对公理的验证与新发现）+ JACHZHU 切片逐条拆解 + 即兴逻辑系统的归纳过程。**结论文件里每条规则的出处都能在这里找到对应的视频和时间戳** |
| `data/official_videos.json` | 官方号视频列表元数据（bvid/标题/发布时间/时长/播放，B 站 API 2026-10-24 抓取，第一页 40 条） |
| `data/jachzhu_videos.json` | JACHZHU 账号全部 32 条视频的 DOM 提取清单（BV 号+卡片原文，含播放数） |
| `scripts/fetch_list.py` | B 站空间列表抓取脚本（wbi 签名实现；裸跑会被 -352 风控拦，需先在浏览器上下文种设备 cookie，见 METHODOLOGY.md §2.1） |
| `scripts/transcribe.py` | 批量转写脚本（faster-whisper large-v3 / cuda / float16 / VAD / beam_size=1，产出带时间戳文本，即 `corpus/` 里文稿的生成器） |
| `编码-切片应答单元.md` | v1.10 补做：25 条切片按 METHODOLOGY §4.2 四列编码，72 个应答单元，四步原型实际覆盖率 22%。编码规则写在表前 |
| `scripts/clip_units.py` | 上面那张编码表的数据与统计脚本（零依赖） |
| `scripts/stats.py` | 词频统计口径（逻辑词/确定词/模糊词/不是A而是B/编号路标/OK），与 METHODOLOGY.md §6.1 的正则一致 |

## 如何用这批资料

1. **质疑某条结论** → 结论里注明了视频和时间戳 → `corpus/` 里翻到对应文稿核对原文 → 不服可以看原视频（BV 号在文稿头部）；
2. **延伸研究** → 改 `scripts/stats.py` 的正则跑自己的指标，或按 `研究笔记` 里的问答链格式标注新的视频；
3. **重新转写** → `scripts/transcribe.py` 换模型/参数，与 `corpus/` 对比 ASR 差异。

未收录进仓库的中间产物：32 条 m4a 音频（约 150MB，版权敏感度高于文本转写，不发布，用 `scripts/transcribe.py` + BV 号可自行下载复现）。
