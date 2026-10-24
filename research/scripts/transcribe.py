# -*- coding: utf-8 -*-
"""批量转写：faster-whisper large-v3, GPU, 输出 srt + 带时间戳纯文本。"""
import json
import os
import sys
import time
from pathlib import Path

# 把 pip 安装的 CUDA DLL 加入搜索路径（必须在 import faster_whisper 前）
import nvidia.cublas
import nvidia.cudnn
for pkg in (nvidia.cublas, nvidia.cudnn):
    for base in pkg.__path__:
        bin_dir = Path(base) / "bin"
        if bin_dir.exists():
            os.add_dll_directory(str(bin_dir))
            os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ["PATH"]

from faster_whisper import WhisperModel

AUDIO_DIR = Path(__file__).parent / "audio"
OUT_DIR = Path(__file__).parent / "transcripts"
OUT_DIR.mkdir(exist_ok=True)

TITLES = {
    "BV1nAn26JEne": "小鹏L05智能体座舱（2026-10-22，25:45，巴黎车展）",
    "BV1fFp36HExr": "华为Pura X View（2026-10-10，22:51，长期使用）",
    "BV1K3Kp6dE6Z": "Robot Phone 跨时代重构（2026-07-21，49:08）",
    "BV1ScdmBpEtX": "AI原生汽车（2026-04-21，30:54）",
    "BV1pFh26mERY": "iPhone18 Pro 上手：解读苹果商业逻辑（2026-09-25，19:29）",
    "BV15Wu261E3L": "万物皆可skill：IMU控制Robot Phone云台（2026-08-10，12:09）",
    "BV11KaV6tEwV": "特斯拉Cybercab 静态体验（2026-09-28，13:05）",
}


def fmt_ts(sec):
    m, s = divmod(int(sec), 60)
    return f"[{m:02d}:{s:02d}]"


def main():
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    files = sorted(AUDIO_DIR.glob("*.m4a"))
    if len(sys.argv) > 1:
        files = [f for f in files if f.stem in sys.argv[1:]]
    for f in files:
        bvid = f.stem
        txt_path = OUT_DIR / f"{bvid}.txt"
        if txt_path.exists():
            print(f"skip {bvid}")
            continue
        t0 = time.time()
        segs, info = model.transcribe(
            str(f), language="zh", vad_filter=True, beam_size=1,
            condition_on_previous_text=False,
        )
        lines = []
        for s in segs:
            text = s.text.strip()
            if text:
                lines.append({"start": round(s.start, 1), "text": text})
        dt = time.time() - t0
        with open(txt_path, "w", encoding="utf-8") as fh:
            fh.write(f"# {TITLES.get(bvid, bvid)}\n")
            for l in lines:
                fh.write(f"{fmt_ts(l['start'])} {l['text']}\n")
        chars = sum(len(l["text"]) for l in lines)
        print(f"done {bvid}: {len(lines)} segs, {chars} chars, {dt:.0f}s, audio {info.duration:.0f}s", flush=True)


if __name__ == "__main__":
    main()
