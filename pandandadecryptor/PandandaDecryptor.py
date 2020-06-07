import os

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
            return f.read(3) != b'CWS'

    def decrypt_bytes(self, swf):
        l = len(self.key)
        return bytes([k ^ self.key[i % l] for i, k in enumerate(swf)])

    def decrypt_file(self, source_filename, target_filename):
        with open(source_filename, 'rb') as source:
            with open(target_filename, 'wb') as target:
                target.write(self.decrypt_bytes(source.read()))

    def decrypt_folder(self, source_folder, target_folder):
        source_folder = source_folder.strip(os.sep)
        target_folder = target_folder.strip(os.sep)

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
                self.decrypt_file(source_file, target_file)