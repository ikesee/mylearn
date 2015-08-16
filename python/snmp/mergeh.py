import os
import sys
import glob
def merge(fdir,outfile):
	file_list = glob.glob(fdir+'*.h')
	file_to_write = file(outfile,'w')
	file_to_write.write('''/*
*@File snmpIVPMB.h
*@bief
*2015-05-29
*change list:
*-----------
*2015-05-27,iks  create it
*
*/

#ifndef SNMPIVPMB_H
#define SNMPIVPMB_H

void    init_snmpIVPMB(void);

''')
	for f in file_list:
		file_to_read = file(str(f),'r')
		list_line = file_to_read.readlines()
		file_to_write.write(list_line[11])
		file_to_read.close()
	file_to_write.write("\n#endif")
	file_to_write.close()

if __name__ == '__main__':
	merge('../snmp/include_0603/','snmpIVPMB.h')
