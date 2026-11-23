# Erdős 第 650 号问题：完整中文译本

本仓库收录论文 **《关于将整数匹配到互异倍数的一个 Erdős 问题的最优界》** 的完整中文译本及可编辑 LaTeX 工程。

- **阅读中文 PDF：** [translation.pdf](translation.pdf)
- **查看 LaTeX 源码：** [translation.tex](translation.tex)
- **下载原始交付工程包：** [Erdos650_中文翻译工程.zip](releases/Erdos650_中文翻译工程.zip)

## 高中生证明详解

另附六章中文讲义，逐步展开匹配的亏损公式、上下界证明、开区间端点与整数取整，并配有完整的数值例子。这是原论文证明的教学展开。

- **阅读讲义 PDF：** [Erdos650_高中生证明详解.pdf](highschool-proof/Erdos650_高中生证明详解.pdf)
- **查看讲义 LaTeX 源码：** [Erdos650_高中生证明详解.tex](highschool-proof/Erdos650_高中生证明详解.tex)
- **阅读与编译说明：** [README.txt](highschool-proof/README.txt)
- **下载完整讲义工程：** [Erdos650_高中生证明详解工程.zip](releases/Erdos650_高中生证明详解工程.zip)

## 原论文

**Wouter van Doorn, Yanyang Li, Quanyu Tang**  
*Optimal bounds for an Erdős problem on matching integers to distinct multiples*  
arXiv:2603.28636v1，2026 年 3 月 30 日。

- [arXiv 原文页面](https://arxiv.org/abs/2603.28636v1)
- [本仓库保存的英文原文 PDF](original_2603.28636v1.pdf)

论文的主要结论为

$$
f(m)=\min\left(m,\left\lceil 2\sqrt m\right\rceil\right).
$$

## 译文内容与格式

中文译本共 **14 页**，采用 A4、`ctexbook` 和默认 Fandol 中文字体。内容包括标题、摘要、正文第 1—5 节、全部证明、3 条原文脚注、16 条参考文献及作者地址，保留原文的公式、定理与引理编号。

译文以所附英文 v1 PDF 为底本。原文两处说明不够精确的地方已在独立的“译者说明”中澄清，正文没有静默改写。详细校对范围及检查记录见 [CHECKS.txt](CHECKS.txt)。

## 编译

需要 XeLaTeX、`ctex`、`xeCJK`、`zhnumber`、`amsmath`、`amssymb`、`amsthm`、`geometry`、`enumitem`、`xurl`、`hyperref`，以及 Fandol 和 Latin Modern 字体。可使用包含这些组件的 TeX Live 或 MiKTeX。

在仓库根目录运行：

```bash
bash build.sh
```

脚本运行两遍 XeLaTeX，以解析目录、交叉引用与参考文献编号；生成文件为 `translation.pdf`。`translation.tex` 是完整单文件源码，不依赖额外的正文片段。

## 文件校验

在仓库根目录运行：

```bash
python3 verify.py
```

程序依据原始交付包的 [SHA256SUMS](SHA256SUMS) 检查译文、底本及随附文件。上传前已核对恢复的压缩包与原始交付的 SHA-256 相同，并重新运行校验通过。重新编译会改变 PDF 文件字节及校验值；原始已交付版本仍保存在 `releases/` 的压缩包中。

## Lean 形式化的范围

文中关于 Lean 形式化完成情况、工具链版本、行数及定理数量的叙述均来自原论文。本次工作是中文翻译与排版，**没有重新运行或独立验证原论文引用的外部 Lean 工程**。本仓库未包含该外部工程。

## 文件说明

| 文件 | 内容 |
| --- | --- |
| `translation.pdf` | 完整中文译本 |
| `translation.tex` | 可编辑、可独立编译的 LaTeX 源码 |
| `original_2603.28636v1.pdf` | 英文翻译底本 |
| `build.sh` | XeLaTeX 编译入口 |
| `verify.py`、`SHA256SUMS` | 原始交付文件的校验程序与摘要 |
| `README.txt` | 原始工程说明 |
| `CHECKS.txt` | 校对记录、已完成检查及未验证范围 |
| `releases/Erdos650_中文翻译工程.zip` | 与原始交付完全一致的工程压缩包 |

