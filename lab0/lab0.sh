# 2.1 Fetch a Web Page
# fetchWebPage='GET /lab0/0 HTTP/1.1\r\nHost: cs144.keithw.org\r\nConnection: close\r\n\r\n'
# echo -e $fetchWebPage | nc cs144.keithw.org http

# 2.2

smtp='
HELO k\n
MAIL FROM: daat00@sjtu.edu.cn\n
RCPT TO: daat00@sjtu.edu.cn\n
DATA\n
From: daat00@sjtu.edu.cn\n
To: daat00@sjtu.edu.cn\n
Subject: Test!\n
\r\n.\r\n
QUIT
'
echo -e $smtp | telnet smtp.sjtu.edu.cn smtp
