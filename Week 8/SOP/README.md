# Lab SOP

[Document for SOP Lab](https://app.box.com/s/vzin09ud9zs8n2uhrsatshwwpvfin6hj)

Go to web_security/sop and open command dock

Enter `docker-compose up -d`

Open the VNC Viewer then enter the `localhost:5900`

return to the cmd, use `docker exec -it web-client sh -l` then the virtual Ubuntu of the **web-client**.

Enter `cat /tmp/hosts >> /etc/hosts` to *dunno why*

Execute tail command to make sure all 3 website are exists in the /etc/hosts file `tail -n5 /etc/hosts`

make sure that return all 3 website url and IP Address as below:

> 10.9.0.5 sitea.com\
> 10.9.0.5 siteb.com\
> 10.9.0.5 parentsite.com

## 4.1.2 Using JS to access DOM objects of the web site

In the *sitea.com* using the Developer Tools's console

### a. Access DOM Objects

by using `document.body`, `document.body.innerText`, `document.body.innerHTML`

### b. Change the text “Hey,Site A is working” to “Header text is modified via document object"

![sitea](/Week%208/SOP/sitea.png)

use the combine keys `CTRL + SHIFT + C` to detect the object. Then click on it, the html path will be shown as below:

```html
<h1 id="header">Hey, Site A is working</h1>
```

then, modify it in DT's Console with

```javascript
h1_element = document.getElementById("header")
h1_element.innerText = "Header text is modified via document object"
```

### c. Create a newwin variable for a new tab

```javascript
var newwin = window.open(http://siteb.com,”right”)
```

> Can you access document object of newwin? Explain why if you could not

No, can not because the provided code is wrong, must be corrected as

```javascript
var newwin = window.open("http://siteb.com","right")
```

then, DOM in opened can not be accessed due to the SOP Same Origin Policy.

### d. Enter JS code to set the new location for tab sitea which is the opener of current tab

Enter JS code to set the new location for tab sitea which is the opener of current tab:
window.opener.location = '<http://parentsite.com>'

When current in siteb.com which is opened by sitea.com, enter the `window.opener.location = 'http://parentsite.com'` code will change the location (url) of the opener (which is sitea) to `http://parentsite.com` which is legal due to the SOP cuz it does not change or access the DOM of sitea.

### e. Try JS code to access document.body object of window.opener. Explain why if you could not

no! You can not access the document.body object of the window.opener because it is violated the SOP, you can not access DOM of the Page that not the same origin.

## 4.1.3 Frame objects

Access <http://parentsite.com> then choose parentsite in list of sites on iframe picker.

![iframepicker](/Week%208/SOP/iframepicker.png)

### a. Can you access window.framea, window.frameb?

yes, i can access and create a variable that represent for the framea and frameb

### b. Can you access document.body of framea, frameb from the parentsite?

no, i can not because is violated the SOP

### c. Can you access window.parentsite?

after selet **sitea.com** by iframepicker, i can not access **window.parentsite** but can use **window.parent** to access it!

### d. Can you access document.body object of parentsite.com? Which object of parentsite that sitea can access?

no, from sitea.com, which is iframe of parentsite, i can not access the document.body or even the document of the parentsite.com

Every objects that sitea.com can access the parentsite include: blur, closed, frames, length, location, opener, parent, self, top, window.

### e. Can you access hello from sitea, siteb?

no, variable from the parentsite can not access by the sitea and siteb which is iframe of site due to the SOP.

## 4.1.4 Sending POST request to a site

### a. Access <http://sitea.com/post.html>

![sitea.com/post.html](/Week%208/SOP/sitea.com,post.html.png)

### b. Type some text in textbox then click “Submit query”. What would show up? Explain why you see that

After type text and click "Submit query", the location was changed to "siteb.com".

Explain: the form that wrote in post.html have the action attribute is "<http://siteb.com>" which mean everything you did will be send to siteb.com

### c. Repeat step (a), toggle Web console >> Network (Ctrl + Shift + E)

![networda](/Week%208/SOP/networka.png)

### d. Repeat step (b), examine the request and response header. What can you conclude about POST form request

after repeat from step (a) with Network tab is on. A package with method POST is existed in the Network tab.

At the request header, the origin is **<http://sitea.com>** and the referer is **<http://sitea.com/post.html>** which mean the source web is sitea.com evenly from sitea.com/post.html

![networktab](/Week%208/SOP/networktab.png)

In request of method, form data sent from the origin is `email=abcd&go=Submit+Query`

![payload](/Week%208/SOP/payload.png)

## 4.1.5 Access image, stylesheet from other sites

### a. In the Inspector panel of sitea.com, can you change sitea’s image to image from siteb.com?

No, you can not change directly sitea's image to siteb's image on Inspector panel of sitea because siteb's image is not existed in sitea directory.

### b. In the Inspector panel of sitea.com, can you change the stylesheet to that of siteb.com?

Again, you can no change directly sitea's stylesheet to siteb's stylesheet on Inspector panel because of the lack of siteb's stylesheet existance on sitea's directory.

## 4.1.6 SOP Applies to web storage

### a. Define a new variable named first = 10

You can define either with javascript in console: window.LocalStorage[“first”] = 100 or Add item in Storage tab

![storageadd](/Week%208/SOP/itemlocal.png)

### b. Open sitea.com in a new tab. Can you access first variable in this tab? Change first to a new value, go back to the previous sitea.com tab, what is the value of first then

Yes, I can access first variable in the fisrt tab in second tab.

![a](/Week%208/SOP/secondtablocal.png)

Evenly change the value of *first* to 200 in the second tab, the value of first in the first tab is changed match to the value in second tab!

![changefirstvalue](/Week%208/SOP/changefirstvalue.png)

### c. Can you access first from siteb.com?

Absolutely no, SOP wont let siteb.com access every variables in sitea.com to protect from extracting data via weird website!

### d. Close all sitea.com tabs. How about first variable when sitea.com is re-opened?

The first valuable still exists in local storage of sitea.com even close all sitea.com tab.

![sitealocal](/Week%208/SOP/changefirstvalue.png)

### e. Close browser then re-open, does first variable still exist?

The result made me shocked that the local variable is still exist in the local storage.

### f. What can you conclude about Local Storage?

The local storage is where you store variables for website using time to time, just like a long-term database.

### Repeat the above steps from (a) to (e) but with Session Storage. What can you conclude about Session Storage?

The session storage is like a ram, use only in a session. When you done a session or close it, the variables will be dissapeared.
