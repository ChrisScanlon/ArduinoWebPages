<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>








  
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>Ethernet Web Server ~E1</title></head><body>
<table style="width: 100%; text-align: left; margin-left: auto; margin-right: 0px;" border="0" cellpadding="0" cellspacing="0">

  <tbody>
    <tr>
      <td style="background-color: rgb(204, 255, 255);"><font size="+3"><span style="font-weight: bold;">Basic
Settings</span></font></td>
      <td style="text-align: right; background-color: rgb(0, 204, 204);"><font size="+3"><span style="font-weight: bold;">Ethernet
Web Server ~CN0&nbsp; <br>
</span></font></td><td style="vertical-align: top;">
      <table style="width: 100%; text-align: left; margin-left: auto; margin-right: 0px;" border="0" cellpadding="0" cellspacing="0">
<tbody><tr><td style="vertical-align: top; width: 141px; background-color: rgb(51, 102, 255);">IP:~IP0 <br>
MAC: ~IPM<br>
</td>
</tr></tbody>
      </table>
      </td>

    </tr>
  </tbody>
</table>

<br>

<table style="text-align: left; width: 100%; background-color: rgb(255, 204, 204);" border="0" cellpadding="0" cellspacing="0">

  <tbody>
    <tr>
      <td style="background-color: rgb(255, 204, 204);"><a href="home.cgi" target="_top">Home</a></td>
      <td style="background-color: rgb(255, 204, 204); font-weight: bold;"><a style="font-weight: normal;" href="basic.cgi" target="_top">Basic</a></td>
      <td><a href="sd.cgi" target="_top">Memory
Card</a></td>
      <td><a href="http.cgi" target="_top">HTTP</a></td>
      <td><a href="ftp.cgi" target="_top">FTP</a></td>
      <td style="background-color: rgb(255, 204, 204);"><a href="ntp.cgi" target="_top">SNTP</a></td>
      <td style="background-color: rgb(255, 204, 204);"><span style="text-decoration: underline;"><a href="email.cgi" target="_top">SMTP</a></span></td>
      <td style="background-color: rgb(255, 204, 204);"><a href="dyndns.cgi" target="_top">Dynamic DNS</a></td>
      <td style="background-color: rgb(255, 204, 204);"><a href="varibles.cgi" target="_top">Variables</a></td>
      <td><a href="varlogs.cgi" target="_top">Logs</a></td><td style="vertical-align: top;"><a href="Users.cgi" target="_top"><span style="text-decoration: underline;">Users</span></a></td>

    </tr>
  </tbody>
</table>

<br>

<span style="font-weight: bold;">Reset Options</span><br>

<table style="text-align: left; width: 100%; background-color: rgb(204, 204, 255);" border="0" cellpadding="0" cellspacing="0">

  <tbody>
    <tr>
      <td style="font-weight: bold;">User:</td>
      <td style="font-weight: bold;">~URA</td>
      <td>
      <form method="get" action="set"> <input maxlength="7" value="~URA" name="User" size="7"> <input value="Change User" type="submit"> </form>
      </td>
      <td>
      <form method="get" action="reset"><input name="reset" value="Master Reset" type="submit"></form>
      </td>
      <td><small>Limit use to prolong EEPROM</small><br>
      <form method="get" action="EEdefaults"><input name="EEDefaults" value="Create EEPROM Defaults" type="submit"></form>
      </td>
    </tr>
    <tr>
      <td style="font-weight: bold;">Password</td>
      <td style="font-weight: bold;">~PWA</td>
      <td>
      <form method="get" action="set"> <input maxlength="7" value="~PWA" name="Password" size="7"> <input value="Change Password" type="submit"> </form>
      </td>
      <td><br>
      </td>
      <td>
      <table style="text-align: left; width: 100%; background-color: rgb(204, 204, 255);" border="0" cellpadding="0" cellspacing="0">
        <tbody>
          <tr>
            <td style="vertical-align: top;">Values
