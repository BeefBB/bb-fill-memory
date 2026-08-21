import time
import argparse
import psutil


def fill_memory(keep_time=15, keep_free=256, block_size=128):
    """
    Args:
        keep_time:  持續時間 (s)
        keep_free:  保留記憶體空間 (MiB)
        block_size: 每次增加記憶體量 (MiB)
    """

    keep_free *= 1024 ** 2
    block_size *= 1024 ** 2

    memory = []
    t_0 = time.monotonic()

    while time.monotonic() - t_0 < keep_time:

        if psutil.virtual_memory().available > keep_free + block_size:

            memory.append(bytearray(block_size))

            print(f"Available: {psutil.virtual_memory().available / 1024**3:.2f} GB")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--time",
        type=float,
        default=15,
        help="持續時間 (s)"
    )

    parser.add_argument(
        "--free",
        type=int,
        default=256,
        help="保留記憶體空間 (MiB)"
    )

    parser.add_argument(
        "--block",
        type=int,
        default=128,
        help="每次增加記憶體量 (MiB)"
    )

    args = parser.parse_args()


    fill_memory(args.time, args.free, args.block)