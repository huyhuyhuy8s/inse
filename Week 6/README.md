# Chapter 4: Web security

## Table of Content

## The Basics

Included:

- Browser
- Web Application Server
- Database

### Web browser (Client Side)

#### Web Architecture

Bao gồm:

- HTML (Content)
- CSS (Presentation)
- Mở rộng tính năng của website:
  - Extensions: Xuất hiện về sau và rất hiện hành (ex: Chrome Extension), thực chất là các script -> phải phiên dịch từ đó có thể kiểm soát được khi biên dịch làm hạn chế việc bị sử dụng với mục đích xấu. Extensions được áp đặt với các chính sách bảo mật.
  - Plug-ins: Xuất hiện đầu tiên (ex: Adobe Flash, PDF Reader,..), sử dụng phần cứng để xử lý -> khiến cho browser không thể quản lý được plug-ins đang sử dụng tài nguyên nào vì **Plug-ins được viết bằng mã máy**.

#### Dynamic Contents

- Adobe Flash
- Microsoft Silverlight
- ActiveX
- Java Applet
- **JavaScript (Hiện hành)**

#### Javascript(JS) & Sandbox

- Javascript chạy code để giúp cho nội dung của HTML (tĩnh) trở nên động (dynamic)
- Có sandbox để thực thi các code để thử nghiệm các code trên đó có nguy hiểm hay không? Nếu có thì sẽ bị sandbox hủy và không gây ảnh hướng đến máy.

#### Javascript Engines

- V8 của Google (Chrome & MS Edge)
- SpiderMonkey (MozillaFirefox)
- JavascriptCore của Apple (Safari)

#### Hoạt động của Javascript

| Javascript Code                  |
| -------------------------------- |
| Byte Code                        |
| Engine (Enforce Security policy) |
| OS                               |

Các code JS sẽ được viết trong thẻ Script của HTML. Các script khi được thực thi sẽ được biên dịch trước - Sẽ được đặt trong sandbox trước để kiểm soát an toàn. JS Code sẽ được dịch sang byte code rồi từ đó chạy trên engine của sandbox đã được áp đặt chính sách an toàn (Enforce Security policy) rồi chạy trên OS.

#### Sandbox Javascript

JS code có thể truy cập vào:

