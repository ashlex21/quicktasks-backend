import redis
import json
import os
from . import models

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def task_cache_key(user_id: int):
    return f"user:{user_id}:tasks"

def get_cached_tasks(user_id: int):
    data = r.get(task_cache_key(user_id))
    if data:
        return json.loads(data)
    return None

def set_cached_tasks(user_id: int, tasks: list[models.Task]):
    serialized = [
        {"id": t.id, "name": t.name, "is_done": t.is_done, "user_id": t.user_id}
        for t in tasks
    ]
    r.set(task_cache_key(user_id), json.dumps(serialized), ex=300)  # expires in 5 min

def invalidate_tasks_cache(user_id: int):
    r.delete(task_cache_key(user_id))
