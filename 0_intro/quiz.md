explain following concepts:

- 操作系统 OS. Window, Linux, MacOS, Android
- terminal, shell
- 解释器 interpreter是什么
    - python, bash 在不同 context 的含义，是编程语言还是解释器？

# Python 入门测验

知识点：Python、脚本、解释器、主文件（main file）、函数、参数、模块。

建议用时：20–30 分钟。请先独立完成，再查看[参考答案与解析](quiz_answers.md)。

## 一、概念理解

### 1. Python 是什么？（单选）

A. 一种操作系统  
B. 一种编程语言  
C. 一个只能运行在终端里的文本文件  
D. 一个函数的名称

### 2. 编程语言与解释器（简答）

在下面两句话中，“Python”和“python3”分别指什么？

- 我用 Python 编写了一段程序。
- 我在终端输入 `python3 main.py hello --name Alice`。

解释器在执行这条命令时起什么作用？

### 3. 什么是脚本？（简答）

用自己的话解释什么是脚本，并写出运行下面两个脚本的终端命令：

- Python 脚本：`main.py`（选择 `hello`，名字使用 `Alice`）
- Bash 脚本：`hello.sh`

### 4. 主文件必须叫 main.py 吗？（判断并说明理由）

“Python 程序的入口文件必须命名为 `main.py`，否则解释器无法运行它。”

## 二、阅读代码

以下题目使用这两个文件。

`greetings.py`：

```python
def hello(name: str):
    print(f"Hello, {name}!")


def bye(name: str):
    print(f"Bye, {name}!")
```

`main.py`：

```python
import argparse

from greetings import hello, bye


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say hello or bye to someone.")
    parser.add_argument("command", choices=["hello", "bye"])
    parser.add_argument("--name", required=True, help="Name of the person to greet")
    args = parser.parse_args()

    print(args)

    if args.command == "hello":
        hello(args.name)
    else:
        bye(args.name)
```

### 5. 函数定义和函数调用（简答）

在代码中分别找出：

1. 定义 `hello` 函数的位置。
2. 调用 `hello` 函数的位置。

只执行函数定义，会立即打印问候语吗？

### 6. 参数与传入的值（填空）

执行下面的代码：

```python
hello("小明")
```

- `hello` 定义中的参数名是 ______。
- 本次调用传入的值是 ______。
- 打印结果是 ______。

### 7. 命令行参数（阅读并回答）

```bash
python3 main.py bye --name Alice
```

1. 哪一部分是解释器命令？哪一部分是脚本文件名？
2. `args.command` 和 `args.name` 的值分别是什么？
3. 最终调用哪个函数，传入什么值？
4. 终端打印什么？

### 8. 缺少参数会怎样？（单选）

执行 `python3 main.py hello` 时会发生什么？

A. 打印 `Hello, world!`  
B. 打印 `Hello, !`  
C. 提示缺少必需的 `--name` 参数，程序退出  
D. 自动询问用户姓名

### 9. 模块与导入（简答）

```python
from greetings import hello, bye
```

1. `greetings` 对应本项目中的哪个文件？为什么导入语句里没有 `.py`？
2. 这行代码让 `main.py` 可以使用什么？
3. 把函数放到单独的模块中有什么好处？写出一点即可。

### 10. 主入口判断（判断并说明理由）

假设在同一目录的另一个 Python 文件里执行：

```python
import main
```

`main.py` 中 `if __name__ == "__main__":` 下方的命令行解析和函数调用会执行吗？如果直接运行 `python3 main.py hello --name Alice` 呢？

## 三、动手练习

### 11. 补全代码

在同一目录新建 `practice.py`，补全下面代码，使运行 `python3 practice.py` 时输出 `Bye, 小红!`。

```python
from ______ import ______


if __name__ == "__main__":
    ______("小红")
```

### 12. 增加一个函数

请在 `greetings.py` 中定义一个 `welcome(name)` 函数，使 `welcome("小明")` 打印 `Welcome, 小明!`。

再新建 `welcome_demo.py`，导入这个函数，并在主入口中调用它，传入你自己的名字。
