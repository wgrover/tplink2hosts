# tplink2hosts
Export /etc/hosts file content from the Clients list of a TP-Link wireless router website

1.  In the terminal, install the dependency `pyperclip` using `pip3 install pyperclip`
2.  In your TP-Link router's admin website, click "Network Map", then "Clients".
3.  Hit `command` + `a` (or `ctrl` + `a`) to select everything on the page.
4.  Hit `command` + `c` (or `ctrl` + `c`) to copy the contents of the page to the clipboard.
5.  In the terminal, run `python3 tplink2hosts`.  The program will parse the contents of the clipboard and print just the IP addresses and hostnames separated with `tab` characters, ready to copy and paste into `/etc/hosts` on your [Pi-hole](https://pi-hole.net) or wherever else you need to use this information.

Tested to work on a Mac (MacOS 12.5) using Safari (15.6) and a TP-Link Archer AXE75 v1.0 router using firmware 1.0.5 Build 20220405 rel.80113(5553).