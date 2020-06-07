# Pandanda Decryptor

Pandanda Decryptor is used to decrypt Pandadna's Adobe Flash assets.

Pandanda uses a very simple XOR algorithm to protect its game assets. Using this tool, it is trivial to convert every Pandadna SWF to a readable format.

## Installation

Your Python version must be at least 3.6, but newer versions are much appreciated.

You must clone the repository. This project has no dependencies.

```
git clone https://github.com/darktohka/PandandaDecryptor
cd PandadnaDecryptor
```

## Running

On Windows, simply run `start.bat` to decrypt all SWFs in your current directory into a folder named `decrypted`.

It is also possible to specify the source and target directory on the command line.

```
usage: python -m pandandadecryptor.Main [-h] [--key KEY] [source] [target]

positional arguments:
  source             The source folder, containing your encrypted SWF.
  target             The target folder, where the decrypted SWFs will be saved.

optional arguments:
  -h, --help         show this help message and exit
  --key KEY, -k KEY  The Pandanda SWF decryption key.
  
example:
  python -m pandandadecryptor.Main C:/Pandanda C:/Pandanda/decrypted
```