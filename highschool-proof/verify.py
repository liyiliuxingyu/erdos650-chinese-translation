#!/usr/bin/env python3
"""Verify a UTF-8 SHA256SUMS file without modifying any package files.

Default: use SHA256SUMS beside this script, independently of the working
directory. An optional manifest argument uses paths relative to that manifest.
Both GNU sha256sum text/binary markers and escaped filenames are supported.
"""

import argparse
import hashlib
from pathlib import Path
import re
import sys


ENTRY = re.compile(r"([0-9a-fA-F]{64}) ([ *])(.+)")


def unescape_gnu_filename(value):
    """Decode the filename escapes used by GNU sha256sum's escaped lines."""
    result = []
    pos = 0
    escapes = {"\\": "\\", "n": "\n", "r": "\r"}
    while pos < len(value):
        char = value[pos]
        if char != "\\":
            result.append(char)
            pos += 1
            continue
        pos += 1
        if pos >= len(value) or value[pos] not in escapes:
            raise ValueError("文件名中存在不支持或不完整的反斜杠转义")
        result.append(escapes[value[pos]])
        pos += 1
    return "".join(result)


def parse_entry(line):
    escaped = line.startswith("\\")
    if escaped:
        line = line[1:]
    match = ENTRY.fullmatch(line)
    if match is None:
        raise ValueError("应为 64 位十六进制 SHA-256、空格、模式标记及文件名")
    expected, _mode, filename = match.groups()
    if escaped:
        filename = unescape_gnu_filename(filename)
    if not filename or "\x00" in filename:
        raise ValueError("文件名为空或含有空字符")
    return expected.lower(), filename


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="只读校验 SHA256SUMS；失败时返回非零状态。"
    )
    parser.add_argument(
        "manifest",
        nargs="?",
        help="可选的校验清单；省略时读取脚本同目录的 SHA256SUMS",
    )
    args = parser.parse_args(argv)
    if args.manifest is None:
        manifest = Path(__file__).resolve().parent / "SHA256SUMS"
    else:
        manifest = Path(args.manifest).expanduser().resolve()

    try:
        text = manifest.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print("[失败] 无法读取校验清单 {!s}：{}".format(manifest, exc), file=sys.stderr)
        return 1

    base = manifest.resolve().parent
    seen = set()
    checked = 0
    entries = 0
    failed = 0

    # Splitting only at LF avoids treating other Unicode filename characters
    # as line separators. Text mode has already normalized CRLF line endings.
    for number, line in enumerate(text.split("\n"), 1):
        if not line or line.isspace() or line.startswith("#"):
            continue
        try:
            expected, filename = parse_entry(line)
            entries += 1
            if filename in seen:
                raise ValueError("清单中重复出现文件名 {!r}".format(filename))
            seen.add(filename)

            relative = Path(filename)
            if relative.is_absolute():
                raise ValueError("清单必须使用相对于其所在目录的文件路径")
            actual_path = (base / relative).resolve(strict=True)
            try:
                actual_path.relative_to(base)
            except ValueError:
                raise ValueError("文件路径越出了工程目录：{!r}".format(filename))
            if not actual_path.is_file():
                raise ValueError("不是普通文件：{!r}".format(filename))

            actual = file_sha256(actual_path)
            if actual != expected:
                raise ValueError(
                    "SHA-256 不一致：{!r}\n  清单：{}\n  实际：{}".format(
                        filename, expected, actual
                    )
                )
            checked += 1
            print("[通过] {!r}".format(filename))
        except (OSError, ValueError, RuntimeError) as exc:
            failed += 1
            print("[失败] 清单第 {} 行：{}".format(number, exc), file=sys.stderr)

    if entries == 0:
        failed += 1
        print("[失败] 校验清单没有有效文件条目。", file=sys.stderr)

    if failed:
        print(
            "校验未通过：{} 个文件通过，{} 项错误。".format(checked, failed),
            file=sys.stderr,
        )
        return 1

    print("全部通过：{} 个文件与 SHA256SUMS 一致。".format(checked))
    return 0


if __name__ == "__main__":
    sys.exit(main())
