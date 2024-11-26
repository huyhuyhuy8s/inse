# In[0]: Import libs
import hashlib
import binascii
import hlextend

# In[1]: Choose a hash function (SHA-1)
def p(y ,x):
    print(y, ":", binascii.hexlify(x))
hash_func = hashlib.sha1

p('sha1', hash_func(b'hello').digest())

sha = hlextend.new('sha1')
print(sha.extend(b'file', b'hello', 10, '52e98441017043eee154a6d1af98c5e0efab055c'))
b'hello\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00xfile'
print(sha.hexdigest())

# In[2]: Create your secret key and message
message = b'Hello'
secret_key = b'Key'

hash1 = hash_func(secret_key + message).digest()
p("MAC1", hash1)
print("Message", message)

sec_message = b'mono'

hash2 = hash_func(hash1 + sec_message).digest()
p('MAC2', hash2)
print("Message", message + sec_message)

p("Check", hash_func(secret_key + message + sec_message).digest())
# In[3]: Block size and padding
if len(secret_key) > hash_func().block_size:
    secret_key = hash_func(secret_key).digest() #In Python, a digest is the result of applying a hash function (such as SHA-256 or MD5) to the content of a file.
secret_key = secret_key.ljust(hash_func().block_size, b'\0')

p("Key", secret_key)
p("Message", message)


# In[4]: Inner and outer padding
Si = bytearray((x ^ 0x36) for x in secret_key)
So = bytearray((x ^ 0x5c) for x in secret_key)

p("Si", Si)
p("So", So)


# In[5]: Inner hash
inner_hash = hash_func(Si + message).digest()
p("Si+Message", Si + message)
p("I Hash", inner_hash)


# In[6]: Outer hash
hmac = hash_func(So + inner_hash).hexdigest()
p("So+Inner-Hash: ", So + inner_hash)
print("HMAC:", hmac)

# In[7]: Nested HMAC Hashes
hm = hash_func(So + hash_func(Si + message).digest()).hexdigest()

print("HMAC Nested:", hm)

print("Compare two HMAC:", "Two hashes are {0}the same".format("" if hm == hmac else "not "))
# %%
