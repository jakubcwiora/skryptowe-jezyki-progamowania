def xor_encrypt(plaintext: str, key: str) -> str:
  if len(plaintext) != len(key):
    raise ValueError("Plaintext and key must be of the same length.")
  ciphertext = ""
  for p, k in zip(plaintext, key):
    ciphertext += chr(ord(p) ^ ord(k))
  return ciphertext


def xor_decrypt(ciphertext: str, key: str) -> str:
  return xor_encrypt(ciphertext, key)  # XOR is symmetric


if __name__ == "__main__":
  plaintext = "algorytm"
  key = "kodykody"
  encrypted = xor_encrypt(plaintext, key)
  print(f"Encrypted: {encrypted}")
  decrypted = xor_decrypt(encrypted, key)
  print(f"Decrypted: {decrypted}")
