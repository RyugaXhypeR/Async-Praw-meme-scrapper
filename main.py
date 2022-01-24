import asyncpraw
import asyncio
import requests
import random


SUBREDDIT = '' # the subreddit from which you want the memes.
TOTAL_MEMES =   # the initial amount of memes the bot picks up.
FOLDER_NAME = '' # the folder you are gonna store memes in (is needed to be created before hand)
VALID_SYM = 'abcdefghijklmnopqrstuvwxyz' # to avoid naming errors 
LIMIT =  # the amount memes you want to store in the folder


async def main():
    # create an application here - https://www.reddit.com/prefs/apps to get access to this
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
            if j.lower() not in VALID_SYM:
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
