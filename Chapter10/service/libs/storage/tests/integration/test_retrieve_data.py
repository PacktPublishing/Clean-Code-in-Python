from storage import DeliveryStatusQuery, DBClient
import asyncio


loop = asyncio.get_event_loop()


async def main():
    client = await DBClient()
    dsq = DeliveryStatusQuery(1, client)
    result = await dsq.get()

    print(">>>>>>>>>>>>>", result.message())
    r = await DeliveryStatusQuery(99, client).get()
    print(r.message())


loop.run_until_complete(main())
