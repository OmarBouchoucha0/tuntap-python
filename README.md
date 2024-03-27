# tuntap-python
a implementation of the tuntap devices on linux to test tcp connetcion

# # refrences
tun_tap = https://en.wikipedia.org/wiki/TUN/TAP
ps : you can't change the capabilities with setcap(linux) on a python sctipt you hace to set 
to the executable itself(not recommanded) , the solution i cameup with is to make a wrapper
script.
https://unix.stackexchange.com/questions/389879/how-to-set-capabilities-with-setcap-command
for testing :
ping -I <name of tun> <adress on that tunnel> 

tcp = https://datatracker.ietf.org/doc/html/rfc793

