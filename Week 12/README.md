# Introduction to Cryptography

## 1. Cryptology

### 1.1 Cryptography ()

### 1.2 Cryptonalysis ()

## 2. Security Services premitives

- Confidentiality -> Encryption
- Integrity -> Hash
- Authenticity -> MAC
- Accountability -> Digitial Signature

## 3. Ciphersystem

Plain text là dữ liệu nguồn k phải là chỉ là các ký tự.

### 3.1 Symmetric

Khóa dùng gì thì mở khóa dùng chính nó.

Cần sử dụng key exchange để share key với nhau.

### 3.2 Asymmetric

Ngược lại so với Symmetric.

Sử dụng 2 loại key là public key và private key.

Bob gửi plain text cho Alice được mã hóa bằng public key, Alice sau khi nhận được tin nhắn được mã hóa sẽ giải mã bằng private key.

Vấn đề của asymmetric là vì public key thì sẽ bị kẻ mạo danh dùng public key để gửi tin mạo danh cho Bob/Alice để lấy được thông tin.

Sử dụng PKI để đảm bảo Public key chính xác là của người dùng chứ không phải do bên thứ 3 mạo danh. Hoặc dùng CA.

## 4. Stream Cipher & Block Cipher

Block cipher là phương pháp chia plain text thành các block khác nhau để xử lý (mã hóa), từ đó giải mã hay so sánh bằng các block.

Stream cipher là phương pháp sử dụng plain text thành (các) chuỗi để mã hóa.

## 5. CryptoAttack

### 5.1 Bruteforce (vắt cạn)

### 5.2 Cryptoanlysis (khám mã)

## 6. Traditional Ciphers



