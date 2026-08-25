import time
import argparse
import psutil


def fill_memory(keep_time=15, keep_free=256, block_size=128, time_out=25):
    """
    Args:
        keep_time:  持續時間 (s)
        keep_free:  保留記憶體空間 (MiB)
        block_size: 每次增加記憶體量 (MiB)
        time_out:   逾時中斷時間 (s)
    """

    if time_out < keep_time:
        print(f"警告: 逾時中斷時間 < 持續時間")
        print(f"實際不會執行到 {keep_time} 秒, 因為到達前就先中斷了")
        print()


    keep_free *= 1024 ** 2
    block_size *= 1024 ** 2


    t_0 = time.monotonic()
    t_1 = 0
    t_print = time.monotonic()

    reach = False

    memory = []


    while not reach or time.monotonic() - t_1 < keep_time:

        if psutil.virtual_memory().available > keep_free + block_size:

            memory.append(bytearray(block_size))

            if time.monotonic() - t_print > 0.3:

                t_print = time.monotonic()
                print(f"剩餘: {psutil.virtual_memory().available / 1024**3:.2f} GB")

        else:

            if not reach:

                reach = True
                t_1 = time.monotonic()

            time.sleep(0.01)


        if time.monotonic() - t_0 > time_out:
            break


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

    parser.add_argument(
        "--timeout",
        type=int,
        default=25,
        help="逾時中斷時間 (s)"
    )

    args = parser.parse_args()


    fill_memory(args.time, args.free, args.block, args.timeout)