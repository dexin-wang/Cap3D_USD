import os
from cryptography.fernet import Fernet
from tqdm import tqdm

KEY_PATH = 'data/omnigibson.key'
with open(KEY_PATH, "rb") as filekey:
    key = filekey.read()
fernet = Fernet(key)
def decrypt_file(encrypted_filename, decrypted_filename):
    with open(encrypted_filename, "rb") as enc_f:
        encrypted = enc_f.read()

    decrypted = fernet.decrypt(encrypted)

    with open(decrypted_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)



# encrypted_filename = '/home/wdx/research/omnigibson_data/data/og_dataset/objects/fridge/hzgqdn/usd/hzgqdn.encrypted.usd'
# decrypted_filename = '/home/wdx/research/omnigibson_data/data/og_dataset/objects/fridge/hzgqdn/usd/hzgqdn.usd'
# decrypt_file(encrypted_filename, decrypted_filename)
        
objects_path = '/home/wdx/research/omnigibson_data/data/og_dataset/objects'
categoryes = os.listdir(objects_path)
for category in tqdm(categoryes):
    category_path = os.path.join(objects_path, category)
    idxes = os.listdir(category_path)
    for idx in idxes:
        encrypted_usd_path = os.path.join(category_path, idx, 'usd', f'{idx}.encrypted.usd')
        decrypted_usd_path = encrypted_usd_path.replace('encrypted.usd', 'usd')
        if os.path.exists(decrypted_usd_path):
            continue
        else:
            try:
                decrypt_file(encrypted_usd_path, decrypted_usd_path)
            except:
                print('Error: ', encrypted_usd_path)