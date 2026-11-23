Erdős 第 650 号问题：高中生证明详解
=================================

一、这份工程包含什么

本工程把论文关于整数与互异倍数匹配的证明展开成中文教学讲义。
核心结论是：对每个正整数 m，

    f(m) = min(m, ceil(2 sqrt(m)))。

这里 f(m) 是面对任意 m 个不同正整数以及任意长度为该集合最大数
两倍的开区间时，都能保证得到的最大匹配对数。准确的量词、整除
条件和左右两侧互异要求，以正文中的定义为准。

这是对已有论文的教学展开，不是新定理或独立发现。讲义补充了
基本概念、证明细节、边界检查、反例和数值计算，方便读者逐步核对。

二、文件入口

Erdos650_高中生证明详解.pdf
    可直接阅读、打印的成品。

Erdos650_高中生证明详解.tex
    完整的单文件 LaTeX 源码。编辑和续作从这里开始。

build.sh
    使用 XeLaTeX 连续编译三遍。中间文件与编译日志放在 build/，
    全部成功后把新 PDF 复制到本目录，保留相同的成品文件名。

verify.py、SHA256SUMS
    校验随包文件的 SHA-256，检查文件是否缺失或与清单不一致。
    这项检查不判断数学证明是否正确。

check_examples.py
    用整数与有理数计算检查正文中的有限数值实例。
    运行时会输出 JSON；有限检查不能代替正文的一般性证明。

PROOF_CHECKS.md、qa/example_checks.json
    实际检查范围、检查记录与保存的数值检查结果。

CONTINUE.md
    接续状态、六章结构和后续修改入口。

sources/original_2603.28636v1.pdf
    对照阅读用的英文原论文。

三、建议阅读顺序

1. 先把问题说清楚
   理解开区间、倍数、互不冲突的配对，以及“对所有情形保证”的含义。

2. 怎样保证所有配对互不冲突
   从交错路证明匹配的亏损公式，再把邻域大小转换成匹配数下界。

3. 为什么任何情形都至少能配出这么多对
   学会左右选点的单射计数；检查特殊端点、三种类型及所有碰撞情形。

4. 怎样构造只能配出少量对的例子
   阅读上界构造，逐步核对最大公因数、同余方程和区间端点。

5. 上下界怎样合成精确答案
   理解 f 的单调性、相邻乘积与平方数之间的边界，以及整数取整。

6. 把抽象证明落到具体计算上
   用完整的数值例子回看前面的一般证明。

首次阅读可顺序通读。再次阅读时，先复述每章要证明的结论，
再核对所用条件；数值例子可辅助理解，但不能据此跳过一般证明。

四、依赖与编译

推荐使用普通、完整安装的 TeX Live 或 MiKTeX，确保 xelatex 命令
可用，并安装相互兼容的发行版宏包。本文使用真正的 ctexbook 类，
中文字体采用 ctex 的 Fandol 字体配置。

所需组件包括：

    XeLaTeX、ctex/ctexbook、xeCJK、Fandol；
    geometry、amsmath、amssymb、amsthm；
    booktabs、longtable、array、enumitem；
    PGF/TikZ、xurl、hyperref，以及上述宏包的正常依赖。

Python 辅助检查要求 Python 3.9 或更新版本，仅使用标准库。
build.sh 需要 Bash；Linux、macOS、WSL 或 Git Bash 均可提供 Bash。
Windows 下也可以在已配置 XeLaTeX 的 LaTeX 编辑器中连续编译三遍。

建议先校验原始交付文件：

    python3 verify.py

Windows 下可使用：

    py -3 verify.py

然后编译：

    bash build.sh

编译始终显式关闭 shell escape，不使用当前工作环境的临时宏包路径。
构建脚本会切换到自身所在目录，因此文件夹路径中含中文或空格也可用。
若某遍编译失败，旧的成品 PDF 会保留；错误日志在 build/ 中。

重新编译可能改变 PDF 的时间信息等字节，因此与原 SHA256SUMS 不再
一致。若把重编译成品作为新版本交付，应重新检查并生成该版本的
校验清单。verify.py 只读取和校验文件，不会自动改写清单。

五、运行数值检查

    python3 check_examples.py

请使用普通 Python 模式，不启用 -O 或 PYTHONOPTIMIZE，以免跳过
脚本中的断言。保存的历史结果在 qa/example_checks.json；当前检查
范围与结论应结合 PROOF_CHECKS.md 阅读。

本工程没有重新执行 Lean 验证，也不声称新增了机器核验结果。
原论文关于 Lean 形式化的说明属于作者原文陈述，与本工程实际运行
的有限数值检查是不同事项。

六、原论文来源

Wouter van Doorn, Yanyang Li, Quanyu Tang:
Optimal bounds for an Erdős problem on matching integers to distinct multiples.

arXiv:2603.28636v1，2026-03-30。
版本页面：https://arxiv.org/abs/2603.28636v1

讲义的论证来源和教学补充请结合正文说明阅读。引用论文时应保留
原作者与原论文信息；引用本讲义的说明或例子时，应标明教学展开性质。
