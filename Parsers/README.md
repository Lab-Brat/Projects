Imagine you have an email client that has a bug in it: when someone tries to send an email to 10+ people, it might create duplicates of that email and send it multiple times. This might not be a problem when there are 11 recipients, for example. However, when there are 200 recipients this could potentially waste a lot of space and bandwidth.

Fortunately, before buggy emails are all sent, they are stored in a buffer, where they will be store for about 5 minutes. Which means a Python script could be implemented to parse through the buffer, find the bugs and delete them before they are sent.
Email entries in the buffer are stored in the format below:

-Queue ID-  --Size-- ----Arrival Time---- -Sender/Recipient-------

Where ID is a unique identifire ending with a \*, size is the size of the email being sent, time is the arrival time in the buffer and sender/recipient could be one, or a list of email addresses. 

An email is deemed buggy when the size and the list of recipients is exactly the same, and this feature is exactly what the script will be trying to find.
