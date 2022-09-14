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
        
# Main program
def main():
    redis_connection = config_redis_connection()
    write_redis_key(redis_connection, 'myHighScore', 1000)
if __name__ == '__main__':
    main()
