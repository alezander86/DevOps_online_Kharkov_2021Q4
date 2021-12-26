# Task 7.1

** A. Create a script that uses the following keys:

** 1. When starting without parameters, it will display a list of possible keys and their description. 

* ![](screen/Screenshot_1.png)

** 2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet.

* ![](screen/Screenshot_2.png)

** 3. The --target key displays a list of open system TCP ports.

* ![](screen/Screenshot_3.png)

<details>
	<summary>bash script</summary>

  ```
#!/bin/bash

if [ "$1" == "--all" ];
then

    n=1
    while [ $n -lt 256 ]; do
       i=$2.$n
       nslookup $i | awk -v var=$i '/name/{print "IP:" var, "Hostname:" $4}'
       n=$(($n+1));
   done

elif [ "$1" == "--target" ];

then

    echo "Open ports:"
    nc $2 -z -v 1-65000 2>&1 | grep succeeded | awk '/tcp/{print $3 " " $4}'

else
    echo "You need to choice option"
    echo "############################################"
    echo "--all : Scan subnet fo every available host IP in a subnet"
    echo "Example: ./1.sh --all 192.168.8"
    echo "--target : for scan open ports by IP"
    echo "Example: ./1.sh --target 192.168.8.1"
fi
  ```
</details>


** The code that performs the functionality of each of the subtasks must be placed in a separate function

** B. Using Apache log example create a script to answer the following questions:

** 1. From which ip were the most requests?

* ![](screen/Screenshot_4.png)

** 2. What is the most requested page? 

* ![](screen/Screenshot_5.png)

** 3. How many requests were there from each ip? 

* ![](screen/Screenshot_6.png)

** 4. What non-existent pages were clients referred to?  

* ![](screen/Screenshot_7.png)

** 5. What time did site get the most requests? 

* ![](screen/Screenshot_8.png)

** 6. What search bots have accessed the site? (UA + IP)

* ![](screen/Screenshot_9.png)

<details>
	<summary>bash script</summary>

  ```
#!/bin/bash
if [[ "$1" == "0" ]]
then
   echo " "
   echo "You need path to log file"
   echo "##############################"
   echo "Example: ./log example_log.log"
   echo " "
else
   echo "1. From which ip were the most requests?"
   echo "2. What is the most requested page?"
   echo "3. How many requests were there from each ip?"
   echo "4. What non-existent pages were clients referred to?"
   echo "5. What time did site get the most requests?"
   echo "6. What search bots have accessed the site? (UA + IP)"
   read -p "Make your choice: " n

    case $n in
      1)
         awk '{ print $1 }' $1 | sort -g | uniq -c | sort -nr | head -1 | awk '{ print $2 }'
      ;;
      2)
         awk '{ print $7 }' $1 | sort | uniq -c | sort -nr | head -1 | awk '{ print $2 }'
      ;;
      3)
         awk '{ print $1 }' $1 | sort -g | uniq -c | sort -nr
      ;;
      4)
         awk '$9 == "404" { print $7 }' $1 | sort | uniq
      ;;
      5)
         awk '{ print $4 }' $1 | cut -d":" -f2,3 | uniq -c | sort -nr |head -1 | awk '{ print $2 }'
      ;;
      6)
         awk -F'"' '{ print $1 $(NF-1) }' $1 | grep -iE "(Google|bot|fetcher|analyzer|scraper|crawler)" | sed 's/\- \[[^]]*\] //g' | sort | u>
      ;;
    esac
fi
  ```
</details>

** C. Create a data backup script that takes the following data as parameters:

** 1. Path to the syncing  directory.

** 2. The path to the directory where the copies of the files will be stored.

In case of adding new or deleting old files, the script must add a corresponding entry to the log file indicating the time, type of operation and file name. [The command to run the script must be added to crontab with a run frequency of one minute]