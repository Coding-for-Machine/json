import file_write
import req_res
import asyncio
from pprint import pprint
import json

url = ''
async def main():
    async for i in file_write.read_line():
        await asyncio.sleep(0.2)
        pprint(json.dumps(i, indent=2))

if __name__ in "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as k:
        print("EXIT")
