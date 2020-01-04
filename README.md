# udp-docker

## Purpose and Overview
These are example programs for sending and receiving UDP using Python and (optionally) using Docker.

This code and desription show:

- Sending and receiving UDP with Python
- Sending and receiving UPD using Python code inside of a Docker container 
- Getting UDP woring between a Docker container and the outside world using a Python `socket`
- Using some Docker commands to `run`, `build`, and `push`
- Using the Docker server in experimental mode using `--platform` to build for a platform other than the one you're building on (e.g., AMD64 processor vs. ARM processor)

The Python files are:
- `udp-send.py` sends a Hello World message every second to the specified ip address and port.
- `udp-rx.py` receives UDP messages from the specified port and displays messages on the terminal.

There are two Docker files (one each to build the images for `udp-send` and `udp-rx`.  Both are named `Dockerfile` (in the corresponding folders for `udp-send` and `udp-rx`).

## How to Test

Run both `udp-send.py` and `udp-rx.py` using either Python or Docker, and watch `udp-rx.py` to see what `udp-send.py` sends.

See next sections for how to run directly with Python or using Docker.
    
If you want to run the programs separately to test:

- Run `udp-send.py`.  Then, view contents of the sent UDP packets in Linux using:

`$ nc -kluv <port>`

- Run `udp-rx.py`.  Then, send UDP packets in Linux using:

`$ nc -u <ip address> <port>`

## To Run using Python

You do not need Docker to run the Python code.  You can run the UDP send code using:

    $ python3 udp-send.py 192.168.1.12 5005
or replace 192.168.1.12 and 5005 with whatever ip address and port you want to send to.

You can run the UDP receive code using:
  
    $ python3 udp-rx.py 5005
    
or replace 5005 with whatever port you want to receive on.

## To Run using Docker

To run the Docker containers, you do not need to build the Docker images.  The following `docker run` commands will pull images from my Docker Hub.  (Of course you need Docker installed on your system first.)

To run the UDP **receive** program on a **PC (x86-64 / AMD64 processor)** in Linux using docker:

    $ docker run -p 5005:5005/udp --init -e myport=5005 --rm --name udprx1 billnewhall/udp-rx:linux-amd64


To run the UDP **send** program on a **PC (x86-64 / AMD64 processor)** in Linux using docker:

    $ docker run -p 5005:5005/udp --init -e destip=192.168.1.31 -e destport=5005 --rm --name udpsend1 billnewhall/udp-send:linux-amd64

These will also run using Docker on a Windows 10 PC, but I have not been able to get `udp-rx.py` to work when sending from another PC to the Windows 10 PC.  (Probably some network or firewall setting.)

To run the UDP **receive** program on a **Raspberry Pi 4 (x86-64 / AMD64 processor)** (I haven't tried a Pi 3 yet) in Linux using docker:

    $ docker run -p 5005:5005/udp --init -e myport=5005 --rm --name udprx1 billnewhall/udp-rx:linux-arm
    
To run the UDP **send** program on a **Raspberry Pi 4 (x86-64 / AMD64 processor)** (I haven't tried a Pi 3 yet) in Linux using docker:

    $ docker run -p 5005:5005/udp --init -e destip=192.168.1.12 -e destport=5005 --rm --name udpsend1 billnewhall/udp-send:linux-arm

## Building Docker Images (Optional but Informative)

You can build the Docker images (rather than downloading from my Docker Hub repo).  Do this using by putting the Python file and the Dockerfile in the same folder, and navigating to that folder in a terminal.  Then run Docker commands as follows.   (Images for `udp-send.py` and `udp-rx.py` must be in separate folders and built separately.)

To clear out existing images (if you want to):

    $ docker system prune -a
    
To build the images on a PC:

    $ docker image build -t billnewhall/udp-rx:linux-amd64 .

and

    $ docker image build -t billnewhall/udp-send:linux-amd64 .


You can remove the `billnewhall/` and `:linux-amd64`entirely, but use the appropriate image name in the `run` instructions above.
    
To build the images for a **Raspberry Pi 4 while using Docker on a PC** (see "Important Note" below):

    $ docker image build --platform linux/arm -t billnewhall/udp-rx:linux-arm .

and

    $ docker image build --platform linux/arm -t billnewhall/udp-send:linux-arm  .

You can remove the `billnewhall/` and `:linux-arm`entirely, but use the appropriate image name in the `run` instructions above.

**Important Note:**    To use the `--platform` option in `docker image build`, the Docker server needs to be run in *experimental* mode.  I did this by creating a file called **daemon.json** file in the /etc/docker folder with the following contents:

```
{ 
    "experimental": true
}
```

Then reboot to enable experimental mode.

To verify experimental mode, use `docker version` in a terminal, and you should see something like:
```
$ docker version
Client: Docker Engine - Community
 Version:           19.03.5
 API version:       1.40
 Go version:        go1.12.12
 Git commit:        633a0ea838
 Built:             Wed Nov 13 07:29:52 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.5
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.12
  Git commit:       633a0ea838
  Built:            Wed Nov 13 07:28:22 2019
  OS/Arch:          linux/amd64
  Experimental:     true
 containerd:
  Version:          1.2.10
  GitCommit:        b34a5c8af56e510852c35414db4c1f4fa6172339
 runc:
  Version:          1.0.0-rc8+dev
  GitCommit:        3e425f80a8c931f88e6d94a8c831b9d5aa481657
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```

`Experimental` for the `Server: Docker Engine - Community` (not client) needs to be `true`.

To push these to your own Docker repo:

    docker push <your username>/<your desired tag>
    
