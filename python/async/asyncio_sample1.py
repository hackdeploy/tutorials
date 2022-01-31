import asyncio
import time


#----------SEQUENTIANL FUNCTIONS--------------------------------------------------------------------------
def say_after_simple(delay, what):
    time.sleep(delay)
    print(what)


def main_simple():
    print(f"started at {time.strftime('%X')}")

    say_after_simple(2, 'hello')
    say_after_simple(2, 'world')

    #when finished print. (Should take around 4 seconds)
    print(f"finished at {time.strftime('%X')}")

#----------ASYNC FUNCTIONS--------------------------------------------------------------------------
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(2, 'hello'))

    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":

    #Run using async
    asyncio.run(main())

    #Running sequentially
    main_simple()