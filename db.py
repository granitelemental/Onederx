import json
from datetime import datetime, timedelta, timezone
import redis

import config


class Data():

    def __init__(self):
        self.conn = redis.Redis(config.REDIS_HOST, config.REDIS_PORT)
        self.tz = timezone(offset=timedelta(0))
        print("connected to redis:", self.conn.ping(), " host:", config.REDIS_HOST, " port:", config.REDIS_PORT)


    def save(self, data):
        date, description = data["date"], data["description"]
        data = {
            f'{description}:{date}': date
        }
        self.conn.zadd("alarm", data)
        return {"status": "data added", "data": data}, 200
        

    def current_time(self):
        return datetime.now(tz=self.tz).timestamp()//1


    def get_active(self):
        current_time = self.current_time()
        res = self.conn.zrangebyscore("alarm", current_time, "+inf", withscores=True)
        res = [
            {
                "description": r[0].decode().split(":")[0],
                "date": r[1]
            } for i, r in enumerate(res)
        ]
        return {"status": "Ok", "data": res}, 200


    def clear_db(self):
        self.conn.flushdb()
        return {"status": "db is cleared"}, 200


    def check_if_time(self):
        current_time = self.current_time()
        res = self.conn.zrangebyscore("alarm", current_time, current_time, withscores=True)
        if res:
            return {
                    "description": res[0][0].decode().split(":")[0],
                    "date": res[0][1]
            }
