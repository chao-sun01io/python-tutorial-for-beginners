# Python 入门测验：参考答案与解析

对应题目：[Python 入门测验](quiz.md)。

### 1

B。Python 是一种编程语言。

### 2

第一句中的 Python 指编程语言；第二句中的 `python3` 是用于启动 Python 解释器的命令。解释器读取并执行 `main.py` 中的 Python 代码。

### 3

脚本是保存在文件中、可交给相应解释器执行的一组指令。本项目中可以这样运行：

```bash
python3 main.py hello --name Alice
bash hello.sh
```

### 4

错误。`main.py` 是常见的命名习惯，并非 Python 的强制要求。也可以把入口文件命名为 `app.py`，然后用 `python3 app.py` 运行。

### 5

1. `def hello(name: str):` 及其缩进的函数体定义了函数。
2. `hello(args.name)` 调用了函数。

只执行这个函数的定义不会打印问候语，调用时才会执行函数体中的 `print`。

### 6

- 参数名：`name`。
- 传入的值：字符串 `"小明"`。
- 打印结果：`Hello, 小明!`。

### 7

1. 解释器命令是 `python3`，脚本文件名是 `main.py`。
2. `args.command` 是 `"bye"`，`args.name` 是 `"Alice"`。
3. 调用 `bye`，传入字符串 `"Alice"`。
4. 打印 `Bye, Alice!`。

`--name Alice` 是命令行参数；程序解析它之后，把得到的值通过 `bye(args.name)` 传给函数。

### 8

C。`required=True` 表示必须提供 `--name`，缺少时 `argparse` 会报错并退出。

### 9

1. 对应 `greetings.py`。导入语句使用模块名 `greetings`，不写文件扩展名。
2. 可以通过 `hello` 和 `bye` 这两个名称调用导入的函数；导入本身不会调用这两个函数。
3. 例如：可以让多个文件复用函数，或者让入口文件更简洁。

### 10

导入 `main` 时，该条件不成立，因此其中的命令行解析和函数调用不会执行。直接运行 `main.py` 时，`__name__` 为 `"__main__"`，条件成立，会解析参数并打印 `Hello, Alice!`。

### 11

```python
from greetings import bye


if __name__ == "__main__":
    bye("小红")
```

### 12

在 `greetings.py` 中增加：

```python
def welcome(name: str):
    print(f"Welcome, {name}!")
```

`welcome_demo.py` 的一种写法：

```python
from greetings import welcome


if __name__ == "__main__":
    welcome("小明")
```

运行 `python3 welcome_demo.py`，会打印 `Welcome, 小明!`。
