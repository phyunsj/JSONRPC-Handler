#!/usr/bin/env python
from xlrd import open_workbook
from string import Template
import sys, pprint, os
import re
import time
import shutil

# Add the directory containing your module to the Python path (wants absolute paths)
scriptpath = "./fixedLabels.py"
sys.path.append(os.path.abspath(scriptpath))
from fixedLabels import *

class scannerTypes(fixedLabels):

    def __init__ (self) :
    	self.jsonrpc_types_h              = open('../egiForm/jsonrpc_user_defined_types.h', 'w')  
        self.jsonrpc_types_c              = open('../egiForm/jsonrpc_user_defined_types.include', 'w')     
        self.jsonrpc_types_h.write(self.header_cpp)
        self.jsonrpc_types_c.write(self.header_cpp)

    def close(self):
        self.jsonrpc_types_h.close()          
        self.jsonrpc_types_c.close() 

    def codegen(self, xlsLists = []):
        for xls_name in xlsLists :
            print ".Generate '"+xls_name+ ".xlsx'"
            wb =  open_workbook('./'+xls_name+'.xlsx')

            for sheet in wb.sheets():
                print "..Scanning "+sheet.name
                num_rows  = sheet.nrows
                num_cells = sheet.ncols
                self.jsonrpc_types_h.write('\ntypedef struct '+sheet.name+' {')
                self.jsonrpc_types_c.write('\nvoid '+sheet.name+'_de_serialize( Json::Value &JsonP, '+ sheet.name+'_t &'+ sheet.name +'_p,  int direction /* 0: json -> struct, 1: struct -> json */ ) \n{')
                curr_row = 0
                while curr_row < num_rows:
                   param_name = sheet.cell_value(curr_row, 0).encode("utf-8")
                   param_type = sheet.cell_value(curr_row, 1).encode("utf-8")
                   curr_row = curr_row + 1
                   #print param_name, param_type
                   self.jsonrpc_types_h.write('\n\t'+param_type +'  '+param_name+';')
                   self.jsonrpc_types_c.write('\n\tif (direction) JsonP["'+param_name+'"] = '+sheet.name+'_p.'+param_name+';')
                   self.jsonrpc_types_c.write('\n\telse  '+sheet.name+'_p.'+param_name+' = JsonP["'+param_name+'"].asInt();')
                self.jsonrpc_types_h.write('\n} '+sheet.name+'_t;\n')
                self.jsonrpc_types_c.write('\n\treturn;\n}\n')