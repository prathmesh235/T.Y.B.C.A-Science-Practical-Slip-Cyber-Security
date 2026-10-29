MAN-IN-THE-MIDDLE ATTACKS AND PACKET SNIFFING
Q. Explain Man-In-The-Middle (MITM) attacks and Packet Sniffing along with their preventive measures. [10 Marks]

1. MAN-IN-THE-MIDDLE (MITM) ATTACK
A Man-In-The-Middle (MITM) attack occurs when an attacker secretly places himself between two communicating parties 
(for example, a user and a website), intercepts the traffic, and may read or modify it while both sides believe they 
are talking directly to each other. It breaks confidentiality and integrity.
Flow: User <-> Attacker <-> Website/Server
Types: Wi-Fi eavesdropping (fake hotspot), ARP spoofing, DNS spoofing, session hijacking, SSL stripping.
Example: On free public Wi-Fi, an attacker's fake hotspot captures a user's login details while the user is logging in to an online account.
Prevention: Use HTTPS/TLS and check the padlock; use a VPN on public Wi-Fi; avoid unknown Wi-Fi networks; enable multi-factor authentication;
use WPA2/WPA3 on Wi-Fi; use certificate validation and HSTS; keep software updated.

2. PACKET SNIFFING
Packet sniffing is the process of capturing and analysing data packets travelling over a network using a sniffer tool (for example, Wireshark or tcpdump). 
Network administrators use it legitimately for troubleshooting, but attackers misuse it to read unencrypted data such as passwords, emails and chats.
Working: The network card is put in promiscuous mode, so it captures all packets passing on the network, not only those meant for it. This works best on 
hubs and open Wi-Fi.
Types: Passive sniffing (only listens, e.g. on a hub or open Wi-Fi) and Active sniffing (injects traffic such as ARP poisoning to capture data on a switched network).
Example: A sniffer on an open Wi-Fi network captures a plain HTTP login page and reads the username and password in clear text.
Prevention: Encrypt data (HTTPS, SSH, SFTP, VPN); use switches instead of hubs; use strong Wi-Fi encryption (WPA3); enable port security and dynamic ARP inspection; 
run intrusion detection systems (IDS); monitor for sniffers/promiscuous interfaces; avoid public Wi-Fi.

