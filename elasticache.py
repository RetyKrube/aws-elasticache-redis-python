# Import the Redis package
import redis

redisEndpoint = 'YOUR_REDIS_ENDPOINT'
# Get the port and host from the endpoint string
PORT = redisEndpoint[-4:];
HOST = redisEndpoint[:-5];

# Configure Redis connection
def config_redis_connection():
    r = redis.Redis(
        host=HOST,
        port=PORT)
    print('Configured Redis node connection: ')
    print(r)
    return r

# Write to Redis cluster
def write_redis_key(r, new_key, new_value):
    temp_success = r.set(new_key, new_value)
    if temp_success:
        print('Successfully wrote to Redis')
        # set expiry time
        temp_success2 = r.expire(new_key, 30)
        if temp_success2:
            print('Successfully set expiry time')
        else:
            print('Unsuccessful key does not exist')
            
# Read from Redis cluster
def read_redis_key(r, new_key):
    temp_success = r.get(new_key)
    if temp_success:
        print('Value of ' + new_key + ' = ' + temp_success.decode("utf-8") )
    else:
        print('Unsuccessful key does not exist')
        
# Write object to Redis cluster
def write_redis_object(r, new_key, new_object):
    temp_success = r.hmset(new_key, new_object)
    if temp_success:
        print('Successfully wrote object to Redis')
        
# Read object from Redis cluster
def read_redis_object(r, new_key):
    temp_success = r.hgetall(new_key)
    if temp_success:
        print('Value of ' + new_key + ' :')
        print(temp_success)
        
# Main program
def main():
    redis_connection = config_redis_connection()
    write_redis_key(redis_connection, 'myHighScore', 1000)
    read_redis_key(redis_connection, 'myHighScore')
    temp_obj = {
        'info1': 'This is info 1',
        'info2': 'This is info 2',
        'info3': 'This is info 3'
    }
    write_redis_object(redis_connection, 'myInfo', temp_obj)
    read_redis_object(redis_connection, 'myInfo')
    
if __name__ == '__main__':
    main()
