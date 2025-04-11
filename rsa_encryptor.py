import rsa

def generate_keys(key_size=512):
    """Генерация RSA-ключей (публичный и приватный)"""
    pubkey, privkey = rsa.newkeys(key_size)
    return pubkey, privkey

def save_keys(pubkey, privkey):
    """Сохранение ключей в файлы"""
    with open('pubkey.pem', 'wb') as f:
        f.write(pubkey.save_pkcs1())
    with open('privkey.pem', 'wb') as f:
        f.write(privkey.save_pkcs1())
    print("🔑 Ключи сохранены в pubkey.pem и privkey.pem")

def encrypt_file(input_file, output_file, pubkey):
    """Шифрование файла с помощью RSA"""
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, pubkey)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f"🔒 Файл '{input_file}' зашифрован и сохранен как '{output_file}'")

if __name__ == "__main__":
    print("🔐 RSA File Encryptor")
    pubkey, privkey = generate_keys()
    save_keys(pubkey, privkey)
    encrypt_file('secret.txt', 'secret_encrypted.txt', pubkey)