- [Document Object Model (DOM) (ex: thẻ, trang, model,...) trong trang đó](#html-dom)
- Các trang khác những đã được kiểm soát (talk later)
- [Lấy dữu liệu từ browser (cookies, history,..)](#html-objects)
- [Đọc file từ hệ thống đã được bảo vệ bởi một lớp access control](#accessing-file)
- Kết nối với các thiết bị ở trên mạng.

#### Nội dung của trang JS có thể truy cập (DOM)

##### HTML DOM

Mỗi trang web trình duyệt sẽ tạo ra một cây quản lý các thành phần trên trang:\
![dom](/Week%206/img/dom.png)\
Bằng cách sử dụng lệnh JS sau:
```javascript
document.getElementById('demo').innerHTML = 'Hello World';
```

##### HTML Objects

- window.history lịch sử truy cập của máy
- window.images hình ảnh của máy
- document.forms forms của html
- document.URL các url trên html

##### Browser Objects

- window.history
  - back() and forward APIs
- window.navigator
  - Navigator.geolocation.getCurrentPosition()

##### Accessing File

Chính sách của JS không cho phép browser thu thập file từ máy tính trực tiếp nên buộc phải thông qua một cửa sổ và người dùng phải tự chọn file mà máy được phép thu thập dữ liệu. Các quy trình trên đều được làm thủ công chứ không được phép chạy ngầm hoặc thu thập dưới dạng binary mà chưa được người dùng cho phép!

### Web Server (Server Side)

Web Server sẽ bao gồm:

- HTTP Server
- Web Applications

Có 2 kiểu xây dựng Web Server:

1. HTTP Server và Web Applications được xây dựng độc lập.
2. HTTP Server và Web Applications được tích hợp.

Cách 1 sẽ xuất hiện luồng trao đổi giữa HTTP Server và Web Applications là các giao tiếp như Common Gateway Interface (CGI), Fast CGI,...

Cách 2 sẽ giúp cho web hoạt động nhanh hơn vì không cần thông qua luồng trao đổi giữa HTTP Server và Web Applications. Ex: PHP, Python, ASP,...

#### Interacting with Server

Tương tác với Server bao gồm:

- HTTP Request hoạt động bằng cách khi client request thì server sẽ gửi html file thay thế hoàn toàn trang hiện tại bằng trang được request.
- Ajax Request hoạt động linh hoạt hơn bằng cách chỉ thay thế phần nội dung được request ở bên client thay vì phải gửi lại gói request và load lại trang như HTTP Request. Cách này nhanh hơn và giảm thời gian load lại nội dung không thay đổi.
- Web Socket

##### HTTP Request & Response

##### GET vs POST

![getvspost](/Week%206/img/getvspost.png)

### Cookies and Sessions

#### Cookies

Stateless nature of the web: Để tránh việc tạo ra vùng nhớ để lưu trữ trạng thái trước đó và giảm thiểu vùng nhớ tạo ra thì thì website trở nên vô trạng thái. Khi nào Client request thì Server sẽ response. Tuy nhiên web cũng không phải lúc nào cũng stateless mà cần phải stateful (ex: thanh toán, đặt hàng,...).

Cookies được sử dụng để hỗ trợ cho website trở nên stateful!

#### Cài đặt Cookies

Cookies được tạo ra ở bên Server và gửi về Client ở bước đầu tiên. Về sau thì Client sẽ gửi Cookies cho Server.

Cookies có thể được tạo bằng PHP như sau:

```php
<?php
    setcookie('cookieA', 'aaaaaa');
    setcookie('cookieB', 'bbbbbb', time() * 3600);

    echo "<h2>Cookies are set</h2>"
>
```

Cookies có 2 loại:

- Cookies bình thường có thời gian sử dụng hữu hạn
- Sessions là Cookies vô hạn để kết nối các request với nhau.

### Ajax, WebSocket, Same-origin Policy

[Ajax, Websocket](#interacting-with-server)

#### Same-Origin Policy (SOP)

#### Giải thích SOP

Là chính sách an ninh mà người thiết kế browser áp đặt trên browser engine (JS Engine) sẽ quyết định chúng ta có được phép truy cập vào một trang web hay không.

2 website có 2 địa chỉ khác nhau, người dùng không được phép sử dụng dữ liệu của website 1 để truy cập vào website 2. Tránh tình trạng khi thay đổi đường dẫn từ website 1 sang website 2 mà vẫn sử dụng dữ liệu từ website 1 lên website 2.

Tuy nhiên vẫn có thể truy suất từ website 1 sang website 2 bình thường nghĩa là nội dung và dữ liệu của website 1 sẽ bị thay đổi bởi website 2.

##### Định nghĩa SOP

Một website sẽ có URL như sau:

`http://www.website.com/example/index.html`

Origin gồm 3 thành phần:

1. URI Scheme: là phần `http`.
2. Domain: `website.com`.
3. Địa chỉ cổng: mặc định là cổng `80`.

Same-Origin Object nghĩa là 3 thành phần của nó giống nhau.
Nếu 1 trong 3 thành phần khác nhau sẽ được gọi là Cross-Origin Object.

##### Phân biệt Same-Origin Object (SOO) và Cross-Origin Object (COO)

Orgin là `http://normal-website.com`

| URL                                       | Difference | SOO or COO |
| ----------------------------------------- | ---------- | ---------- |
| `http://normal-website.com/example/`      |            | SOO        |
| `https://normal-website.com/example/`     | URI Scheme | COO        |
| `http://www.normal-website.com/example/`  | Domain     | COO        |
| `http://normal-website.com:8080/example/` | Port       | COO        |

#### SOP quan trọng như nào

- Cô lập website này với một website khác ngay trên trình duyệt.
- Ngăn chặn ứng trên trên website đang chạy trên tab này truy suất dữ liệu trên website khác trên một tab khác. Tránh việc tiêm code trên server.
- Giúp cho người dùng duyệt web một cách an toàn.

## Cross-site Request Forgery (CSRF)

Lợi dụng cơ chế của Cross Domain Request

## Cross-site Scripting Attack

## SQL Injection Attack
