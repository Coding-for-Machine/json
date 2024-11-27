import aiofiles
import json

file_name = "data.json"
# write file
async def write_data(data, filename="data.json"):
    async with aiofiles.open(filename, mode='w') as f:
        # JSON formatiga aylantirib yozish
        await f.write(json.dumps(data, indent=4))
# read file
async def read_data():
    async with aiofiles.open("data.json", mode="r") as f:
        await f.read()

# lina file
async def read_line():
    async with aiofiles.open("data.json", mode='r') as f:
        while line:= await f.read(128):
            yield line