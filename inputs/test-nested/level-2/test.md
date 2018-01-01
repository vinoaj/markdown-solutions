Title: Google Cloud Platform: assigning a static IP address to a VM instance

An external IP address is assigned to every Google Cloud Platform virtual machine (VM) instance that you create. 

This IP address can be used in your DNS settings so that users can access the instance via a domain name. The problem, however, is that the IP address resets whenever the VM instance is restarted. This means that every time you restart your VM instance, you will need to update your various configurations (e.g. DNS, load balancing) to reference the new IP address.

You can bypass this issue by **reserving and assigning a static IP address** for an instance. An added bonus is that this is free! However, you will be [charged USD$0.01/hour for unused IP addresses](https://cloud.google.com/compute/pricing?hl=en_US#ipaddress) - i.e. reserved static IP addresses that are not attached to an instance or forwarding rule.

[adinserter block=1]


#Concepts
##Regional vs Global IP addresses
**Regional** IP addresses can be used by:

+ VM instances
+ *Network* load balancers

**Global** IP addresses are used for *global* load balancers.


#How to reserve and assign a static IP address to a Google Cloud Platform VM instance
Navigate to the Google Cloud Platform Console page for your project.

Using the left-hand menu, navigate to *Networking > VPC network > External IP addresses*
[TODO: image]

Click on *+ Reserve Static Address*
[TODO: image]

Edit the settings:

+ **Name**: a name to describe this IP reservation (e.g. "webserver-primary-ip")
+ **IP version**: IPv4 or IPv6 depending on your needs
+ **Type**: Regional if you want to use it for accessing a VM instance
+ **Region**: Select the same region as where your VM instance lives
+ **Attached to*: Select the instance you wish to attach the static IP address to
+ Click on *Reserve* to save your settings
[TODO: image]

You will be taken back to the [External IP addresses list page](https://console.cloud.google.com/networking/addresses/list). Here you can see the new IP address that has been assigned to your instance.
[TODO: image]

This IP address can now be used in your DNS settings.

[adinserter block=1]



