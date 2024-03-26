# flask-inventory Makefile

PROJPATH = $(PWD)
PROJNAME = $(notdir ${PROJPATH})
REMOTEDIR = ${PROJNAME}

MK = ./mk

include $(MK)/*.mk

