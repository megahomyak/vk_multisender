from vkbottle import User
import asyncio
from random import randint

ids = [int(id_) for id_ in open("profile_ids.txt").read().strip().splitlines()]

PEER_IDS_LIMIT = 100

user_batches = [
    ids[i:i + PEER_IDS_LIMIT]
    for i in range(0, len(ids), PEER_IDS_LIMIT)
]

message = open("message.txt").read().strip()
user_token = open("user_token.txt").read().strip()

async def main():
    client = User(token=user_token)
    for user_batch in user_batches:
        await client.api.messages.send(
            message=message,
            peer_ids=user_batch,
            random_id=randint(-1_000_000, 1_000_000)
        )
        await asyncio.sleep(1)

asyncio.run(main())
