import os

SWF_MAGIC = b'CWS'

class PandandaDecryptor(object):

    def __init__(self, key):
        if isinstance(key, str):
            key = list(key.encode('utf-8'))
        elif isinstance(key, bytes):
            key = list(key)

        self.key = key

    def is_decryptable(self, filename):
        if not filename.lower().endswith('.swf'):
            return False

        with open(filename, 'rb') as f:
            return f.read(len(SWF_MAGIC)) != SWF_MAGIC

    def decrypt_bytes(self, swf):
        l = len(self.key)
        result = bytes([k ^ self.key[i % l] for i, k in enumerate(swf)])

        if result[:len(SWF_MAGIC)] != SWF_MAGIC:
            raise Exception('Incorrect SWF or decryption key.')

        return result

    def decrypt_file(self, source_filename, target_filename):
        with open(source_filename, 'rb') as source:
            with open(target_filename, 'wb') as target:
                target.write(self.decrypt_bytes(source.read()))

    def decrypt_folder(self, source_folder, target_folder):
        source_folder = source_folder.strip('\\/')
        target_folder = target_folder.strip('\\/')

        if source_folder == target_folder:
            raise Exception('Target folder cannot be the same as the source folder!')

        for root, _, files in os.walk(source_folder):
            for file in files:
                source_file = os.path.join(root, file)

                if not self.is_decryptable(source_file):
                    continue

                target_root = os.path.join(target_folder, root[len(source_folder) + 1:])

                if not os.path.exists(target_root):
                    os.makedirs(target_root)

                target_file = os.path.join(target_root, file)
                print('Decrypting...', source_file)

                try:
                    self.decrypt_file(source_file, target_file)
                except Exception as e:
                    print('Decryption failed:', e, source_file)