File <br>
            <table style="text-align: left; width: 100%; font-weight: bold; background-color: rgb(204, 255, 255);" border="0" cellpadding="0" cellspacing="0">
              <tbody>
                <tr>
                  <td colspan="1" rowspan="1" style="background-color: rgb(204, 255, 255);"><a href="values.dat" target="_blank">values.dat</a></td>
                </tr>
              </tbody>
            </table>
            </td>
          </tr>
        </tbody>
      </table>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;">&nbsp;Settings File <br>
      <table style="text-align: left; width: 100%; font-weight: bold; background-color: rgb(204, 255, 255);" border="0" cellpadding="0" cellspacing="0">
        <tbody>
          <tr>
            <td><a href="settings.txt" target="_blank">settings.txt</a></td>
            <td>
            <form method="get" action="email"><input name="settings.txt" value="Email Settings File" type="submit"></form>
            </td>
          </tr>
        </tbody>
      </table>
      </td>
      <td style="vertical-align: top;">
      <form method="get" action="csettings"><input value="Create Default Settings File" name="settings.txt" type="submit"><br>
From current settings<br>
      </form>
      </td>
      <td style="vertical-align: top;">&nbsp; Log File&nbsp; <a href="log.txt" target="_blank">log.txt</a>
      <form method="get" action="email"><input name="log.txt" value="Email Log File" type="submit"></form>
      </td>
    </tr>
  </tbody>
</table>

<br>

<span style="font-weight: bold;">Basic Settings</span>
<br>

<table style="text-align: left; width: 100%; font-weight: bold; background-color: rgb(102, 204, 204);" border="0" cellpadding="0" cellspacing="0">

  <tbody>
    <tr>
      <td>MAC
Address</td>
      <td>~IPM<br>
      </td>
      <td>&nbsp;
      <form method="get" action="set"> <input maxlength="32" value="~IPM" name="MAC" size="32"> <input value="Change MAC Address" type="submit"> </form>

      </td>
      <td>Server Port

      </td>
      <td>~IPA
      </td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPA" name="ServerPort" size="32"> <input value="Change Server Port" type="submit"> </form>

      </td>
    </tr>
    <tr>
      <td>IP
Address</td>
      <td>~IP0</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IP0" name="IPAddress" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td>Default
IP Address</td>
      <td>~IPD</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPD" name="DefaultIPAddress" size="32"> <input value="Change Default IP Address" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td>Subnet
Mask</td>
      <td>~IPN</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPN" name="SubnetMask" size="32"> <input value="Change Subnet Mask" type="submit"> </form>
      </td>
      <td>Gateway
IP Address</td>
      <td>~IPG</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPG" name="Gateway" size="32"> <input value="Change Gateway" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td>Primary
DNS Server</td>
      <td>~IPP</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPP" name="PrimaryDNS" size="32"> <input value="Change Primary DNS" type="submit"> </form>
      </td>
      <td>Secondary
DNS Server</td>
      <td>~IPS</td>
      <td>
      <form method="get" action="set"> <input maxlength="32" value="~IPS" name="SecondaryDNS" size="32"> <input value="Change Secondary DNS" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td><br>
      </td>
      <td><br>
      </td>
      <td><br>
      </td>
      <td><br>
      </td>
      <td colspan="1" rowspan="1"><br>
      </td>
      <td><br>
      </td>
    </tr>
    <tr>
      <td style="background-color: rgb(204, 153, 51);">IP Interfaces</td>
      <td style="background-color: rgb(204, 153, 51);">&nbsp;~IP1</td>
      <td style="background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP1" name="IPAddress1" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td style="background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="background-color: rgb(204, 153, 51);"><br>
</td>
    </tr>
    <tr>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP2<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP2" name="IPAddress2" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP3<br>
      </td>
      <td style="background-color: rgb(204, 153, 51);">
      <form method="get" action="set"><input maxlength="32" value="~IP3" name="IPAddress3" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP4<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP4" name="IPAddress4" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP5<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP5" name="IPAddress5" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP6<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP6" name="IPAddress6" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP7<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP7" name="IPAddress7" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP8<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP8" name="IPAddress8" size="32"> <input value="Change IP Address" type="submit"> </form>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);"><br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">~IP9<br>
      </td>
      <td style="vertical-align: top; background-color: rgb(204, 153, 51);">
      <form method="get" action="set"> <input maxlength="32" value="~IP9" name="IPAddress9" size="32"> <input value="Change IP Address 9" type="submit"> </form>
      </td>
    </tr>
  </tbody>
</table>

<br>

<span style="font-weight: bold;"></span><span style="font-weight: bold;">System
Log</span><br>

<br>

<iframe src="log.txt" height="400" width="100%">&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;p&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;Your
browser does not
support
iframes.&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/p&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;
</iframe><br>

<br>

<br>

<div style="text-align: center;"><font style="font-weight: bold;" size="+1"><span style="font-style: italic;">This page was generated on
~E2.
</span></font><br>
</div>

</body></html>
