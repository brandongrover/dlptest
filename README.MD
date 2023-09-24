# DLP Testing for Canadian PII
<p>Some dataset generators, receivers, and test cases.</p>
<br>
<br>

#### Python3 SMTPD Listener

<p>Simple listener to accept SMTP messages to stdout.<br>
__py -m smtpd -n -c DebuggingServer localhost:25__</p>
<br>

#### DNS Listener

<p>Receive, respond to, and save DNS requests to a text file</p>
__py .\receivers\fakedns.py <optional_port_number>__
<br>

#### Create Data

<p>Creates various formats of Drivers License, SIN, Date of Birth, and Address for txt, csv, and pdf files.<br>
Modify main if you would like to generate more or less of these.</p>
** py .\data_generator\file_creator.py **
<br>