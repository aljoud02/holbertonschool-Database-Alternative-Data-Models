import time
import fakeredis

# connect to fake redis database
r = fakeredis.FakeStrictRedis(decode_responses=True)
print("WhatsApp Server Connected")

# save phone and code
phone = "+966559662026"
otp = "0966"
r.set(phone, otp, ex=3)
print("[Insert] Code created successfully")

# read code immediately
print("[Read] Code is:", r.get(phone))

# wait for timeout
print("Waiting 4 seconds...")
time.sleep(4)

# test ttl deletion feature
print("[TTL] Code after delay:", r.get(phone))
