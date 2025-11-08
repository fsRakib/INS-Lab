cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"

def caesar_decrypt(cipher, shift):
    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

for s in range(1, 26):
    print(f"Shift {s}: {caesar_decrypt(cipher, s)}")
