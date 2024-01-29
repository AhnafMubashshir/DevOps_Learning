# Level 101
## 1.Fundemantal Series
## **_Linux Basics_
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
### OSI Model
Application Layer
Presentation Layer
Session Layer
Transport layer
Network Layer
Data Link Layer
Physical Layer

** Application Layer :
provides services for network applications:
http
https
smtp

**Presentation Layer:
- Translation into Binary form  (ASCII->EBCDIC)
- Data compression
- Data Transmission: Encryption/Decryption ->SSL(secure sockets layer)

**Session Layer:
- Authentication
- Authorization
- Session Management (keep tracking which data packets belongs to textfile or imagefile)
Transport layer

**Transport layer:
- Segmentation
Data receives from session layer devides into **Segments**
Segements having data unit (port num, seq num)
seq num:reassembles data unit for correct connection
 - Flow Control: server to application download speed management
 - Eror Control:Using **Checksum** to retreive missing/corruped data
 **TCP** -Connection Oriented Transmission
**UDP** - Connectionless (no loss data retrieving)

**Network Layer:
- Logical Addressing : IP address
- Routing-  packet goes to Network1 to Network2 by Ip address+ Mask Value checkng which is done by server .
- Path determination: best Possible path
 OSPF(open shortest path first)
BGP(Border Gateway Protocol)
IS-IS(Intermediate system)

**Data Link Layer:
- Pyhsical Addressing : MAC addressing attched  to previously logical Address(IP). its 12 digit alpha-numeric number embedded in NIC (Network interface Card).
- Head, Tail, Frame
- Access Media
**Physical Layer:
- Converts Binary seq into signal and transmits over local media


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

## 2.Python and Web
**What is the difference then, between java and python?**
Java's compiler is more strict and sophisticated.It is a statically typed language. So the compiler is written in a way that it can verify types related errors during compile time.
While python being a dynamic language, types are not known until a program is run. So in a way, python compiler is dumb (or, less strict). 

Python, on the other hand, is an interpreted language. When you run a Python script, it goes through a two-step process:
- **Compilation to Bytecode**: The Python source code is first compiled into bytecode. Bytecode is an intermediate representation that is platform-independent and is not directly executed by the CPU.

- **Execution by Python Virtual Machine (VM)**: The Python bytecode is then executed by the Python interpreter or Python Virtual Machine (VM). The Python interpreter reads the bytecode and translates it into machine code on the fly. This introduces an additional layer of abstraction compared to languages like C or C++.

**in case of C/C++, the output is machine code which can be directly read by your operating system. When you execute that program, your OS will know how exactly to run it. But this is not the case with bytecode.**

##### **Advantages**:
- **Portability**: Bytecode is platform-independent, allowing Python code to be executed on any system with a compatible Python interpreter.

- **Dynamic Typing**: Python's dynamic typing and features like introspection are made possible by the interpretation of bytecode during runtime.

## **_Python Concepts_
- **Everything in Python is an object.**
- That includes the functions, lists, dicts, classes, modules, a running function (instance of function definition), everything. In the CPython, it would mean there is an underlying struct variable for each object.

In python's current execution context, all the variables are stored in a dict. It'd be a string to object mapping.
 >>> float_number=42.0
>>> def foo_func():
...     pass
...

**NOTICE HOW VARIABLE NAMES ARE STRINGS stored in a dict
>>> locals ()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'float_number': 42.0, 'foo_func': <function foo_func at 0x1055847a0>}
### Decorators
In Python, decorators are a powerful and flexible way to **modify or extend the behavior of functions or methods without changing their source code directly.** 
Decorators are often used for tasks like **logging, authentication, caching, and more.** Decorators are applied using the @decorator_name syntax.

Function Decorators:

- A decorator in Python is essentially a function that takes another function as an argument and adds or modifies its behavior.
- You can define a decorator using the @decorator_name syntax above the function you want to decorate.

**python source code**

```sh def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello() 
```
**Output**:
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

