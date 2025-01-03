import redis
import json

def convert_dict_to_json(data):
    """
    Converts a dictionary to a JSON string.
    :param data: Dictionary to convert.
    :return: JSON string.
    """
    return json.dumps(data)


class RedisManager:
    def __init__(self, host="localhost", port=6379, db=0):
        """
        Initializes the RedisManager with connection details.
        :param host: Redis server host.
        :param port: Redis server port.
        :param db: Redis database index.
        """
        self.redis_client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set_info_to_redis(self, data):
        """
        Stores player data in Redis with a team-based key.
        :param data: Dictionary containing player information.
        """
        if "team" not in data or "key" not in data:
            raise ValueError("Data must contain 'team' and 'key' fields.")
        cache_key = f"{data['team']}:{data['key']}"
        self.redis_client.set(cache_key, convert_dict_to_json(data))

    def get_info_from_redis(self, keyword):
        """
        Retrieves all data for a specific keyword from Redis.
        :param keyword: Keyword to search for in Redis keys (e.g., team name).
        :return: List of formatted player information.
        """
        pattern = f"{keyword}:*"
        keys = self.redis_client.keys(pattern)
        info = []

        for key in keys:
            data = self.redis_client.get(key)
            if data:
                player_data = json.loads(data)
                info.append(f"name: {player_data['name']} - position: {player_data['position']} ")
        return info

    def remove_info_from_redis(self, keyword):
        """
        Removes all data for a specific keyword from Redis.
        :param keyword: Keyword to search for in Redis keys (e.g., team name).
        """
        pattern = f"{keyword}:*"
        keys = self.redis_client.keys(pattern)

        for key in keys:
            self.redis_client.delete(key)
        print(f"Deleted all data for keyword: {keyword}")
