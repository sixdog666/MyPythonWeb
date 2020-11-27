import asyncio

import orm

from models import User,Blog,Comment

async def test(loop):

    await orm.create_pool(loop, user='www-data', password= 'www-data', db='awesome')

    u = User(id='02', name='song', email = 'test@example.com', admin=False, passwd='1234567890', image='about:blank', create_at=0.2)

    await u.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    loop.run_until_complete(test(loop))

    print('test finished')

    loop.close()