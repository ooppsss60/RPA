from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import pyautogui
import logging
import time
from worker import Worker

worker = Worker()


def on_move(x, y):
    logging.info(f'Mouse moved to ({x}, {y})')


@worker.task
def on_click(x, y, button, pressed):
    if pressed:
        pyautogui.screenshot(f'screenshots/{time.time()}.png')
        logging.info(f'Mouse clicked at ({x}, {y}) with {button}')


def on_scroll(x, y, dx, dy):
    logging.info(f'Mouse scrolled at ({x}, {y})({dx}, {dy})')


def on_press(key):
    logging.info(f'{key} pressed')


def on_release(key):
    logging.info(f'{key} release')


class Listener:
    def __init__(self):
        self.keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
        self.mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move)

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
