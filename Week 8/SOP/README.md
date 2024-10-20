# Lab SOP

Go to web_security/sop and open command dock

Enter `docker-compose up -d`

Open the VNC Viewer then enter the `localhost:5900`

return to the cmd, use `docker exec -it web-client sh -l` then the virtual Ubuntu of the **web-client**.

Enter `cat /tmp/hosts >> /etc/host` to *dunno why*

Execute tail command to make sure all 3 website are exists in the /etc/hosts file `tail -n5 /etc/hosts`

make sure that return all 3 website url and IP Address as below:

> 10.9.0.5 sitea.com\
> 10.9.0.5 siteb.com\
> 10.9.0.5 parentsite.com

## Using JS to access DOM objects of the web site

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
window.opener.location = 'http://parentsite.com'

