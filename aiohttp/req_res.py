import aiohttp

# get data
async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()

async def get_data_id(url, post_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/{post_id}") as response:
            if session.status==200:
                return await response.json()
            else:
                return await response.status
            
# post data 
async def post_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status==201:
                return await response.json()
            else:
                return await response.status
            
# put data
async def put_data(url, post_id, data):
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{url}/{post_id}", json=data) as response:
            if response.status==200:
                return await response.json()
            else:
                return await response.status
            
# delete data
async def delete_data(url, post_id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{url}/{post_id}") as response:
            if response.status==200:
                return await response.json()
            else:
                return await response.status
            
