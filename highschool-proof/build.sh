#!/usr/bin/env bash
# Build the self-contained source with an ordinary TeX Live or MiKTeX setup.
# Shell escape stays disabled. The previous delivered PDF survives a failure.
set -euo pipefail

package_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source_stem='Erdos650_高中生证明详解'
source_file="${package_dir}/${source_stem}.tex"
build_dir="${package_dir}/build"

if ! command -v xelatex >/dev/null 2>&1; then
    printf '%s\n' '未找到 xelatex。请安装完整、兼容的 TeX Live 或 MiKTeX，并把 XeLaTeX 加入 PATH。' >&2
    exit 1
fi

if [[ ! -f "$source_file" ]]; then
    printf '未找到主文件：%s\n' "$source_file" >&2
    exit 1
fi

mkdir -p -- "$build_dir"
cd -- "$package_dir"

for pass in 1 2 3; do
    pass_log="${build_dir}/xelatex-pass-${pass}.log"
    printf '正在运行 XeLaTeX，第 %s/3 遍……\n' "$pass"
    if ! xelatex \
        -no-shell-escape \
        -interaction=nonstopmode \
        -halt-on-error \
        -file-line-error \
        -synctex=0 \
        -output-directory="$build_dir" \
        "$source_file" >"$pass_log" 2>&1; then
        printf '第 %s 遍编译失败。完整输出：%s\n' "$pass" "$pass_log" >&2
        tail -n 50 -- "$pass_log" >&2 || true
        exit 1
    fi
done

compiled_pdf="${build_dir}/${source_stem}.pdf"
if [[ ! -s "$compiled_pdf" ]]; then
    printf '编译命令结束，但未找到非空 PDF：%s\n' "$compiled_pdf" >&2
    exit 1
fi

cp -f -- "$compiled_pdf" "${package_dir}/${source_stem}.pdf"
printf '编译完成：%s\n' "${package_dir}/${source_stem}.pdf"
printf '中间文件与日志：%s\n' "$build_dir"
