# -*- coding: utf-8 -*-
"""新语料统计：逻辑词密度等，与 v2 同口径（human_per_k 计算方式）。"""
import re, sys, glob
from pathlib import Path

LOGIC = re.compile(r"因为|所以|但|如果|那么|也就是说|对吧|所谓的|其实|就是说")
def k(n, chars): return round(n / chars * 1000, 1)

for f in sorted(glob.glob("transcripts/*.txt")):
    text = Path(f).read_text(encoding="utf-8")
    # 去掉时间戳行首 [mm:ss]
    body = re.sub(r"\[\d+:\d+\]\s*", "", text)
    body = re.sub(r"^#.*$", "", body, flags=re.M)
    chars = len(body)
    m = {
        "逻辑词": len(re.findall(r"因为|所以|但是|但|如果|那么|也就是说|它", body)),
        "对吧": len(re.findall(r"对吧", body)),
        "其实": len(re.findall(r"其实", body)),
        "我觉得": len(re.findall(r"我觉得|在我看来", body)),
        "所谓的": len(re.findall(r"所谓的", body)),
        "确定词": len(re.findall(r"一定|绝对|肯定", body)),
        "模糊词": len(re.findall(r"可能|应该|大概", body)),
        "你": len(re.findall(r"你", body)),
        "第一二三": len(re.findall(r"第一个|第一点|第一|第二个|第二点|第二个|第三", body)),
        "不是而是": len(re.findall(r"不是[^，。]{1,12}而是", body)),
        "OK翻页": len(re.findall(r"\bOK\b|OK，", body)),
    }
    name = Path(f).stem
    out = [f"{name} 字数={chars}"]
    out.append(f"逻辑词/千字={k(m['逻辑词'],chars)}")
    out.append(f"对吧/千字={k(m['对吧'],chars)} 其实={k(m['其实'],chars)} 我觉得={k(m['我觉得'],chars)} 所谓的={k(m['所谓的'],chars)}")
    out.append(f"确定词={k(m['确定词'],chars)} 模糊词={k(m['模糊词'],chars)} 你={k(m['你'],chars)}")
    out.append(f"编号路标={m['第一二三']} 不是而是={m['不是而是']} OK={m['OK翻页']}")
    print("\n".join(out), "\n")
