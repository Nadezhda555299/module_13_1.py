import asyncio
import time


async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i+1}-й шар')

    print(f'Силач {name} закончил соревнования.')

async def main():
    strong1 = asyncio.create_task(start_strongman('Pasha', 3))
    strong2 = asyncio.create_task(start_strongman('Denis', 4))
    strong3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strong1, strong2, strong3
    print('\nПобедила дружба!')

asyncio.run(main())
