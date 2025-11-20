# Information Security Lab Portfolio

## Lab 1: Apache Web Server Installation & Maintenance

### Objectives
- Install, administer and maintain an Apache web server
- Set up virtual hosts for multiple websites
- Host dynamic websites using HTML and JavaScript

### Tasks Completed

#### Task 1: Setting up Apache Web Server
- Installed Apache2 on Ubuntu using WSL
- Configured firewall settings
- Tested web server functionality
- Mapped custom domain `webserverlab.com` to localhost

![Lab 1 Setup](https://github.com/fsRakib/INS-Lab/blob/main/Lab1/lab1.jpg)

**Key Commands:**
```bash
sudo apt update
sudo apt install apache2
sudo ufw allow 'Apache'
sudo systemctl status apache2
```

#### Task 2: Setting up Virtual Hosts
- Created virtual hosts for `example.com` and `anothervhost.com`
- Configured directory structures and permissions
- Enabled/disabled sites using `a2ensite` and `a2dissite`
- Tested multiple domain hosting on single server

**Virtual Host Configuration:**
```apache
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/example.com/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

#### Task 3: Dynamic Website Hosting
- Created interactive websites with HTML forms
- Implemented JavaScript for client-side processing
- Deployed on virtual hosts with different functionality

---

## Lab 2: Attacking Classic Crypto Systems

### Objectives
- Break Caesar cipher using brute force attack
- Break substitution ciphers using frequency analysis
- Understand weaknesses in classical cryptography

### Tasks Completed

#### Checkpoint 1: Caesar Cipher Attack
- Implemented brute force attack trying all 25 possible shifts
- Successfully decrypted ciphertext using shift 10
- Plaintext: **"experience is the teacher of all things"**

![Lab 2 Cryptanalysis](https://github.com/fsRakib/INS-Lab/blob/main/Lab1/lab2.jpg)

**Python Implementation:**
```python
def break_caesar(ciphertext):
    for shift in range(1, 26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                plaintext += shifted
        print(f"Shift {shift}: {plaintext}")
```

#### Checkpoint 2: Substitution Cipher Attack
- Performed frequency analysis on ciphertexts
- Mapped most frequent cipher characters to English letters
- Identified common words and patterns
- Successfully decrypted both substitution ciphers

**Frequency Analysis Approach:**
1. Count character frequencies in ciphertext
2. Compare with English language frequency distribution
3. Identify common words (the, and, of, etc.)
4. Iteratively refine the substitution mapping

---

## Lab 3: Symmetric Encryption & Hashing

### Objectives
- Perform symmetric encryption using OpenSSL
- Understand different encryption modes (ECB, CBC, CFB, OFB)
- Generate message digests and HMAC
- Study cryptographic properties

### Tasks Completed

#### Task 1: AES Encryption with Different Modes
- Encrypted files using AES-128 in CBC, CFB, and OFB modes
- Verified successful decryption
- Compared encrypted file sizes and properties

**Commands Used:**
```bash
openssl enc -aes-128-cbc -e -in plain.txt -out cipher_cbc.bin \
-K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

#### Task 2: ECB vs CBC Mode Analysis
- Encrypted BMP images using both ECB and CBC modes
- Preserved BMP headers for visualization
- Observed pattern leakage in ECB mode
- Demonstrated CBC mode's superior security

**Observations:**
- **ECB:** Visible patterns in encrypted image
- **CBC:** Completely random appearance

#### Task 3: Error Propagation Study
- Created 64+ byte text files
- Corrupted single bits in encrypted files
- Analyzed error propagation in different modes
- Documented recovery capabilities

#### Task 4: Padding Analysis
- Tested encryption with various file sizes
- Identified padding requirements for different modes
- **ECB/CBC:** Require padding to block size
- **CFB/OFB:** No padding required (stream ciphers)

#### Task 5: Message Digest Generation
- Generated hashes using MD5, SHA-1, SHA-256, SHA-512
- Compared hash lengths and properties
- Documented collision resistance characteristics

#### Task 6: Keyed Hash and HMAC
- Implemented HMAC with MD5, SHA-1, SHA-256
- Tested variable key lengths
- Verified HMAC's key size flexibility

#### Task 7: Hash Properties Analysis
- Demonstrated avalanche effect
- Flipped single bit in input file
- Observed completely different hash outputs
- Implemented bit difference calculator (Bonus)

---

## Lab 4: Programming Symmetric & Asymmetric Crypto

### Objectives
- Implement cryptographic operations in Python
- Build AES encryption/decryption with multiple modes
- Implement RSA operations and digital signatures
- Measure and analyze cryptographic performance

### Tasks Completed

#### Task 1: AES Encryption/Decryption (5 Marks)
**Implementation Features:**
- 128-bit and 256-bit key support
- ECB and CFB modes
- Automatic key generation and storage
- PKCS7 padding for block modes

**Code Structure:**
```python
def aes_encrypt(self, input_file, output_file, key_size, mode):
    key = self.aes_128_key if key_size == 128 else self.aes_256_key
    if mode.upper() == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
```

#### Task 2: RSA Encryption/Decryption (4 Marks)
**Implementation Features:**
- 2048-bit RSA key generation
- PKCS1_OAEP padding
- PEM format key storage
- Public key encryption, private key decryption

#### Task 3: RSA Signature (4 Marks)
**Implementation Features:**
- PKCS#1 v1.5 signature scheme
- SHA-256 message digest
- Signature generation and verification
- Separate signature file storage

#### Task 4: SHA-256 Hashing (3 Marks)
**Implementation Features:**
- File content hashing
- Hexadecimal digest output
- Integration with RSA signatures
- Performance timing

#### Task 5: Performance Measurement (4 Marks)
**Analysis Results:**
- **AES:** Near-constant time across key sizes (128-256 bits)
- **RSA:** Exponential time increase with larger keys
- **Observation:** Symmetric crypto significantly faster than asymmetric

**Performance Visualization:**
- Generated comparative plots for AES vs RSA
- Analyzed time complexity trends
- Provided practical crypto selection guidelines

### Program Usage
```bash
# Install dependencies
pip install pycryptodome matplotlib

# Run cryptographic operations
python crypto_program.py --aes-encrypt input.txt output.bin ECB
python crypto_program.py --rsa-sign document.txt signature.bin
python crypto_program.py --sha256 file.txt
python crypto_program.py --performance
```

---

## Technical Skills Demonstrated

### System Administration
- Linux/Ubuntu environment management
- Apache web server configuration
- Firewall and service management
- Virtual host setup and DNS mapping

### Cryptography
- Classical cipher cryptanalysis
- Modern symmetric encryption (AES)
- Asymmetric cryptography (RSA)
- Hash functions and digital signatures
- Cryptographic mode understanding

### Programming
- Python implementation of crypto algorithms
- Command-line interface development
- File I/O and binary data handling
- Performance measurement and visualization

### Security Analysis
- Vulnerability assessment of crypto systems
- Error propagation analysis
- Performance vs security trade-offs
- Practical attack implementations

---

## Tools and Technologies Used

- **Operating System:** Windows 10 with WSL/Ubuntu
- **Web Server:** Apache2
- **Cryptography:** OpenSSL, PyCryptodome
- **Programming:** Python 3, Bash scripting
- **Analysis:** Frequency analysis, Performance profiling
- **Visualization:** Matplotlib for performance plots

---

## Key Learnings

1. **Web Security:** Understanding web server architecture and virtual hosting
2. **Cryptanalysis:** Practical experience breaking classical ciphers
3. **Modern Crypto:** Hands-on implementation of AES, RSA, and hash functions
4. **Performance:** Quantitative analysis of cryptographic operations
5. **Security Principles:** Trade-offs between security, performance, and usability

---

This portfolio demonstrates comprehensive understanding of information security principles from classical cryptanalysis to modern cryptographic implementations.
