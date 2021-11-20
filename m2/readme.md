## Module 2 NetworkingFundamentals

# Task 3.1 Create Enterprise, Data Center, Home Office and add ip adresses for them (I was born 13.04.1986)

1. Create Enterprise

* ![](screen/Screenshot_1.png)

2. Data Center

* ![](screen/Screenshot_2.png)

3. Home Office

* ![](screen/Screenshot_3.png)

## Work with Wireshark

* ![](screen/Screenshot_4.png)

*Source MAC Address: 00:31:92:13:df:ad  <br/>
*Destination MAC Address: 30:9c:23:7f:e2:b1 <br/>
*Source IP Address: 79.142.76.130 <br/>
*Destination IP Address: 192.168.88.103 <br/>
*Source TCP Port : 443 <br/>
*Destination TCP port: 60184 <br/>

# Task 3.2 Vlan and connection of different networks

5 and 6 Check ping to the DefaultGateways

* ![](screen/Screenshot_5.png)

* ![](screen/Screenshot_6.png)

* ![](screen/Screenshot_7.png)

7. Change mask to the 255.255.255.192 and check ping.

* ![](screen/Screenshot_8.png)

* ![](screen/Screenshot_9.png)

8. There is a ping only between web server 1 and the gateway, since they are in the same subnet range.

* ![](screen/Screenshot_10.png)

10. There will be no ping due to the lack of routes between Vlans on the switch

* ![](screen/Screenshot_11.png)

12. Configuring inter-Vlan routing

* ![](screen/Screenshot_12.png)

* ![](screen/Screenshot_15.png)

Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.<br/>
Router(config-if)#interface GigabitEthernet0/0.2<br/>
Router(config-subif)#encapsulation dot1Q 2<br/>
Router(config-subif)#eneip address 4.13.86.1 255.255.255.192<br/>
Router(config-subif)#interface GigabitEthernet0/0.3<br/>
Router(config-subif)#<br/>
%LINK-5-CHANGED: Interface GigabitEthernet0/0.3, changed state to up<br/>

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0.3, changed state to up<br/>
interface GigabitEthernet0/0.3<br/>
Router(config-subif)#interface GigabitEthernet0/0.3<br/>
Router(config-subif)#encapsuip address 4.13.86.1 255.255.255.192ip address 4.13.86.65 255.255interface GigabitEthernet0/0.3interface<br/> GigabitEthernet0/0.4<br/>
Router(config-subif)#<br/>
%LINK-5-CHANGED: Interface GigabitEthernet0/0.4, changed state to up<br/>

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0.4, changip address 4.13.encapsulation dot1Q 3encapsip address 4.13.86.65<br/> 255.255.255.192ip address 4.13.86.129 255.255.255.192<br/>
Router(config-subif)#eiexit<br/>
Router(config)#txtexit<br/>

15. Change Gateways

* ![](screen/Screenshot_13.png)

16. Testing connection by ping

* ![](screen/Screenshot_14.png)

# Task 3.3 Routing settings
 
1. In Task 3.2.2 my internet connection is 23.4.86.00/26

* ![](screen/Screenshot_16.png)

* ![](screen/Screenshot_17.png)

2. Configure routing on the HomeRouter 

* ![](screen/Screenshot_18.png)

3. Check network performance using the ping and tracert commands between Client1 and WebServer2.

* ![](screen/Screenshot_19.png)

