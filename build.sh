#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
xelatex -interaction=nonstopmode -halt-on-error translation.tex
xelatex -interaction=nonstopmode -halt-on-error translation.tex