### Sockets

#### **How a python program is executed??**

The execution of the Python program involves 2 Steps:
- Compilation
- Interpreter

#### Compilation
The program is converted into **byte code**. Byte code is a fixed set of instructions that represent arithmetic, comparison, memory operations, etc. It can run on any operating system and hardware. The byte code instructions are created in the .pyc file. The .pyc file is not explicitly created as Python handles it internally but it can be viewed with the following command:

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200703191624/binary.PNG)

The dis command is known as “disassembler” that displays the byte code in an understandable format.

#### Interpreter
The next step involves converting the byte code (.pyc file) into machine code. This step is necessary as the computer can understand only machine code (binary code). Python Virtual Machine (PVM) first understands the operating system and processor in the computer and then converts it into machine code. Further, these machine code instructions are executed by processor and the results are displayed.
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200703190408/Capture.PNG)
#### **How's python3 is superior than python2.7 ?**
**Unicode Support**:
Python 3 has native support for Unicode, making it the default string type. In Python 2.7, strings were ASCII by default, and Unicode support required explicit handling with the u prefix.

**Print Function**:
Python 3 uses the print() function instead of the print statement, providing a more consistent and versatile way to print output. This change makes it easier to adapt to various output requirements.

**Division Behavior**:
Python 3 changes the division operator behavior, making the / operator always perform true division. In Python 2.7, division between two integers resulted in integer division unless one of the operands was a float.

**Syntax Improvements**:
Python 3 introduced syntax improvements to enhance readability and consistency, such as the removal of redundant constructs and adjustments to function annotations.

**Range Function**:
The range() function in Python 3 returns an iterator, similar to the behavior of xrange() in Python 2.7. This change improves memory efficiency when dealing with large ranges.

**Modern Language Design**:
Python 3 incorporates lessons learned from the development of Python 2 and strives for a more consistent and clean language design. It eliminates certain inconsistencies and improves the overall structure of the language.

**Enhanced Libraries**:
Some Python 3 features and improvements are library-specific, providing enhanced functionality and better performance. New modules and features have been added to the standard library.

**Easier Porting to Future Versions**:
Python 3 is designed to be forward-compatible, making it easier for developers to port their code to future versions of the language. The Python community actively encourages migration to the latest Python 3 release.

**Example**: https://www.mygreatlearning.com/blog/python-2-vs-python-3/




# Level 102
## 1.Linux Intermediate
## **_Package Management_
Package management is a method of installing and maintaining software programs on any operating system

 Package file is a **compressed collection** of files that contains software, its dependencies, installation instructions and metadata about the package.
 ### Repository
 Repository is a storage location where all the packages, updates, dependencies are stored. 
 Each repository can contain thousands of software packages hosted on a remote server intended to be installed and updated on linux systems. 
 We usually update the package information ( often referred to as metadata) by running “sudo dnf update”.
 
Linux Distribution ->	Low-Level |	High-Level 
Debian ->	        dpkg	|      apt-get
Fedora,RedHat ->	dnf	    |       dnf

## **_Storage Media_
Storage media are devices which are used to store data and information. Linux has amazing capabilities when it comes to handling external devices including storage devices. There are many kinds of storage devices physical storage devices like hard drives, virtual storage devices like RAID or LVM, network storage and so on.

## **_Archiving and Backup_
### Archiving
We usually archive the data that are no longer needed but are kept mostly for compliance purposes. This helps in storing the data into compressed format saving a lot of space. Below section is to familiarize with the archiving tools and commands.

#### gzip
gzip is a program used to compress one or more files, it replaces the original file with a compressed version of the original file.

### Backup
Backup is a process of copying/duplicating the existing data, This backup can be used to restore the dataset in case of data loss. Data backup also becomes critical when the data is not needed in a day to day job but can be referred to as a source of truth and for compliance reasons in future. Different types of backup are :

#### Incremental backup
Incremental backup is the backup of data since the last backup, this reduces data redundancy and storage efficiency.

