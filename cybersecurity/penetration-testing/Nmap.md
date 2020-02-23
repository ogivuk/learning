# Nmap

[Nmap](https://nmap.org/) ("Network Mapper") is a free and open source utility for network discovery and security auditing.

Nmap suite also includes:

* [Zenmap](https://nmap.org/zenmap/),  an advanced GUI and results viewer,
* [Ncat](https://nmap.org/ncat/), a flexible data transfer, redirection, and debugging tool
* [Ndiff](https://nmap.org/ndiff/), a utility for comparing scan results, and
* [Nping](https://nmap.org/nping/), a packet generation and response analysis tool

Nmap port states:

* **Open**: an application is actively listening for connections/packets on that port
* **Closed**: there is not any application (currently) listening on that port
* **Filtered**: there is a firewall or a filter blocking the port, so nmap cannot determine if it is open of closed
* **Unfiltered**: the port is responding to nmap probes, but it is not possible to determine if it is open or closed
* **Open/Filtered**: the port is either filtered or open, and nmap cannot precisely determine the state
* **Closed/Filtered**: the port is either filtered or closed, and nmap cannot precisely determine the state

## Installation

Debian Linux and Derivatives such as Ubuntu:

```bash
sudo apt update && sudo apt install nmap
```

Sometimes Debian's Nmap releases are a year or more behind the current Nmap version. The latest release can be obtained by compiling it from source code, or by downloading the RPM-format binaries and converting it to a deb package. More information can be found in the [official guide](https://nmap.org/download.html).

## Scanning

Note: Nmap is a noisy tool that creates a lot of traffic during scanning.

### Common Scans

[Host Discovery (Ping Scan)](https://nmap.org/book/man-host-discovery.html)

* checks if the target is alive, no port scanning
* goes beyond simple ICMP echo requests to solicit a response
* `-sn` option means no port scan
* `nmap -sn <target_IP_address_or_subnet>`
* `nmap -sn -iL <file_list_of_hosts_or_networks>`
* Default: Nmap sends an ICMP echo request, a TCP SYN packet to port 443, a TCP ACK packet to port 80, and an ICMP timestamp request

Supported protocols

* shows which IP protocols are supported by the target
* the scan cycles through IP protocol numbers
* `sudo nmap -sO <targets>`

Firewall probe

* checks if scans are getting filtered
* `sudo nmap -sA <targets>`

TCP scan - Fast mode

* scan fewer ports than the default scan with `-F`
* with faster timing template `-T4`
* `nmap -T4 -F <targets>`

TCP scan - Particular ports

* `nmap -p <port_range> <targets>`
* scan all ports with `-p-`

Enumerating TCP services

* enumerates services associated with identified ports
* using `-sV` as in service version
* `nmap -sV <targets>`

UDP scan

* nmap sends a UDP packet to every targeted port mostly with no payload or with protocol-specific payload for a few more common ports
* nmap assigns one of the port states based on (no) response
* `sudo nmap -sU -p <port_range> <targets>`

OS detection

* `sudo nmap -O <targets>`

Intense scan

* combined TCP scanning, enumeration of TCP sevices, and some advanced scripts
* `nmap -T4 -A -v <targets>`

General options

* `--reason` shows the reason why nmap reports a host up or a port open
* `-v` increases verbosity level, `-vv` has even higher effect

### Enumeration Scripts

Nmap functionality can be extended using nmap scripts. The script can be found in `/usr/share/nmap/scripts/` on some systems.

* run the default set of scripts: `nmap -sC <targets>`
* run a particular script: `nmap --script <script_name> <targets>`
* asterisk `*` can be used to select a range or scripts, e.g., `nmap --script http* <targets>`
* if the target service is not running on its default port, add also `-p <port> -sV`
  * example: `nmap -p 12345 -sV --script ssh* <targets>`

HTTP Enumeration

* `nmap --script http-enum <targets>`

HTTP Methods

* enumerate which HTTP methods GET, POST, PUT, DELETE, OPTIONS are supported
* `nmap --script http-methods <targets>`

SMB Enumeration

* on port 445 by default
* `nmap -p 445 --script smb-os-discovery <targets>`
* `nmap -p 445 --script smb-enum-shares <targets>`

DNS Enumeration

* on port 53 by default
* `nmap -p 53 -A -v <targets>`

FTP Enumeration

* on port 21 by default
* `nmap --script ftp-syst --script ftp-anon <targets>`

MySQL Enumeration

* on port 3306 by default
* `nmap --script mysql-info <targets>`

SSH Enumeration

* on port 22 by default
* `nmap --script ssh2-enum-algos <targets>`
* `nmap --script ssh-brute <targets>`
* run all: `nmap --script ssh* <targets>`
* if not on default port: `nmap -p <port> -sV --script ssh2-enum-algos <targets>`

SMTP Enumeration

* on port 25 by default
* scripts could reveal several weaknesses such as open relays and acceptance of arbitrary commands
* `nmap --script smtp-commands <targets>`
* `nmap --script smtp-open-relay <targets>`

VNC Enumeration

* on port 5900 by default
* `nmap --script vnc-info <targets>`
* `nmap --script vnc-brute <targets>`

Service Banner Grabbing

* any service usually has a banner associated
* banners may even contain some organizational information
* `nmap --script banner <targets>`

## Detecting Vulnerabilities

Nmap can do a basic vulnerability assessment, but not as comprehensive as Nessus or OpenVAS. The vulnerability assessment is done with the help of Common Vulnerabilities and Exposures (CVE) IDs.

Installation:

```bash
cd /usr/share/nmap/scripts/
sudo git clone https://github.com/vulnersCom/nmap-vulners.git
sudo git clone https://github.com/scipag/vulscan.git
sudo nmap --script-updatedb
```

Run the scripts:

```bash
nmap -sV --script nmap-vulners/vulners --script vulscan <targets>
```

## Nmap Output

| Output Type | Argument | Example |
| ----------- | :------: | ------- |
| Text file   | `-oN`    | `nmap <targets> -oN output.txt` |
| XML file    | `-oX`    | `nmap <targets> -oX output.xml` |
| Greppable   | `-oG`    | `nmap <targets> -oX output.grep` |
| Append to previous | `--append-output` | `nmap <targets> -oN output.txt --append-output` |

## Nmap and Python

Install the required Nmap library: `pip install python-nmap`

Typicall usage:

```python
# import the nmap.py module
import nmap

# instantiate nmap.PortScanner object
nm = nmap.PortScanner()
```
