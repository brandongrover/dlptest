# DLP Testing for Canadian PII
<p>Some dataset generators, receivers, and test cases.</p>
<br>
<br>

#### Python3 SMTPD Listener

<p>Simple listener to accept SMTP messages to stdout.</p>
 python3 -m smtpd -n -c DebuggingServer 0.0.0.0:2525 >> mail.txt
<br>

#### DNS Listener

<p>Receive, respond to, and save DNS requests to a text file</p>
py .\receivers\fakedns.py <optional_port_number>
<br>

#### Create Data

<p>Creates various formats of Drivers License, SIN, Date of Birth, and Address for txt, csv, and pdf files.<br>
Modify main if you would like to generate more or less of these.</p>
py .\data_generator\file_creator.py
<br>