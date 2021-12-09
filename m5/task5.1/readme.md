# Task 5.1

*PART 1*

1. Log in to the system as root.  

* ![](screen/Screenshot_1.png)

2. Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change *?

* ![](screen/Screenshot_2.png)

man passwd

* ![](screen/Screenshot_3.png)

3)  Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?

* ![](screen/Screenshot_4.png)

Here we see list of users , they additional information, they home directory, they groups and id.

4) Change personal information about yourself.

* ![](screen/Screenshot_5.png)

* ![](screen/Screenshot_6.png)

5 Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.

* ![](screen/Screenshot_7.png)

* ![](screen/Screenshot_8.png)

* ![](screen/Screenshot_9.png)

6. Explore the more and less commands using the help system. View the contents of files .bash* using commands.

user@user-Virtual-Machine:/etc$ more --help

* ![](screen/Screenshot_10.png)

user@user-Virtual-Machine:/etc$ less --help

* ![](screen/Screenshot_11.png)

user@user-Virtual-Machine:/etc$ more bash.bashrc

* ![](screen/Screenshot_12.png)

user@user-Virtual-Machine:/etc$ less bash.bashrc

* ![](screen/Screenshot_13.png)

7. * Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.

* ![](screen/Screenshot_14.png)

* ![](screen/Screenshot_15.png)

* ![](screen/Screenshot_16.png)

8. * List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.

* ![](screen/Screenshot_17.png)

* ![](screen/Screenshot_18.png)

# Task 5.1

*PART 2*

1. Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level. 

* ![](screen/Screenshot_19.png)

* ![](screen/Screenshot_20.png)

* ![](screen/Screenshot_21.png)

* ![](screen/Screenshot_22.png)

2. What command can be used to determine the type of file (for example, text or binary)? Give an example.

* ![](screen/Screenshot_23.png)

* ![](screen/Screenshot_24.png)

3. Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

* ![](screen/Screenshot_25.png)

4. Become familiar with the various options for the ls    command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches.

* ![](screen/Screenshot_26.png)

* ![](screen/Screenshot_27.png)

5. Perform the following sequence of operations: -  create a subdirectory in the home directory;-  in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);-  view the created file;-  copy the created file to your home directory using relative and absolute addressing.-  delete the previously created subdirectory with the file requesting removal;-  delete the file copied to the home directory.

* ![](screen/Screenshot_28.png)

* ![](screen/Screenshot_29.png)

6. Perform the following sequence of operations:-  create a subdirectory testin the home directory;
-  copy the .bash_historyfile to this directory while changing its name to labwork2;-  create a hard and soft link to the labwork2file in the test subdirectory; -  how to define soft and hard link, what do theseconcepts;-  change the data by opening a symbolic link. What changes will happen and why -  rename the hard link file to hard_lnk_labwork2;-  rename the soft link file to symb_lnk_labwork2 file; -  then delete the labwork2. What changes have occurred and why?

* ![](screen/Screenshot_30.png)

7. Using the locate utility, find all files that contain the squid and traceroute sequence.

* ![](screen/Screenshot_31.png)

8. Determine which partitions are mounted in the system, as well as the types of these partitions.

* ![](screen/Screenshot_32.png)

* ![](screen/Screenshot_33.png)

* ![](screen/Screenshot_34.png)

9. Count the number of lines containing a given sequence of characters in a given file. 

* ![](screen/Screenshot_35.png)

10. Using the findcommand, find all files in the /etc directory containing the host character sequence.

* ![](screen/Screenshot_36.png)

11. List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep? 

* ![](screen/Screenshot_37.png)

* ![](screen/Screenshot_38.png)

12. Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.

* ![](screen/Screenshot_39.png)

13. What are the types of devices and how to determine the type of device? Give examples.

* ![](screen/Screenshot_40.png)

* ![](screen/Screenshot_41.png)

* ![](screen/Screenshot_42.png)

* ![](screen/Screenshot_43.png)

14. How to determine the type of file in the system, what types of files are there? 

* ![](screen/Screenshot_44.png)

15.* List the first 5 directory files that were recently accessed in the /etcdirectory. 

* ![](screen/Screenshot_45.png)