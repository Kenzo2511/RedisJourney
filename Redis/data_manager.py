import redis
import json

def conver_dict_to_json(data):
    json_data = json.dumps(data)
    return json_data

class RedisManager():
    def __init__(self):
        self.redis_client = redis.Redis( host = "localhost", port = 6379, db = 0 )

    def _set_info_to_redis(self, data):
        cache_key = f"Players:{data['key']}"
        self.redis_client.set(cache_key, conver_dict_to_json(data))

    def _get_info_from_redis(self, data):
        cache_key = f"Players:{data['key']}"
        return self.redis_client.get(cache_key)

    def _remove_info_to_redis(self, data):
        cache_key = f"Players:{data['key']}"
        return self.redis_client.delete(cache_key)

    