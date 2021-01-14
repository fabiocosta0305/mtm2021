# MTM 2021 Grand Challenge - Extracting Data from SDSF for loading on another place

## Prequesites

### z/OS

+ REXX Script on a PDS
  + Place the script included on `rexx/sdsfret.rexx` on a PDS
  + With ZOWE, use the command `zowe files upload ftds rexx/sdsfret.rexx '<MY-PDS>'`
+ User with Permissions to read information from all the jobs on SDSF
+ z/OS Automation Utils deployed

### Linux

+ Ansible Playbook with z/OS Core Collections Installed
  + Use `ansible-galaxy collection install ibm.ibm_zos_core`
+ Ansible Runner library installed on Python
  + Use `pip3 install ansible_runner` if needed
  
### Usage

By running this script, you'll have a list of data that can by inserted on any metric collector or RDBMS as a JSON object.      