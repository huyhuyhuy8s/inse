# Authentication and Access Control

Table off

## Authentication

### Goal

Confusion matrix (Learned in Machine Learning)

|            |         | Predict        |                |
| ---------- | ------- | -------------- | -------------- |
|            |         | Dog            | Not Dog        |
| **Actual** | Dog     | True Positive  | False Negative |
|            | Not Dog | False Positive | True Negative  |

### Types

- Something you know: Password, PIN, OTP,...
- Something you have: Phone, ATM, Credit Cards,..
- Something you are: Fingerprint, Face Authentication,...

### Factors

- Single
- Two
- Multiple

### Trusted Path

Là đừng dẫn đáng tin cậy từ user đế authenticator để đảm bảo an toàn cho xác thực.

### Password Authentication

#### Keys vs Passwords

| Crypto Keys                            | Passwords                                                      |
| -------------------------------------- | -------------------------------------------------------------- |
| Key is 64 bits                         | Password are 8 characters, and 256 different characters        |
| Then 2^64 keys                         | Then 2568 = 2^64 pwds                                          |
| Choose key at random...                | Users do not select passwords at random                        |
| Then attacker must try about 2^63 keys | Attacker has far less than 263 pwds to try (dictionary attack) |

#### Implementing Password Authentication

linux:

- username /etc/passwd
- password /etc/shadow

### Biometric

Đọc thêm cho vui :skull:

## Access Control

### Requirements

### Policies

- DAC: Discretionary Access Control - Kiểm soát truy cập không bắt buộc
- MAC: Mandatory Access Control - Kiểm soát truy cập bắt buộc
- RBAC: Role-based Access Control - Kiểm soát truy cập dựa trên phân quyền
- Rule-based Access Control - Kiểm soát truy cập dựa trên luật lệ

### Access Control Elements (ACE)

- Subjects
- Objects
- Access right

|         |        | object |        |        |
| ------- | ------ | ------ | ------ | ------ |
|         |        | file 1 | file 2 | file 3 |
|         | user a | -rw-   |        |        |
| subject | user b |        | -r-x   |        |
|         | user c | -r-x   |        | -r-x   |

#### Access Control Matrix (ACM)

- C-list (Combabilities list) Sort by Subjects
- ACL (Access Control List) Sort by Objects

