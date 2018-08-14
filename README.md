# spinfo
Service Port Information

This script written in Python3 can be executed in Linux shells. It is used for fetching "network service name" 
and its corresponding "port" information. "/etc/services" file is used as source data for this script:

Below are a few examples on how this script can be used:

GET HELP
========
  $ spinfo.py -h
  usage: spinfo [-h] [-S SERVICE [SERVICE ...] | -P PORT [PORT ...]] [-T | -U]

  optional arguments:
    -h, --help            show this help message and exit
    -S SERVICE [SERVICE ...], --service SERVICE [SERVICE ...]
    -P PORT [PORT ...], --port PORT [PORT ...]
    -T, --tcp
    -U, --udp

GET PORT INFO FOR A SERVICE(S)
==============================
Multiple service names with space delimited can be passed.
If a service name is prefixed with "~" sign, then the script does a "lazy" search. 
If a service name is not prefixed with "~" sign, then the script does a "specific" search.

    $ spinfo.py -S ssh
    
     SERVICE NAME     PORT NUMBER    PROTOCOL            SERVICE DESCRIPTION           
    --------------- --------------- ---------- ----------------------------------------
          ssh                    22    tcp     The Secure Shell (SSH) Protocol         
          ssh                    22    udp     The Secure Shell (SSH) Protocol         
          ssh                    22    sctp    SSH 
          
    $ spinfo.py -S ssh ~ldap

     SERVICE NAME     PORT NUMBER    PROTOCOL            SERVICE DESCRIPTION           
    --------------- --------------- ---------- ----------------------------------------
          ssh                    22    tcp     The Secure Shell (SSH) Protocol         
          ssh                    22    udp     The Secure Shell (SSH) Protocol         
          ssh                    22    sctp    SSH                                     
         ldap                   389    tcp                                             
         ldap                   389    udp                                             
         ldaps                  636    tcp     LDAP over SSL                           
         ldaps                  636    udp     LDAP over SSL                           
      www-ldap-gw              1760    tcp     www-ldap-gw                             
      www-ldap-gw              1760    udp     www-ldap-gw                             
      ldap-admin               3407    tcp     LDAP admin server port                  
      ldap-admin               3407    udp     LDAP admin server port                  
     bmc_ctd_ldap              6301    tcp     bmc-ctd-ldap # BMC CONTROL-D LDAP SERVER
     bmc_ctd_ldap              6301    udp     bmc-ctd-ldap # BMC CONTROL-D LDAP SERVER
     
          
GET SERVICE INFO FOR A PORT(S)
==============================
    $ spinfo.py -P 993

      PORT NUMBER    SERVICE NAME    PROTOCOL            SERVICE DESCRIPTION           
    --------------- --------------- ---------- ----------------------------------------
                993      imaps         tcp     IMAP over SSL                           
                993      imaps         udp     IMAP over SSL  
                

    $ spinfo.py -P 68 53 -U

      PORT NUMBER    SERVICE NAME    PROTOCOL            SERVICE DESCRIPTION           
    --------------- --------------- ---------- ----------------------------------------
                 68     bootpc         udp     dhcpc                                   
                 53     domain         udp 
