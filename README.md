# Encryption and Decryption Using RSA and DES
This project demonstrates a secure hybrid encryption system where an image file is encrypted using the DES (Data Encryption Standard) algorithm, and the DES key itself is secured using RSA encryption. The workflow includes user input of an 8-character DES key, RSA keypair generation using large prime. The encrypted DES key and image are conceptually transmitted over a network then decrypted using the RSA private key and DES decryption to verify the original image's integrity. The project highlights how hybrid encryption leverages RSA for secure key exchange and DES for efficient bulk data encryption, combining cryptographic strength and speed.
