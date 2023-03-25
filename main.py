import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client

from modules import config as config_lib

config = config_lib.TomlConfig()

session_name = config.get_str("session", "name")
api_id = config.get_int("api", "id")
api_hash = config.get_str("api", "hash")


client = Client(name=session_name, api_id=api_id, api_hash=api_hash,
                plugins={'root': 'handlers'}, sleep_threshold=7)

logging.basicConfig(filename='logs/main.log', level=logging.ERROR,
                    format='%(asctime)-4s %(name)-8s %(levelname)-8s %(message)s', datefmt='%d.%m.%d %H:%M')

scheduler = AsyncIOScheduler()

# scheduler.add_job(job_func, 'interval', seconds=7, args=(arg1, arg2, arg3))

scheduler.start()

client.run()
