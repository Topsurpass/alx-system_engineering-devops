# Load balancer
This project contains tasks on load balancer

## Learning objectives
This project has fulfilled the learning objectives such as knowing:
* Load balancer
* Web stack debugging
* Introduction to load-balancing and HAproxy
* Debian/Ubuntu HAProxy packages
## Project explanation
This is how the load balancer works. The load balancer helps to distribute traffics or loads across different web servers using different algorithm. In this project, we used HAproxy as our load balancer, using roundrobin algorithm for distribution. The load balancer is installed on webserver 7670-lb-01 (you can use ssh to access the server), and it distributes the load to webserver 7670-web-01 and 7670-web-02 (Both's custom HTTP header has been configured to include X-Served-By with its value being $hostname of the server, this is done to be able to determine which server is handling request at a particular time). The webservers have been configured and loaded with the the html files to load, the port to listen to e.t.c. The load balancer also has been configured with the list of webservers to redirect to with their port, this is done via its configuration file. Once everything is done, I mapped the loadbalancer IP address to the A record of my domain on the cpanel and thats all.
## Requirements
* Editor: The editor used was vi
* shellcheck
* Nginx web server
* Docker
* HAproxy load balancer using roundrobin algorithm
## Project links
* [Load balancer](https://intranet.alxswe.com/concepts/46)
* [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
* [Load-balancing algorithms](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-the-algorithms/ta-p/273759)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)
* [Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw&feature=youtu.be)
* [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
## Author
Olowosuyi Temitope
