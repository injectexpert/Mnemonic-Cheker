# Mnemonic-Cheker
#### Mnemonic Cheker which generates mnemonic phrases and checks their addresses against a database in .txt format. If there is a match, a separate file is created.

For this code to work, you need to install the following dependencies:
- bip32utils` (installation via `pip install bip32utils)
- mnemonic` (installation via `pip install mnemonic)

Replace `'database.txt'` in the `check_addresses` function call with the path to your database file.
The database expects each address to be written on a new line.

The `create_file_with_mnemonic` function, which creates a file with a mnemonic phrase if a matching address is found.
A file will be created for each found address and will be named like `found_mnemonic_{address}.txt`. The phrase will be written to a file.
After displaying the found addresses on the screen, the code will create the corresponding files with mnemonic phrases if matches are found.
The files will be created in the same directory where the script is run.
Make sure you have a database file with addresses and its path is correct in the code (replace `'database.txt'` with the appropriate path to your file).

## Contact Me on telegram or twitter: https://twitter.com/injectexp / https://t.me/inject_exp
