import argparse
import asyncio
import moteus
import math 

async def main():
    parser = argparse.ArgumentParser()
    moteus.make_transport_args(parser)
    args = parser.parse_args()

    transport = moteus.get_singleton_transport(args)
    c1 = moteus.Controller(id=1, transport=transport)
    c2 = moteus.Controller(id=2, transport=transport)
    c3 = moteus.Controller(id=3, transport=transport)
    c4 = moteus.Controller(id=4, transport=transport)
    while True:
        results = await transport.cycle([
           c1.make_position(position=math.nan, query=True),
           c2.make_position(position=math.nan, query=True),
           c3.make_position(position=math.nan, query=True),
           c4.make_position(position=math.nan, query=True),
           
           ])
        
        print(", ".join(
            f"{x.source} " +
            f"{x.values[moteus.Register.POSITION]}"
            for x in results))

        await asyncio.sleep(0.01)

if __name__ == '__main__':
    asyncio.run(main())