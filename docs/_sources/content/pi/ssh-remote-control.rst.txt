SSH Remote Control
##################

.. include:: ../../references.inc

As part of my research work, I maintain several small clusters. 

.. csv-table:: Cluster Systems
   :header: "Processor", "Num", "Cores"
   :widths: 15, 15, 15

   "Intel-I5", 4, 8
   "Pi 3", 4, 16
   "Pi 4", 7, 14
   "Pi 5", 4, 20

I have a 4-processor cluster using Intel *NUC* computers, a 4-processor system
on using Raspberry Pi 3 machines, another 7-processor Raspberry Pi 4 system, and
a 4-processor Raspberry Pi 5 system.  All of these clusters run some form of
Linux. I have all set up for SSH access with no password required. My intent is
to use these clusters as test beds, to experiment with parallel processing
techniques.  Logging in to a console on each machine using *SSH* is simple
enough, but repeatedly login in and running commands on a bunch of machines is
painful. I do use the *Ansible* tool to manage basic configurations on all of
these machines, which significantly improves my life.

Developing for a cluster
========================

In most cases the code that runs on a cluster is written in some high level
language like *C++* or modern *Fortran*. I use a *MacBook Air* as my primary
laptop, and it is all set up to produce documents (like this one) and build |PY|
applications. My goal is to use |PY| to create a simple automation technique
that lets me send a list of commands to one or more machines and collect the
console output for display on my management laptop. That output will be included
in my documentation using the *Sphine* **programoutput** extension. 

The inspiration for this experiment is *Ansible*, but I want to have more
control over the command sequence and the collection of output from a remote
task.

Time to improve the process.

Test Setup
==========

I have a simple Raspberry Pi 3 running on the top of my office bookcase. That
machine has been running for over a year and can be accessed using a *Wifi*
connection.

In this example, I have set up an alias for the machine (mine is **picam**) that
dets up the remote machine **IP** address. I have also added my *SSH* public key
to the **known_hosts** list on the *Pi*. This allows  logging in with no
password.

Once all of this has been set up, this should work:

.. command-output:: ssh picam 'uptime'

*SSH* supports running commands from a text file. Here is an example command
file:

.. command-output:: cat ex2.txt

The normal *SSH* command to run this locally is:

.. code-block:: shell

   ssh picam < commands.txt

Unfortunately, the *Sphinx* extension I use to include program output in my
documents cannot handle file redirection like this. We could transfer the
command file to the *Pi* and run it there but we would miss the individual
command output results. A solution (maybe not the best) is to create a simple
local |PY| program that reads our command file and runs the *SSH* commands for
us. (|PY| is great for creating simple automation tasks like this (see
:cite:t:`Weigart:2015`).

Here is a basic |PY| snippet using this approach:

.. literalinclude::  ../../code/ex3.py
   :language: python
   :linenos:

And here is the program output:

.. command-output:: python code/ex3.py

This works! We now need to wrap this up in a loop that reads a line from the
command file and creates the list of command parts. |PY| is up to this job!

.. literalinclude::  ../../code/ex1.txt
   :language: python
   :linenos:

.. command-output::  python code/ex4.py code/ex1.txt

Generating this code was not too difficult, considering the need to read the
command line, make sure the lines were not blank, then creating a list of final
command parts to be proceeded by the **subprocess.run** code.

However, the output displayed here does not currently match what I see when
running this code locally. It appears that output buffering by the *Sphinx*
extension is not dealing with this well. A solution is to generate the output
lines in the |PY| code and dump that output at the end of the code.

.. literalinclude::  ../../code/ex1.txt
   :language: python
   :linenos:

