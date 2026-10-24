#!/usr/bin/env python3
"""评审复算脚本：一次跑出 reviews/2026-10-24-同行评审与红队报告.md 里引用的全部数字。

零依赖，Python 3.8+，在仓库根目录运行：
    python reviews/scripts/recheck.py

口径说明（和项目原口径的差别都在这里，方便你证明我错了）：
  - 「正文」= 去掉 `#` 标题行、`>` 元信息行、行首 `[mm:ss]` 时间戳之后的文字；
  - 「字数」= 正文去掉所有空白后的字符数（转写没有标点，等于汉字+字母数字）；
  - 原口径 A（thinking §六）：分母 = 整个文件的原始长度（含时间戳、元信息、换行）；
  - 原口径 B（stats.py）：分母 = len(正文)，含换行。
"""
import glob
import re
import statistics
import sys

sys.path.insert(0, "tools")
import ai_flavor_check as A  # noqa: E402

FILES = sorted(glob.glob("corpus/*/*.txt"))


def raw(f):
    return open(f, encoding="utf-8").read()


def body(f, keep_newlines=True):
    t = re.sub(r"^\[\d+:\d+\]\s*", "", raw(f), flags=re.M)
    t = re.sub(r"^[#>].*$", "", t, flags=re.M)
    return t if keep_newlines else re.sub(r"\s", "", t)


def head(title):
    print(f"\n==== {title} ====")


# ── 1. 分母：18.2 万字到底是什么 ──
head("1. 全语料分母")
raw_len = sum(len(raw(f)) for f in FILES)
speech = sum(len(body(f, False)) for f in FILES)
print(f"原始文件总长度（含时间戳/元信息/换行）= {raw_len}")
print(f"实际口播字数（正文去空白）          = {speech}")
print(f"比值 = {raw_len / speech:.2f}")

# ── 2. 口头习惯词频 ──
head("2. 口头习惯词频（次/万字）")
HAB = {"其实": "其实", "所谓的": "所谓的", "我觉得": "我觉得", "为什么": "为什么", "对吧": "对吧", "OK": r"OK|ok|Ok"}
B_all = "".join(body(f, False) for f in FILES)
print(f"{'词':<6}{'次数':>6}{'原口径A':>10}{'正文口径':>10}")
for k, p in HAB.items():
    c = len(re.findall(p, B_all))
    print(f"{k:<6}{c:>6}{c / raw_len * 1e4:>10.1f}{c / speech * 1e4:>10.1f}")
for label, sel in (("官方 7 条", lambda f: "official" in f), ("切片 25 条", lambda f: "clips" in f),
                   ("剔除双人 3 条", lambda f: "RobotPhone跨时代" not in f and "韩路" not in f)):
    b = "".join(body(f, False) for f in FILES if sel(f))
    print(f"  {label}: 对吧 {b.count('对吧') / len(b) * 1e4:.1f}/万字，字数 {len(b)}")
print(f"71 篇底座：1660/796821 = {1660 / 796821 * 1e4:.2f}/万字；1660/864937 = {1660 / 864937 * 1e4:.2f}/万字")

# ── 3. 官方 7 条逐条：METHODOLOGY §6.2 ──
head("3. 官方 7 条逐条（每千字）")
R = {
    "逻辑§6.1": r"因为|所以|但是|但|如果|那么|也就是说|它",
    "逻辑检测器": r"因为|所以|但|如果|那么|的话|也就是说|换句话说|之所以|对于|所谓|只有|它",
    "逻辑syntax": r"因为|所以|但|如果|那么|也就是说|对于|所谓|只有|它",
    "确定": r"一定|绝对|肯定", "模糊": r"可能|应该|大概", "对吧": r"对吧",
}
print("文件 | 逻辑§6.1(stats.py分母) | 逻辑§6.1(去空白) | 逻辑-检测器口径 | 逻辑-syntax口径 | 确定 | 模糊 | 对吧 | 不是而是(§6.1正则) | 编号")
for f in (f for f in FILES if "official" in f):
    b = body(f)
    n_b, n = len(b), len(re.sub(r"\s", "", b))
    c = {k: len(re.findall(p, b)) for k, p in R.items()}
    notab = re.findall(r"不是[^，。]{1,12}而是", b)
    num = len(re.findall(r"第一个|第一点|第一|第二个|第二点|第二个|第三", b))
    print(f.split("/")[-1][:20], f"{c['逻辑§6.1'] / n_b * 1e3:.1f}", f"{c['逻辑§6.1'] / n * 1e3:.1f}",
          f"{c['逻辑检测器'] / n * 1e3:.1f}", f"{c['逻辑syntax'] / n * 1e3:.1f}", f"{c['确定'] / n_b * 1e3:.2f}",
          f"{c['模糊'] / n_b * 1e3:.2f}", f"{c['对吧'] / n_b * 1e3:.2f}", [m.replace(chr(10), '⏎') for m in notab], num,
          sep=" | ")

