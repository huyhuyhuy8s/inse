# Chapter 3: Access Control
## What is authentication?
![image](/buffer-overflow/INSE/lecture/img/qytr_authentication.png)
- B1: Xác thực bthan bằng pass or vân tay
- B2: Hệ thống cung cấp mã, mỗi lần truy xuất thì hệ thống sẽ ktr cái mã đó để quyết định user có đc phép sd tài nguyên hay k
1. Định nghĩa:
- Chứng minh danh tính của user
- Diễn ra những bước như khởi chạy ứng dụng
2. Mục tiêu:
- Để user có thể sd đc hệ thống
  - Availability: nếu đúng là user thì user ph đc sd hệ thống
  - No false negatives: có dki trên hệ thống but hệ thống bảo k có (cần tránh)
- Hệ thống xác minh đúng user đã cung cấp danh tính, tránh tình trạng nhận dạng sai user
  - Authenticity
  - No false positives
3. Phương pháp:
- Knowledge-based: dựa trên thông tin về user (pass)
- Possession-based: dựa trên những gì user có (ATM, điện thoại)
- Inheritance-based: tính thừa kế (vân tay, võng mạc, khuôn mặt)
> Có thể kết hợp các nhân tố lại với nhau.
4. The Importance of a Trusted Path
## Password authentication
1. Định nghĩa:
- User nhập unique ID và key và thông tin trễn sẽ được ktr so sánh vs dữ liệu đã dki trc đó\
[?] Why "sth u know" more populer than others?
    - Pass là user tự đặt, dễ nhớ, dễ liên tưởng --> Cost: free
    - Convenience: if user quên pass thì admin vẫn can easy reset lại hệ tống để tạo pass ms
2. Trouble:
- Mang yếu tố cng: dễ lộ, hờn hợt khi đặt pass
3. Keys & Passwords:
![image](/buffer-overflow/INSE/lecture/img/key&pass.png)
4. Best advice:
- Chọn pass dựa theo passphrase
- Sd pass cracking tool để test pass\
**Passphrase**
    - Leetspeak: [tool](http://www.robertecker.com/hp/research/leet-converter.php) \
  [tool_check](https://www.useapassphrase.com/)         