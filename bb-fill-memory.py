import time
import psutil


"""
這個程式會在幾秒內盡可能吃光記憶體
用來強迫Windows釋放或管理記憶體
"""


def fill_memory():

    KEEP_TIME = 15                  # 持續 (s)
    KEEP_FREE = 256 * 1024 * 1024   # 保留 (MB)
    BLOCK_SIZE = 128 * 1024 * 1024  # 每次吃 (MB)

    memory = []
    t_0 = time.time()

    while time.time() - t_0 < KEEP_TIME:

        if psutil.virtual_memory().available > KEEP_FREE + BLOCK_SIZE:

            memory.append(bytearray(BLOCK_SIZE))

            print(f"Available: {psutil.virtual_memory().available / 1024**3:.2f} GB")


if __name__ == "__main__":

    fill_memory()