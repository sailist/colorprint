import ctypes, sys
from colorprint.unicolor import *



if sys.platform == "win32" and sys.stdin.isatty():
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    std_err_handle = ctypes.windll.kernel32.GetStdHandle(STD_ERROR_HANDLE)
    # _handle_dict = dict(
    #     stdout=std_out_handle,
    #     stderr=std_err_handle
    # )
else:
    std_out_handle = sys.stdout
    std_err_handle = sys.stderr
_handle_dict = dict(
    stdout=sys.stdout,
    stderr=sys.stderr
)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def reset_color():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def in_terminal():
    '''
    在win环境中用python xx.py命令时，只支持获取句柄更改的手段，其他时候，可以用 \033
    :return:
    '''
    return sys.stdin.isatty()
def in_win():
    return sys.platform == "win32"

def cprint(*args,fore=None,back=None,sep=" ",end="",handle = "stdout",flush = True):
    value = sep.join(*args)

    if fore is None and back is None:
        reset_color()
    elif back is None:
        set_cmd_text_color(fore)
    elif fore is None:
        set_cmd_text_color(back)
    else:
        set_cmd_text_color(fore|back)

    print(value,end=end,file=_handle_dict[handle],flush=flush)
    # sys.stdout.write(str(value))
    # if flush:
    #     sys.stdout.flush()

    reset_color()
    return cprint

def eprint(*args,fore=None,back = None,mode = None,sep=" ",end="",handle = "stdout",flush = True):
    value = sep.join(*args)

    if mode is None:
        mode = MODE_NORMAL
    if fore is None and back is None:
        print(f"\033[{mode}m{value}\033[0m", end=end, file=_handle_dict[handle], flush=flush)
    elif back is None:
        print(f"\033[{mode};{fore}m{value}\033[0m", end = end, file=_handle_dict[handle], flush=flush)
    elif fore is None:
        print(f"\033[{mode};;{back}m{value}\033[0m",end = end,file=_handle_dict[handle],flush=flush)
    else:
        print(f"\033[{mode};{fore};{back}m{value}\033[0m", end=end, file=_handle_dict[handle], flush=flush)




def uprint(*args,
           fore=None,
           back = None,
           mode = None,
           sep=" ",
           end="",
           handle = "stdout",
           flush = True,):
    '''
    Prints the colored values to sys.stdout or sys.stderr.
    :param fore:
    :param back:
    :param mode:
    :param sep: string inserted between values, default a space.
    :param end: string appended after the last value, default a newline.
    :param handle: str, "stdout" or "stderr"
        note:the stderr haven't be tested.
    :param flush: whether to forcibly flush the stream.
    :param continuous: default True, if True, the return value will be a lambda method wrapped the uprint mathod
                and the options.
    :return: uprint method, you can use
        uprint()()()() to output strings with diff color.
    '''
    args = [str(i) for i in args]
    if in_win() and in_terminal():
        cprint(args, fore=fore, back=back,sep=sep,end=end, handle=handle, flush=flush)
    else:
        eprint(args,fore=fore,back=back,mode=mode,sep=sep,end=end,handle=handle,flush=flush)

    def extendprint(*args,
           fore=fore,
           back = back,
           mode = mode,
           sep=sep,
           end=end,
           handle = handle,
           flush = flush):
        return uprint(*args,fore=fore,back=back,mode=mode,sep=sep,end=end,handle=handle,flush=flush)

    return extendprint