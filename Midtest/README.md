# Midtest 

## Table of Content

| 1   | 2   | 3   | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- |
| 7   | 8   | 9   | 10  | 11  | 12  |
| 13  | 14  | 15  | 16  | 17  | 18  |
| 19  | 20  | 21  | 22  | 23  | 24  |
| 25  | 26  | 27  | 28  | 29  | 30  |
| 31  | 32  | 33  | 34  | 35  | 36  |
| 37  | 38  | 39  | 40  | 41  | 42  |

## The Test

### 1. The protection measure used is (are)

![1](/Midtest/img/1.jpg)

> Answer: 

### 2. Which example illustrates an organization's responsibility to comply with an individual's right to correct their personal data?

![2](/Midtest/img/2.jpg)

> Answer: c. cuz of the 'correct' term.

### 3. The protection measure used is (are)

![3](/Midtest/img/3.jpg)

> Answer: 

### 4. What technique is commonly used to ensure data integrity?

![4](/Midtest/img/4.jpg)

> Answer: b. deal to the name of the chapter 3 in the course 'Access Control'

### 5. What is CSRF in web security?

![5](/Midtest/img/5.jpg)

> Answer: b. CSRF (viết tắt của Cross-Site Request Forgery) hay còn gọi là giả mạo yêu cầu chéo trang là một loại hình tấn công mạng trong đó kẻ tấn công lừa người dùng thực hiện các hành động trái ý muốn trên một trang web mà người dùng đã được xác thực.

### 6. A hacker gains access to a company's financial records, modifies them, and then deletes the original files. Which security goals are violated?

![6](/Midtest/img/6.jpg)

> Answer: 

### 7. A hacker gains access to a company's financial records, modifies them, and then deletes the original files. Which security goals are violated?

![7](/Midtest/img/7.jpg)

> Answer: a. because the dev are totally trusted to the input of user

### 8. Which of the following Java code snippets is safe against SQL injection?

![8](/Midtest/img/8.jpg)

> Answer: d. deal to the function 'setString(1, username)' to prevent the SQL Injection.\
c. is not enout to protect because the username could have the sign ' in it.

### 9. What is the primary goal of secure coding?

![9](/Midtest/img/9.jpg)

> Answer: a.

### 10. Identify correct type of vulnerability in following code?

![10](/Midtest/img/10.jpg)

Có 3 loại tấn công lỗ hổng XSS phổ biến, gồm:

- DOM - based XSS: Sử dụng các kỹ thuật JavaScript để thay đổi nội dung trang web và chèn mã độc vào DOM.

- Stored XSS: Mã độc được lưu trữ trên máy chủ, khi người dùng truy cập vào trang web sẽ kích hoạt mã độc.

- Reflected XSS: Mã độc được chèn vào các URL, khi người dùng click vào URL đó thì mã độc sẽ được thực thi.

- CSRF (viết tắt của Cross-Site Request Forgery) hay còn gọi là giả mạo yêu cầu chéo trang là một loại hình tấn công mạng trong đó kẻ tấn công lừa người dùng thực hiện các hành động trái ý muốn trên một trang web mà người dùng đã được xác thực.

> Answer: a. vì người dùng có thể chèn mã đọc javascript vào trong mục input

### 11. What kind of vulnerability the following code snippet does exhibit?

![11](/Midtest/img/11.jpg)

> Answer: d. vì không xác thực lại old password để confirm đó là người dùng.

### 12. How can continuous monitoring help in mitigating the risks of impersonation?

![12](/Midtest/img/12.jpg)

> Answer: b. By detecting and responding to suspicious activities

### 13. The protection measure used is (are)?

![13](/Midtest/img/13.jpg)

> Answer:  

### 14. What is the technique behind the -fno-stack-protector gcc option?

![14](/Midtest/img/14.jpg)

> Answer: The aforementioned "guard variable" is commonly referred to as a canary.

### 15. What kind of vulnerability in the following code snippet?

![15](/Midtest/img/15.jpg)

> Answer: b. because then sql command 'select * from products where name like '%{query}%'" cannot return the error except the none.

### 16. The protection measure used is (are)

![16](/Midtest/img/16.jpg)

> Answer: a. because there is not any protection have in the query. There is only the execute function.

### 17. Which of the following best describes a Tamper-Proof feature in an operating system?

