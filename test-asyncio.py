import uasyncio as asyncio

async def odd():
    count = 0
    while True:
        print(count)
        count += 2
        await asyncio.sleep(0.5)
        
async def even():
    count = 1
    while True:
        print(count)
        count += 2
        await asyncio.sleep(0.5)

loop = asyncio.get_event_loop()
loop.create_task(odd())
loop.create_task(even())
loop.run_forever()