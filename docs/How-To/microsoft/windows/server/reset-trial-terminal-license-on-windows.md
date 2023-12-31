While Windows installed with Terminal Server role it does work without License for 120 Days on trail license, where within 120 days if the License server is not Connected the server will stop accepting connection with below error and event ID

![alt text](images/error-no-licence.png)

**EventID: 1128**
**Source: TerminalServices-RemoteConnectionManager**

The RD Licensing grace period has expired and the service has not registered with a license server with installed licenses. A RD Licensing server is required for continuous operation. A Remote Desktop Session Host server can operate without a license server for 120 days after initial start up.

![event 1129](images/1128eventid.png)

The official solution is to Activate the RDS/TS CAL License server and point the Server to License server with User/Device License and will be resolve the problem

But if you want to reset the timer and again avail 120 days grace time  here is the solution

The solution was to delete the REG_BINARY in
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod`
Only leaving the default.

![registry editor](images/regkey-650x424.png)

Note: you must take ownership and give admin users full control to be able to delete this key.

After a reboot the server should be working again for another 120 Days.

Here is the [link](http://anilgprabhu.blogspot.com/2014/05/reset-trial-terminal-license-on-windows.html) to the original article.