![17](/Midtest/img/17.jpg)

> Answer: c.

Operating System with a robust design, as not to allow the execution of malicious code. **Access to internal data and procedures are never allowed without the proper authorization.** In its more strict implementations, this Operating System will have **attack detection mechanisms**. If the attack is of a certain level, the Operating System **may even delete all its code and/or data.**

### 18. What can **lead to increased regulatory scrutiny** for organizations that **fail to uphold information privacy standards**?

![18](/Midtest/img/18.jpg)

> Answer: d. because data of customer are being branch (Phân nhánh) và violation to privacy (vi phạm sự riêng tư)

### 19. John has security clearance as TOP-SECRET in Misc. Affairs Department. What can you state about John's office access control policy?

![19](/Midtest/img/19.jpg)

> Answer: c. Thông tin đã được phân loại thành TOP-SECRET và John là cá nhân được quyền truy cập.

**Security Clearance** là trạng thái được cấp cho các cá nhân cho phép họ **truy cập vào thông tin đã được phân loại** hoặc đến các khu vực hạn chế, sau khi hoàn thành quá trình kiểm tra lý lịch kỹ lưỡng.

- **Discretionary access control (DAC)**: based on the discretion of the data owner. (dựa trên sự quyết định của người sở hữu dữ liệu. **Người sở hữu và tạo ra data có khả năng cấp quyền truy cập cho người khác.**)
- **Mandatory access control (MAC)**: A system-wide access policy. (một chính sách truy cập toàn hệ thống **người sở hữu data không có khả năng cấp quyền truy cập**. || **Quyền truy cập được cấp cho cá nhân**. || **Thông tin đã được phân loại (classification)**)
- **Role-based access control (RBAC)**: based on user roles. (dựa trên role của người dùng. **quyền truy cập được cấp theo vai trò**)
- **Rule-based access control**: based on a set of predefined rules. (**quyền truy cập được cấp theo quy định hoặc luật.**)

### 20. What is the primary purpose of multi-factor authentication (MFA)?

![20](/Midtest/img/20.jpg)

> Answer: d. 

### 21. What kind of vulnerability in the following code snippet?

![21](/Midtest/img/21.jpg)

> Answer: d. union

### 22. Which security goals are violated for the following cases (answer text may be in whichever case)

![22](/Midtest/img/22.jpg)

> Answer: 

### 23. Which of the following is a key principle of defensive programming?

![23](/Midtest/img/23.jpg)

> Answer: 

### 23. Which of the following is a key principle of defensive programming?

![23](/Midtest/img/23.jpg)

> Answer: 

### 23. Which of the following is a key principle of defensive programming?

![23](/Midtest/img/23.jpg)

> Answer: 

### 26. What is a common method to prevent SQL injection attacks in secure coding?

![26](/Midtest/img/26.jpg)

> Answer: a. parameterized queries is the most common.

### 27. Which of the following belong to the rule-based access control

![27](/Midtest/img/27.jpg)

> Answer: b. and c.

a. is belong to MAC because the user are grouped and data are also grouped.\
b. is true because it's ruled as can just be accessed between 1:00pm to 3:00p.\
c. is true because it's ruled as can just be accessed if the ip address is not in 10.0.0.0/8\
d. is belong to MAC

### 28. In the context of SQL injection, what type of attack does the following input represent? ' ; DROP TABLE users; --

![28](/Midtest/img/28.jpg)

> Answer: a. stacked query is a query that have more than 1 command

### 35. Which of these inputs is an example of a boolean-based blind SQL injection attack?

![35](/Midtest/img/35.jpg)

> Answer: c. 

### 38. Which of the following security levels are used to classify documents in the Mandatory Access Control system

![38](/Midtest/img/38.jpg)

> Answer: a. Confidential b. Secret and d. Top Secret

### 39. Which type of vulnerability does expose in following code?

![39](/Midtest/img/39.jpg)

> Answer: d. because the xss cant be used in php echo.

**PHP CAN NOT EXECUTE JAVASCRIPT ->> NO XSS**;

### 41. The protection measure used is (are):

![41](/Midtest/img/41.jpg)

> Answer:

| High Memory     |
| --------------- |
| arguments       |
| return address  |
| Frame pointer   |
| local variables |

## 42. What is a significant threat posed by impersonation?

![42](/Midtest/img/42.jpg)

> Answer: b.
