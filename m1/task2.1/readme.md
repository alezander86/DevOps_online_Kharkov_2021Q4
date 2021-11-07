# Task 2.1
## Part 1
**1. What are the most popular hypervisors for infrastructure virtualization?**

***1. Native Hypervisors.
They runs directly on the host's hardware to control the hardware and to manage guest operating 
** VMware ESX
** Microsoft Hyper-V
** Citrix XenServer
** Oracle VM Server for SPARC
** Oracle VM Server for x86
** Nutanix AHV

***2. Hosted Hypervisors.
They runs on a conventional operating system (OS) just as other computer programs do. A guest operating system runs as a process on the host.
** VMware Workstation
** VirtualBox 
** Microsoft Virtual PC
** QEMU 
** Parallels Desktop for Mac

### **Features of popular Hypervisors**
** 2. Briefly describe the main differences of the most popular hypervisors.

Scalability,Performance;Density

* ![](screen/table1.png)

High Availability & Resiliency

* ![](screen/table2.png)

## Part 2

### **Work with VirtualBox**

1. VirtualBox version
* ![](screen/Screenshot_1.png)

2. Create VM1 - VM1_TARYRAIEV
* ![](screen/Screenshot_2.png)

3. Install Ubuntu 20.04

4. Make Clone VM1 - VM1_TARYRAIEV
* ![](screen/Screenshot_3.png)

5. Make Group
* ![](screen/Screenshot_4.png)

6. Make snapshots of VM1 - VM1_TARYRAIEV
* ![](screen/Screenshot_5.png)

7. Export VM1_TARYRAIEV to .ova file.
* ![](screen/Screenshot_6.png)


### **Virtual machines configuration**

1. Configure Shared folder beetween VMhost and VM1_TARYRAIEV.
* ![](screen/Screenshot_7.png)
* ![](screen/Screenshot_8.png)

2. Configure connect from host USB port to guest USB port.
* ![](screen/Screenshot_9.png)
* ![](screen/Screenshot_10.png)
* ![](screen/Screenshot_11.png)


3. Configure different network modes for VM1, VM2.
Connection Table

<table>
	<tr>	
		<td>Mode</td><td>VM -> Host</td><td>VM <- Host</td><td>VM1 <-> VM2</td><td>VM -> Net/LAN</td><td>VM -> Net/LAN</td>
	</tr>
	<tr>
		<td>Host-only</td><td>+</td><td>+</td><td>+</td><td>-</td><td>-</td>
	</tr>
	<tr>
		<td>Internal</td><td>-</td><td>-</td><td>+</td><td>-</td><td>-</td>
	</tr>
	<tr>
		<td>Bridged</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td>
	</tr>
	<tr>
		<td>NAT</td><td>+</td><td><a href="https://www.virtualbox.org/manual/UserManual.html#natforward">Port forward</a></td><td>-</td><td>+</td><td><a href="https://www.virtualbox.org/manual/UserManual.html#natforward">Port forward</a></td>
	</tr>
	<tr>
		<td>NATservice</td><td>+</td><td><a href="https://www.virtualbox.org/manual/UserManual.html#network_nat_service">Port forward</a></td><td>+</td><td>+</td><td><a href="https://www.virtualbox.org/manual/UserManual.html#network_nat_service">Port forward</a></td>
	</tr>
</table>  

4. Configure different network modes for VM1_TARYRAIEV, VM2_TARYRAIEV.

### **Table of mode connections**
* ![](screen/table.png)

### **NAT mode.**
* ![](screen/Screenshot_12.png)
* ![](screen/Screenshot_13.png)

### **Bridged mode**
* ![](screen/Screenshot_14.png)
* ![](screen/Screenshot_15.png)

### **Internal network**
* ![](screen/Screenshot_16.png)
* ![](screen/Screenshot_17.png)
* ![](screen/Screenshot_18.png)

### **Host-only adapter**
* ![](screen/Screenshot_19.png)
* ![](screen/Screenshot_20.png)

-----------

## **VBoxManage**

1. list vms and showvminfo command
* ![](screen/Screenshot_21.png)

3. creatvm command
* ![](screen/Screenshot_22.png)

4. start VM , reset VM, stop VM, take snapshot of VM, clone VM and rename VM 
* ![](screen/Screenshot_23.png)

-----------

## Part 3

### **Vagrant**

1. Create folders , Initialized the environment with the default Vagrant box, Start vagrant vm.
* ![](screen/Screenshot_24.png)

4. Connect to vm by ssh (MobaXterm)
* ![](screen/Screenshot_25.png)

5. Check Date
* ![](screen/Screenshot_26.png)

6. Stop and delete VM
* ![](screen/vag6.png)

7. Create own vagrant box
* ![](screen/vag7.png)

-----------