# ── 4. 切片的确定词 vs 模糊词 ──
head("4. 切片 25 条：确定词 vs 模糊词")
over, cge = 0, 0
for f in (f for f in FILES if "clips" in f):
    b = body(f, False)
    c, v = len(re.findall(r"一定|绝对|肯定", b)), len(re.findall(r"可能|应该|大概", b))
    over += c / len(b) * 1e3 > 2
    cge += c >= v
print(f"确定词 > 2/千字（产品层上限）的切片：{over}/25；确定词 ≥ 模糊词的切片：{cge}/25")
bc = "".join(body(f, False) for f in FILES if "clips" in f)
print(f"正则污染：'不一定' {bc.count('不一定')} 次被计为确定词；'不可能' {bc.count('不可能')} 次被计为模糊词")

# ── 5. 检测器：原文件 vs 去掉时间戳和元信息 ──
head("5. 检测器分数分布")
s_raw, s_clean = [], []
for f in FILES:
    s_raw.append(A.score(A.analyse(raw(f)))[0])
    s_clean.append(A.score(A.analyse(body(f)))[0])
# v1.9 起检测器在 analyse() 里自己剥离时间戳和元信息，两行结果应相同；8ebcbac 及之前两行不同
for lab, s in (("原文件（README 的用法）", s_raw), ("去时间戳+元信息", s_clean)):
    print(f"{lab}: 中位 {statistics.median(s)}，范围 {min(s)}–{max(s)}，<20 的 {sum(x < 20 for x in s)}/{len(s)}")
xb = "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"
r1, r2 = A.analyse(raw(xb)), A.analyse(body(xb))
print("西贝条（README『预期 11 分』、CI 回归门槛用的就是它）：")
print("  原文件:", A.score(r1)[0], A.score(r1)[2], "数字密度", r1["human_per_k"]["数字"])
print("  去伪影:", A.score(r2)[0], A.score(r2)[2], "数字密度", r2["human_per_k"]["数字"])

# ── 6. 套话稿能不能拿 0 分 ──
head("6. 对抗样本")
adv = raw("reviews/data/adversarial-套话稿.txt")
ra = A.analyse(adv)
print("纯套话 AI 稿:", A.score(ra)[0], A.score(ra)[1], ra["human_per_k"])

# ── 7. README『它能带来什么』0 分复跑 ──
head("7. README『它能带来什么』")
lines = raw("README.md").split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith("先给结论"))
end = next(i for i, l in enumerate(lines) if l.startswith(("外壳年年换", "外壳条条不同")))  # v1.9 改了收口句
sec_start = next(i for i, l in enumerate(lines) if l.startswith("## 它能带来什么"))
for lab, txt in (("正文，不含末句链接行", "\n".join(lines[start:end])),
                 ("正文，含末句链接行", "\n".join(lines[start:end + 1])),
                 ("整节，含稿前六行表格", "\n".join(lines[sec_start + 1:end + 1]))):
    r = A.analyse(txt)
    print(f"{lab}: {A.score(r)[0]} 分", A.score(r)[2] or "")

# ── 8. 手工断句复核句长 ──
head("8. 手工断句（2 段，单人标注）")


def L(s):
    return len(re.findall(r"[一-鿿A-Za-z0-9]", s))


allv = []
for f in sorted(glob.glob("reviews/data/断句-*.txt")):
    ss = [l.strip() for l in open(f, encoding="utf-8") if l.strip()]
    allv += [L(s) for s in ss]
q = sorted(allv)
print(f"n={len(q)} 句，中位 {statistics.median(q)} 字，P90 {q[int(.9 * len(q))]}，超过 30 字 {sum(x > 30 for x in q) / len(q):.0%}")
