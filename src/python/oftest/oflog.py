# @author Jonathan Stout
from subprocess import Popen, PIPE
import json
import logging
import os
import time
from oftest import config

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, "wb")

"""
oflog.py
Provides Loggers for oftest cases, and easy to use wireshark
logging.
 
Test case writers use three main functions.
1. get_logger() - Returns a Logger for each testcase or the
default logger if --publish is not passed.
2. start_logging(testcase) - Starts tshark on each test interface,
and the controller interface if -H is passed on the CLI. Additionally
registers tshark pids to testcase for process clean up.
"""
 
pubName = ""

def create_log_directory(log_directory):
    """Deletes directory, (if already exists) and then recreates
    directory.
    """
    try:
        Popen(["rm", "-rf", log_directory],stdout=None)
        time.sleep(1)
    except:
        pass
    finally:
        os.makedirs(log_directory)

def start_wireshark_cap(log_directory):
    process_ids = []
    interfaces = config["port_map"].values()
    interfaces.append(find_interface(config["controller_host"]))

    for iface in interfaces:
        fd = log_directory + "{0}.pcap".format(iface)
        pid = Popen(["tshark", "-i", str(iface), "-w", fd, "-q"],
                    stdout=DEVNULL, stderr=DEVNULL)
        process_ids.append(pid)
    time.sleep(1)
    return process_ids

def stop_wireshark_cap(process_ids):
    for pid in process_ids:
        pid.terminate()
    time.sleep(1)

def start_logging(testcase):
    """Start wireshark captures for each network interface."""
    if not config["publish"]: return

    _group, _test = testcase.__class__.__name__[3:].split("No")
    global pubName
    pubName = "Grp{0}No{1}".format(_group, _test)
    directory = "./src/python/ofreport/logs/Grp{0}No{1}/"
    log_directory = directory.format(_group, _test)
    create_log_directory(log_directory)

    process_ids = start_wireshark_cap(log_directory)
    testcase.addCleanup(stop_logging, process_ids)

def stop_logging(process_ids):
    """Stop wireshark captures for each network interface."""
    if not config["publish"]: return
    stop_wireshark_cap(process_ids)

def get_logger():
    """Configure logging for each test case.
    """
    if not config["publish"]:
        return logging
    LOG = logging.getLogger(pubName)
    LOG.setLevel(logging.DEBUG)
    logDir = "%slogs/%s" % ("./src/python/ofreport/", pubName)
    h = logging.FileHandler(logDir+"/testcase.log")
    h.setLevel(logging.DEBUG)
    
    f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    h.setFormatter(f)
    LOG.addHandler(h)
    return LOG

def find_interface(ip="127.0.0.1"):
    """
    Parses ifconfig to return the interface associated with ip.
    """
    p = Popen(["ifconfig | grep 'Link\|inet\|mtu'"], shell=True, stdout=PIPE)
    data = p.communicate()[0]
    data = data.split("\n")[:-1]
    interface = None

    for line in data:
        a = line.strip(" \t").split(" ")
        # Note the interface
        if "Link" in a or "mtu" in a:
            interface = a[0].strip(":")
        # Find the right IP
        if a[0] == "inet" and a[1].strip("addr:") == ip:
            return interface
