Erdos650 完整中文翻译工程

底本：Wouter van Doorn、Yanyang Li、Quanyu Tang，
Optimal bounds for an Erdős problem on matching integers to distinct multiples，
arXiv:2603.28636v1，2026-03-30，原文共8页。

译文范围：标题、摘要、正文第1—5节、全部证明、3条脚注、16条参考文献及作者地址。
原编号：公式(1)—(4)，定理2.1、注2.2、引理2.3、定理3.1、断言3.2、注3.3、定理4.1。
正文按原文翻译；原文两处说明不够精确，详见译者说明。

编译方法：
1. 安装完整的 TeX Live 或 MiKTeX，包含 XeLaTeX、ctex、xeCJK、zhnumber、amsmath、amssymb、amsthm、geometry、enumitem、xurl、hyperref。
2. 安装 ctex 默认的 Fandol 字体与 Latin Modern 字体（完整 TeX Live 通常已经包含）。
3. 在解压目录中运行 bash build.sh；或连续运行两次：
   xelatex -interaction=nonstopmode -halt-on-error translation.tex
4. 输出为 translation.pdf。交付的中文PDF与 translation.tex 内容一致。

校验方法：
运行 python3 verify.py，按 SHA256SUMS 检查文件是否完整。

说明：
本工程提供译文和可编辑LaTeX源码；不含文献[6]引用的外部Lean工程。
正文所列Lean版本、Mathlib提交、行数和定理数均按论文原文保留，未在本次翻译中重新运行验证。
所需字体和TeX依赖由上述软件包提供，不含在压缩包内。
