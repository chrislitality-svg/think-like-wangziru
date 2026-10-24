# 贡献指南 · Contributing Guide

感谢你有兴趣参与！这个仓库是一项**表达方法研究** + 它的可执行摘要（Agent Skill）。欢迎以下几类贡献：

| 贡献类型 | 怎么做 |
|---|---|
| **复现与质疑** | 结论都带 `corpus/` 出处与时间戳——按 [`METHODOLOGY.md`](METHODOLOGY.md) §八复现，发现对不上就开 Issue（给出文件名 + 时间戳 + 你的计数） |
| **新语料标注** | 按 `research/研究笔记-33条逐条拆解.md` 的问答链格式标注新视频，PR 附上 BV 号 |
| **即兴层偏差验证** | 最高优先级的开放问题：对完整直播回放做应答单元编码，验证「先判断后补证据」是否为切片高光偏差（见 `references/thinking-思维运转.md` 附录协议） |
| **翻译** | 新增语言或改进现有六语 README（中/英/韩/日/法/德） |
| **工具改进** | `tools/` 与 `research/scripts/` 均零第三方依赖，保持这一点；改动词频口径需同步更新 `METHODOLOGY.md` §6.1 |

## PR 规则

1. 改动会过 CI（工具编译 + 检测器语料回归：真人语料 AI 味指数必须 < 20）；
2. 修改研究结论时，在 PR 描述里给出证据链（语料文件 + 时间戳），并在 [`METHODOLOGY.md`](METHODOLOGY.md) §九证据分级表登记层级与强度；
3. 不接受改变仓库定位的 PR：不得用于训练模仿/冒充本人的模型、不得商用（CC BY-NC 4.0）、不得署王自如之名发布衍生稿；
4. 引用原话每处不超过 15 字，标注出处视频与时间点。

## 报告问题

- 研究结论错误 → Issue 标题加 `[research]`，附语料出处；
- skill 效果问题 → 加 `[skill]`，注明你用的模型（推荐 Gemini 3.8 Flash / DeepSeek V4 Flash）；
- 语料版权 concerns → 直接开 Issue，第一时间处理。

---

Thanks for contributing! This repo is an **expression-method study** plus its executable digest (an Agent Skill). The highest-value open problem right now: code full livestream replays to test whether the "judgment-first" improv pattern survives outside third-party highlight clips — protocol in `references/thinking-思维运转.md` (appendix). All research claims must keep a corpus file + timestamp evidence chain; changes to conclusions must be registered in `METHODOLOGY.md` §9. No commercial use, no persona-mimicry models (CC BY-NC 4.0).
