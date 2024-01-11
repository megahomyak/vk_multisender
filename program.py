from vkbottle import User
from random import randint
from hampst import *

ids = ints(read("profile_ids.txt").splitlines())

message = read("message.txt")
user_token = read("user_token.txt")

async def main():
    client = User(token=user_token)
    for peer_id in ids:
        await client.api.messages.send(
            message=message,
            peer_id=peer_id,
            random_id=randint(-1_000_000, 1_000_000)
        )
        await asyncio.sleep(0.25)

asyncio.run(main())
