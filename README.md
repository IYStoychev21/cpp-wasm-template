# cpp-wasm-template

<p align="center"> A script written in Python to compile C++ code into WebAssembly using Emscripten <p>

## Getting started
  - Use the template to generate a repository

## Prerequisites
  - [Python](https://www.python.org/)
  - [Empscripten](https://emscripten.org/)

## Installation
```
pip install -r requirements.txt
```

## Configuration
```yml
#config.yml

SourceDir: ./Assembly/src
OutputDir: ./App/src
IncludeDirs:
  - ./Assembly/src
IntBins: ./App/src/bin-int
OutputFileName: main
BuildMode: Debug
```

- SourceDir - Relative path to cpp code
- OutputDir - Relative path to the output WASM file
- IncludeDirs - Dir that would be including in the compilation phase
- IntDins - Relative path to intermediate directory
- OutputFileName - Name of the wasm file
- BuildMode - Build mode Debug/ Release

## Usage
```
python build.py config.yml
```
