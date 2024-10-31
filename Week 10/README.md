# CHAPTER 5: MALICIOUS SOFTWARE

## 1. Malware

|                  | Virus                                                        | Worm                                                        |
| ---------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| How it triggered | Kích hoạt chung với chương trình vật chủ                     | Click vào một đường URL để kích hoạt một script tạo ra worm |
| Spread out scope | Phân tán vào trong các ổ đĩa, files, bộ nhớ của máy bị nhiễm | Phát tán và lây lan trên mạng                               |

### Virus

Ký sinh vào trong một chương trình (khỏe mạnh) nào đó.

Gồm 2 nhiệm vụ:

- Phát tán trên phạm vi máy thuộc local với máy bị nhiễm
- Phá hoại các files trong máy bị nhiễm

Dấu hiệu nhận biết: Kích thước file tăng lên

Thường được đính vào trong cuối của chương trình ký sinh vì

- Tại đầu thì sẽ khó khăn trong việc tìm kiếm vì đầu chương trình là session data
- Tại giữa thì sẽ tốn công để mà sửa các lệnh jump đến một địa chỉ nào đó (e.g: jump địa chỉ 100 nhưng sau khi chương trình chèn virus vào thì khả năng code địa chỉ 100 đó sẽ ở địa chỉ là 200)

Cách để xác định virus của các phần mềm quét virus:

- vì lý do quyết định ký sinh ở cuối chương trình cũng là cách để xác định virus trong các chương trình
- các nhà cung cấp chương trình quét virus có cách xác định mã hash của các chương trình mã độc, từ đó detect dựa trên mã hash đã được lưu

### Worm

Là một đường link, URL dẫn tới một mã độc được kích hoạt bằng các click vào nó

Worm lây lan và sống trên mạng Internet

## 2. Modern Malware

### Botnet

Là mạng lưới các máy bị nhiễm mã độc chạy tự động.

Mục tiêu: Để điều khiển một lượng lớn các máy bị nhiễm mã độc để gây ra các cuộc tấn công với số lượng và quy mô lớn

Hacker lây truyền worm sang các máy khác trên mạng Internet, tuy nhiên hacker cũng không thể tự detect được các máy đã bị lây nhiễm. Dựa vào đó, hacker tạo ra được botmaster để kiểm soát và điều khiển các máy bị nhiễm độc thuộc botnet.

Botmaster thực chất cũng không thể tự detect và liên lạc được với các máy bị nhiễm độc trong botnet, botmaster sử dụng C&C (Command and Control)

### APT (Advance Persistant Threat)

- Advance: malware đặc biệt (rất phổ biến)
- Persistent: Tồn tại lâu dài, nhiều bước, kí sinh chậm và lâu bền
- Threat: Đối tượng là các tập đoàn có giá trị lớn và các thông tin của họ

## 3. Malware Analysis

### Basic Static

Kiểm tra file exe mà không cần nhìn vào chỉ dẫn để xác nhận là mã độc hay không phải mã độc (cần kinh nghiệm)

### Advance Static

Load file exe vào trong disassembler và nhìn vào trong kiến trúc của chương trình theo thứ tự để phát hiện chương trình làm những gì

### Basic Dynamic

Chạy mã độc và quan sát những hành vi của nó trên hệ thống theo thứ tự để loại bỏ phần bị nhiễm độc

### Advance Dynamic

Debug để kiểm tra trạng thái bên trong một chương trình exe có chứa mã độc
