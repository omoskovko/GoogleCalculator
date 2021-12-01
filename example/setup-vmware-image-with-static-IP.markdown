# How to setup your VMWare Fusion images to use static IP addresses on Mac OS X

At [Crush + Lovely](http://crushlovely.com), we use [Railsmachine's](http://railsmachine.com) [Moonshine](http://github.com/railsmachine/moonshine) to automate the configuration of our servers.  When writing our deployment recipes, VMWare Fusion's ability to take snapshots and rollback to these snapshots is a huge timesaver because it takes just seconds to roll a server image to it's original state.

When you're just configuring a single server, having a static IP address for your server image isn't too important, but when you're configuring multi-server setups, it can be useful to duplicate a number of server images and give each a static IP address so you can consistently deploy to them.  While not documented well at all, it turns out that this is relatively easy to accomplish in four simple steps.

## 1. Determine the MAC address of your guest machine

Let's say you have a guest machine with the name `ubuntu-lucid-lynx-base` and you keep your guest machine images in `~/Documents/Virtual\ Machines/`.  To determine the MAC address for this VM, you can run:

```
cat ~/Documents/Virtual\ Machines/ubuntu-lucid-lynx-base.vmwarevm/ubuntu-lucid-lynx-base.vmx | grep ethernet0.generatedAddress
```

If more than one line is returned, you're looking for the one with the value like `00:0c:29:9d:2a:38`.

## 2. Add your static IP address to VMWare's `dhcpd.conf`

Open `/Library/Application\ Support/VMware\ Fusion/vmnet8/dhcpd.conf`. `vmnet8` is the virtual interface for NAT networking in VMWare the guest machines.  In this file, you'll see a subnet clause that looks something like this:

```
subnet 172.16.179.0 netmask 255.255.255.0 {
	range 172.16.179.128 172.16.179.254;
	option broadcast-address 172.16.179.255;
	option domain-name-servers 172.16.179.2;
	option domain-name localdomain;
	default-lease-time 1800;                # default is 30 minutes
	max-lease-time 7200;                    # default is 2 hours
	option routers 172.16.179.2;
}
```

Take note of the line starting with `range`.  The IP addresses you will assign your guest machines will need to fall *outside* that range.  Find the line that looks like this:

```
####### VMNET DHCP Configuration. End of "DO NOT MODIFY SECTION" #######
```

Below that line, add a clause for your guest machine.  It should look like this:

```
host ubuntu-lucid-lynx-base {
    hardware ethernet 00:0c:29:9d:2a:38;
    fixed-address 172.16.179.102;
}
```

Make sure the `hardware ethernet` value matches the MAC address you found in step one, and the `fixed-address` is an IP outside the range listed in the `subnet` clause.

## 3. Optional: Update your `/etc/hosts` file

If you want to assign a fancy local hostname that refers to your guest machine, you can do so by editing your `/etc/hosts` file.  For instance, to assign the hostname `ubuntu.local` to the guest machine we just setup, we could add the following line to our `/etc/hosts` file:

```
172.16.179.102 ubuntu.local
```

## 4. Restart the VMWare daemons

Last thing to do is restart your VMWare daemons:

```
sudo "/Library/Application\ Support/VMware\ Fusion/boot.sh" --restart
```

* _original source_: http://crshlv.ly/rjlXdS
* _note_: These instructions have been tested on Snow Leopard only.

Wahooo! Found the solution via a forked gist. :p I just had to restart services (https://gist.github.com/mgutz/1b8b5569190155dc31b9).
```
sudo /Applications/VMware\ Fusion.app/Contents/Library/services.sh --stop
sudo /Applications/VMware\ Fusion.app/Contents/Library/services.sh --start
```
