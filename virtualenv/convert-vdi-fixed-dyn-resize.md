# Convert VDIs Between Fixed-Sized and Dynamic In VirtualBox

Suppose you're working on a virtual machine, but you suddenly run out of disk drive space.

* Shutdown the virtual machine
* If the drive is fixed size, create a clone of _Standard_ variant
```
VBoxManage clonehd osboxub.vdi osboxdyn.vdi --variant Standard
```
* Then resize the drive using `modifyhd` command, specifying the size in mb.
```
VBoxManage modifyhd osboxdyn.vdi --resize 50000
```
* Extend the primary partition to include the new drive space. Download the Gparted live cd or what ever partition manager program you wish and mount it to the guests virtual CD and boot the guest. From here you can expand the primary partition to use the new space.


### What if I used Fixed Disks, or VMDK?
```
VBoxManage clonehd <infilename or UUID> <outfilename> --format VDI --variant Standard
```
