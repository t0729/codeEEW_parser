from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent

long_description = "詳細な説明等は GitHub を参照してください: https://github.com/t0729/codeEEW_parser/"

setup(
    name="codeEEW_parser",
    version="0.2.0",
    packages=find_packages(),
    author="t0729",
    description="緊急地震速報のコード電文を解析するためのパッケージ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t0729/codeEEW_parser/",
)
