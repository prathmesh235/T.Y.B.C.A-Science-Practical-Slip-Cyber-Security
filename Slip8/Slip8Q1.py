STEGANOGRAPHY AND ITS DIFFERENCE FROM CRYPTOGRAPHY
Q. Define Steganography and distinguish it clearly from Cryptography. [10 Marks]

1. STEGANOGRAPHY
Steganography is the art and science of hiding a secret message inside an ordinary-looking carrier (such as an image, audio, video or text file) so that the very existence of the message is not noticed. The word comes from Greek: steganos (covered) + graphia (writing).
Working: Secret message + Cover file (image) -> Embedding algorithm -> Stego file (looks normal) -> Extraction -> Secret message
Types / techniques:
- Image steganography: hiding bits in the least significant bits (LSB) of pixels.
- Audio / video steganography: hiding data in sound or video frames.
- Text steganography: hiding data in spaces, word patterns or formatting.
- Network steganography: hiding data in unused packet header fields.
Example: A secret text is hidden in the pixel bits of a normal photo and sent by email. Anyone seeing the photo notices nothing unusual.

2. CRYPTOGRAPHY
Cryptography is the technique of converting a readable message (plaintext) into an unreadable form (ciphertext) using an algorithm and 
a key, so that only the intended receiver can read it. The message is visible, but its meaning is hidden.
Example: "HELLO" becomes "KHOOR" using a Caesar cipher (shift 3), or a file is encrypted with AES.

