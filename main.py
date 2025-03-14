import time

import pyautogui
import pyperclip
import keyboard
from spider import get_video


def get_text():
    # 将选中的文本复制到剪贴板
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # 等待复制操作完成
    copied_text = pyperclip.paste()
    get_video(copied_text)
    return copied_text



keyboard.add_hotkey('ctrl+q', get_text)
keyboard.wait('esc')

