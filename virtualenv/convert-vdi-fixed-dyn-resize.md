# Convert VDIs Between Fixed-Sized and Dynamic In VirtualBox

Suppose you're working on a virtual machine, but you suddenly run out of disk drive space.

* Shutdown the virtual machine
* If the drive is fixed size, create a clone of _Standard_ variant
```
$ VBoxManage clonehd osboxub.vdi osboxdyn.vdi --variant Standard
```
* Then resize the drive using `modifyhd` command, specifying the size in mb.
```
$ VBoxManage modifyhd osboxdyn.vdi --resize 50000
```
