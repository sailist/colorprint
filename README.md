# colorprint
colorprint provide unified print method which can output colored text

# how2use
安装
```bash
pip install colorprint
```

查看例子
 ```python
from colorprint.example import printall
printall()
```
![fore](./image/fore.jpg)![back](./image/back.jpg)

使用
```python
from colorprint.printer import uprint
from colorprint.unicolor import *
uprint("FOREGROUND_GREEN\n", fore=FOREGROUND_GREEN)
uprint("BACKGROUND_WHITE\n", back=BACKGROUND_WHITE)

uprint("MODE_NORMAL\n", mode=MODE_NORMAL)\
    ("MODE_BLINK\n", mode=MODE_BLINK)\
    ("MODE_BOLD\n", mode=MODE_BOLD)\
    ("MODE_HIDE\n", mode=MODE_HIDE)\
    ("MODE_INVERT\n", mode=MODE_INVERT)\
    ("MODE_UNDERLINE\n", mode=MODE_UNDERLINE)
```

方法介绍：
```python
def uprint(value,
           fore=None,
           back = None,
           mode = None,
           end="",
           handle = "stdout",
           flush = True):
    '''
    Prints the colored values to sys.stdout or sys.stderr.
    :param fore: 
    :param back: 
    :param mode: 
    :param end: string appended after the last value, default a newline.
    :param handle: str, "stdout" or "stderr"
        note:the stderr haven't be tested.
    :param flush: whether to forcibly flush the stream.
    :return: uprint method, you can use 
        uprint()()()() to output strings with diff color.
    '''
```
