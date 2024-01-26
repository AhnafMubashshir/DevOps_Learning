# Level 101

## 1.Fundemantal Series

## _Linux Basics_

This course is divided into three parts. In the first part, we cover the fundamentals of Linux operating systems.
In the second part, we cover some basic commands used in Linux like navigating the file system, viewing and manipulating files, I/O redirection etc.
In the third part, we cover Linux system administration. 

### Commands for Navigating the File System:

- ls  (list files and directories)
- pwd  (print working directory)
- cd  (change direcotry)


### Commands for Manipulating Files : 

- touch (create new file)
- mkdir (create new directories)
- rm (delete files and directories)
- cp (copy files and directories)
- mv (move files and directories) 
   Eg: mv <source_path> <destination_path>

### Commands for Viewing Files :
- cat (most simplest use to print the contents of the file on your output screen)
- head (displays the first 10 lines of the file by default)
- tail
- more (all)
- less

### Echo Command in Linux
 prints the given input string on the screen.

### Text Processing Commands
- grep (display all the lines in a file that contains a particular input)
 Eg:grep <word_to_search> <file_name>

- sed (used to replace a text in a file)
 Eg:sed 's/<text_to_replace>/<replacement_text>/' <file_name>

- sort 
 increasing order
 lexicographical order

### I/O Redirection
We can use some special operators to redirect the output of the command to files or even to the input of other commands.
  Eg: https://linkedin.github.io/school-of-sre/level101/linux_basics/images/linux/commands/image30.png
 
 ls > redirected file

 ### Linux Server Administration



## **_Linux Networking Fundamentals_

### Birds eye view of the course
The course covers the question “What happens when you open linkedin.com in your browser?” The course follows the flow of TCP/IP stack.More specifically, the course covers topics of Application layer protocols DNS and HTTP, transport layer protocols UDP and TCP, networking layer protocol IP and Data Link Layer protocol

### DNS
DNS is an **application layer** protocol

#### DNS Resolution : 
When somebody tries to open www.linkedin.com in the browser, the browser tries to convert www.linkedin.com to an IP Address. This process is called DNS resolution. 
The browser would have a DNS cache of its own where it checks if there is a mapping for the domainName to an IP Address already available, in which case the browser uses that IP address. 
If no such mapping exists, the browser calls gethostbyname syscall to ask the operating system to find the IP address for the given domainName

### UDP
UDP is a **transport layer** protocol.

**Multiplexing**:
When a client makes a DNS request, after filling the necessary application payload, it passes the payload to the kernel via **sendto system call**.

The kernel picks a random port number(>1024) as source port number and puts 53 as destination port number and sends the packet to lower layers. 

When the kernel on server side receives the packet, it checks the port number and queues the packet to the application buffer of the DNS server process which makes a **recvfrom system call** and reads the packet.

This process by the kernel is called multiplexing(combining packets from multiple applications to same lower layers).

**Demultiplexing** :
Segregating packets from single lower layer to multiple applications.

### TCP
Another common transport layer protocol **TCP** does a bunch of other things like 
- reliable communication
- flow control
- congestion control. 

But UDP is designed to be lightweight and handle communications with little overhead. 

##### Reliable Connection:
 A TCP connection is established by a three way handshake.
 1. the client sends a SYN packet along with the starting sequence number it plans to use.
 2. the server acknowledges the SYN packet and sends a SYN with its sequence number.
 3. Once the client acknowledges the syn packet, the connection is established.
 
##### Congestion Control:
TCP also does congestion control which determines how many segments can be in transit without an ack.

### HTTP
The HTML page of linkedin.com is served by HTTP protocol which the browser renders.
Browser sends a HTTP request to the IP of the server determined above. Request has a verb GET, PUT, POST followed by a path and query parameters 

### IP Routing and Data Link Layer
When the packet reaches the IP layer, the transport layer populates source port, destination port.

IP/Network layer populates destination IP(discovered from DNS) and then looks up the route to the destination IP on the routing table.



## _Git_