#### Differential backup
Sometimes our data keeps on modifying/updating. In that case we take backup of changes that occurred since the last backup called differential backup.

#### Network backup
Network backup refers to sending out data over the network from the source to a backup destination in a client-server model. This backup destination can be centralized or decentralized. Decentralized backups are useful for disaster recovery scenarios.

**rsync** is one of the linux command which sync up file from one server to the destination server over the network.

#### Cloud Backup
Two most widely used cloud backup options are Azure backup (from Microsoft) and Amazon Glacier backup (from AWS).

## **_Intro to VIM_
Vim is an open-source and free command line editor.
As an SRE we several times 
- log into into the servers
- make changes to the config file 
- edit and modify scripts 

**Opening a file and using insert mode**
We use the command vim filename to open a file filename. The terminal will open an editor but once you start writing, it won’t work. It’s because we are not in "INSERT" mode in vim.

Press i and get into insert mode and start writing.
**Vim Commands	Description**
:q	 Exit the file but won’t exit if file has unsaved changes
:wq	Write(save) and exit the file.
:q!	Exit without saving the changes.

## **_Bash Scripting_
Writing the first bash script:

We will start with a simple program, we will use Vim as the editor during the whole journey.

```sh
#!/bin/bash

# This if my first bash script
# Line starting with # is commented

echo "Hello world!"
```
We will save this script as “firstscript.sh” and make the script executable using chmod.

![alt text](https://linkedin.github.io/school-of-sre/level102/linux_intermediate/images/image16.png)
## 2.Linux Advance
## **_Containers_
A container is your code bundled along with its entire runtime environment. That includes your system libraries, binaries and config files needed for your application to run.

**Difference between virtual machines and containers**

- Containers do not have a separate (guest) OS
- Container engine is the intermediary between containers and Host OS. It is used to facilitate the life-cycle of a container on the Host OS (it is not a necessity, however).

#### VM
![alt text](https://linkedin.github.io/school-of-sre/level102/containerization_and_orchestration/images/VM.png)

#### Container
![alt text](https://linkedin.github.io/school-of-sre/level102/containerization_and_orchestration/images/Containers.png)

**Hypervisor vs. Container Runtime**:

**VMs**: Hypervisors (such as VMware, Hyper-V, or KVM) manage the creation, operation, and monitoring of virtual machines. Hypervisors provide a layer of abstraction between the physical hardware and the VMs.
**Containers**: Container runtimes (e.g., Docker, containerd) are responsible for managing the life cycle of containers. They interact with the host OS and leverage containerization features provided by the Linux kernel (namespaces, cgroups) to create isolated environments.

**Docker Image**
A Docker image is a lightweight, standalone, and **executable package** that includes everything needed to run a piece of software, including the code, runtime, libraries, and system tools. It is a snapshot of a filesystem with the necessary components to run an application.

## **_Orchestration With Kubernetes_
The Kubernetes components themselves are run as containers wrapped in Pods (which is the most basic kubernetes resource object).

Control plane components:
kube-apiserver
etcd
kube-scheduler
kube-controller-manager
Node plane components
kubelet
kube-proxy
This workflow might help you understand the working on components better:

An SRE installs kubectl in their local machine. This is the client which interacts with the Kubernetes control plane (and hence the cluster).

They create a YAML file, called manifest which specifies the desired state of the resource (e.g a deployment names “frontend” needs 3 pods to always be running)

When they issue a command to create objects based in the YAML file, the kubectl CLI tool sends a rest API request to the kube-apiserver.

If the manifest is valid, it is stored as key value pairs in the etcd server on the control plane.

kube-scheduler chooses which nodes to put the containers on (basically schedules them)

There are controller processes (managed by kube-controller manager) which makes sure the current state of the cluster is equivalent to the desired state (here, 3 pods are indeed running in the cluster -> all is fine).

On the node plane side, kubelet makes sure that pods are locally kept in running state.

## 3.System Design
