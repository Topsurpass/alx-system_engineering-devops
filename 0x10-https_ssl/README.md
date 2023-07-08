# HTTPS_SSL

# Objectives
This project has fulfilled the objectives such as knowing:
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

## Task 0

What we need to do here is add sub domains(www, lb-01, web-01, web-02) to our domain name(temz.tech) and point the subdomains to the appropriate ip addresses

Step 1
We need to go over to our domain administrators that is the get.tech


- Login into get.tech
- Click on account
- You should see some textboxes
- Enter your domain name eg(example.tech) under the jump to domain textbox
- Click on the double arrow in front of it to search
- Scroll down, you will see manage Dns click on it
- We need to add the following subdomain www, lib-01, web-01 and web-02
- You will see two fields. Host name and ipv4 address
- Click on add A record
- For www. In the host name type www and the ipv4 enter ip address of your load balancer then click on add record.
- Let's repeat the process for the other subdomains
- For lib-01. In the host name type lib-01and in the ipv4 add ip address of your load balancer.
- For web-01. In the hostname type web-01 and in the ipv4 add ip address of your web-01 webserver
- For web-02. In the hostname type web-02 and in the ipv4 type the ip address of your web-02 webserver

## Task 1

- Make a copy of this script and make it executable
- The script contains script to install certbox (used to generate SSL certificate)

```
https://github.com/Topsurpass/alx-system_engineering-devops/blob/master/0x10-https_ssl/certbot
```
- Run the script with sudo
```
sudo ./certbot www.yourdomain.tech your_email
```
- When installation is complete
- We need to configure our haproxy
- sudo vi /etc/haproxy/haproxy.cfg
- You should change the all the content to the content of the following script
```
https://github.com/Topsurpass/alx-system_engineering-devops/blob/master/0x10-https_ssl/1-haproxy_ssl_termination
```
- Please edit where necessary(line 37 to 49)
- You will need to put your domain name and web server ip addresses
- Test the validity of your server running the following command
```
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```
- It should show valid. You can then
- Exit your web_server and then write the same content inside the 1-haproxy_ssl_termination file. Make it executable and push to github. You should be good

## Task 2

- In your terminal write the content of this script inside the file 100-redirect_http_to_https
- Edit as needed
- Push to github
```
https://github.com/Topsurpass/alx-system_engineering-devops/blob/master/0x10-https_ssl/100-redirect_http_to_https 
```
## Project links

* [What is HTTPS?](https://www.instantssl.com/http-vs-https)
* [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
* [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)
* [DNS](https://intranet.alxswe.com/concepts/12)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)

## Requirements
* shellcheck version 0.3.7
* ubuntu 16.06 LTS
* certbot

## Author
* Olowosuyi Temitope
