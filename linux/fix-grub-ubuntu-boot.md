# How To Repair Grub Boot Loader On Ubuntu Linux 16.04

I have Ubuntu 16.04 installed on one SSD and Windows 10 on another SSD.
Boot Repair is the most commonly used tool to fix errors regarding Grub boot loader. First of all arrange a Live CD/DVD/ USB for Ubuntu and boot your system using this media (If you are looking to repair Grub, chances are you are already on the stage where system is un-bootable into current operating system, so yes its a valid request to use Live CD/DVD/USB at this point).

Once you are logged into your system using Live disk, run following command to add “Boot Repair” tool’s PPA to your system.

```
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt-get update
sudo apt-get install -y boot-repair
```

Open Boot Repair from the menu. And follw the instructions.

