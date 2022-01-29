import asyncpraw
import asyncio
import requests
import random
from string import ascii_letters

SUBREDDIT = ''
TOTAL_MEMES = 
FOLDER_NAME = ''
VALID_SYM = ascii_letters
LIMIT = 


async def main():
    reddit = asyncpraw.Reddit(
        client_id='',
        client_secret='',
        username='',
        user_agent='',
    )

    subreddit = await reddit.subreddit(SUBREDDIT)
    lim = subreddit.hot(limit=TOTAL_MEMES)
    all_sub = []

    async for i in lim:
        all_sub.append(i)

    submission = random.sample(all_sub, LIMIT)
    for i in range(LIMIT):

        title = submission[i].title
        url = submission[i].url

        for j in title:
            if j not in VALID_SYM:
                title = title.replace(j, '-')

        print(f"{i+1}. {url}")
        request_url = requests.get(url).content
        with open(f'{FOLDER_NAME}/{title}.jpg', 'wb+') as f:
            f.write(request_url)

        await reddit.close()

#event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
