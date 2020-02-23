# Penetration Testing

Phases of penetration testing:

1. Reconnaissance / Information gathering
    * gather as much information as possible using passive and active techniques
    * tools: nmap and metasploit
2. Enumeration
    * probe the target in detail and find the exact service versions running on the target
    * tools: nmap and metasploit
3. Vulnerability assessment
    * look for existence of any known vulnerabilities
    * tools: OpenVAS
4. Gaining access
    * attempt to exploit the found vulnerabilties to gain access to the system
    * tools: metasploit
5. Escalating priviledges
    * after gaining access, escalate the priviledges to the highest level
    * tools: metasploit
6. Maintaining access
    * make the access persistent
    * tools: metasploit
7. Covering tracks
    * clean up any traces left during previous phases, such as garbage files, modified configuration files, changed registry entries, and logs
    * tools: metasploit
