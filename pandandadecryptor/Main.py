from .PandandaDecryptor import PandandaDecryptor
import argparse

DEFAULT_KEY = b'd02adaa4cf8fe4859fda09ae936aadbf138001925203340fa89d6c99b546d97e'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', '-k', default=DEFAULT_KEY, help='The Pandanda SWF decryption key.')
    parser.add_argument('source', nargs='?', default='.', help='The source folder, containing your encrypted SWF.')
    parser.add_argument('target', nargs='?', default='decrypted', help='The target folder, where the decrypted SWFs will be saved.')
    args = parser.parse_args()

    tool = PandandaDecryptor(args.key)
    tool.decrypt_folder(args.source, args.target)

if __name__ == '__main__':
    main()