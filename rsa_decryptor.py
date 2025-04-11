import rsa

def load_private_key(key_file='privkey.pem'):
    """Загрузка приватного ключа из файла"""
    with open(key_file, 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())
    return privkey

def decrypt_file(input_file, output_file, privkey):
    """Дешифрование файла"""
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = rsa.decrypt(encrypted_data, privkey)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    print(f"🔓 Файл '{input_file}' расшифрован и сохранен как '{output_file}'")

if __name__ == "__main__":
    print("🔐 RSA File Decryptor")
    privkey = load_private_key()
    decrypt_file('secret_encrypted.txt', 'secret_decrypted.txt', privkey)