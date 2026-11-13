"""CLI 入口。支援互動輸入、--text 與 --file。"""

import argparse
from pathlib import Path
import sys

from analyzer import analyze_text
from report import format_report


def parse_args() -> argparse.Namespace:
    """解析命令列參數。"""
    parser = argparse.ArgumentParser(
        description="以有限規則分析文字中的 Prompt Injection 可疑特徵。"
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--text", help="直接分析命令列文字（可傳入空字串）")
    source.add_argument("--file", type=Path, help="從 UTF-8 文字檔讀取輸入")
    return parser.parse_args()


def read_input(args: argparse.Namespace) -> str:
    """依參數讀取文字；無參數時允許輸入一行或空字串。"""
    if args.text is not None:
        return args.text
    if args.file is not None:
        try:
            return args.file.read_text(encoding="utf-8")
        except OSError as error:
            raise ValueError(f"無法讀取檔案：{error}") from error
    try:
        return input("請輸入要分析的文字（直接按 Enter 可分析空字串）：\n> ")
    except EOFError:
        return ""


def main() -> int:
    """執行 CLI 並回傳程序結束碼。"""
    args = parse_args()
    try:
        text = read_input(args)
    except ValueError as error:
        print(f"錯誤：{error}", file=sys.stderr)
        return 2

    result = analyze_text(text)
    print(format_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
