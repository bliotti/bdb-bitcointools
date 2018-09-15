
# Genereate Bitcoin testnet public addresses from a arbitrary secret.

## imports

# Secp256k1 Curve and constants in sextuple form 
from pycoin.ecdsa import generator_secp256k1 as g

# Convert binary to ascii and vise versa
from binascii import hexlify,unhexlify

# Encoding base58 format and hash160
from pycoin.encoding import b2a_hashed_base58,hash160



## create random secret for seeding you test net address
secret = 8675309 # example
x,y = (secret*g).pair()
pub = g.__class__(g.curve(), x,y)
hex_x = hex(x)
hex_x = hex_x[2:]
hex_x = hex_x[:-1]
hex_y = hex(y)
hex_y = hex_y[2:]
hex_y = hex_y[:-1]

#confirm it is an odd number
y % 2 #odd

#compressed and y % 2 =1 so odd -> preprend 03
sec = '03' + hex_x
sec_bin = unhexlify(sec)
h160 = hash160(sec_bin)
address_unicode = b2a_hashed_base58(chr(0x6f) + h160)
address = str(address_unicode)

#uncompressed
sec = '04' + hex_x + hex_y
sec_bin = unhexlify(sec)
h160 = hash160(sec_bin)
addres  = str(b2a_hashed_base58(chr(0x6f) + h160))

