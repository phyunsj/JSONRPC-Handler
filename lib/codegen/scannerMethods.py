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

class scannerMethods(fixedLabels):

    def __init__ (self) :   	 
        self.jsonrpc_types_h           = open('../egiForm/jsonrpc_class_types.include', 'w')
        self.jsonrpc_types_c              = open('../egiForm/jsonrpc_switch_handler.include', 'w')     
        self.jsonrpc_types_h.write(self.header_cpp)
        self.jsonrpc_types_c.write(self.header_cpp)
        self.jsonrpc_counter = 400

    def close(self):
        self.jsonrpc_types_h.close()          
        self.jsonrpc_types_c.close() 

    def codegen_input_array(self, _method_name, _row_num, _param_name, _param_type, _total_param):

        array_template = '''            
        int JReq_${row_num}_count = 3;
        const Json::Value JReq_${row_num} = JsonReq["params"]["${param_name}"];
        for(index=0; index < JReq_${row_num}.size(); ++index) {
            if ( index  >= JReq_${row_num}_count ) break;
            ${method_name}_input.${param_name}[index] = JReq_${row_num}[index].asInt();
        }
''' 

        array_single_template = '''           
        int JReq_${row_num}_count = 3;
        const Json::Value JReq_${row_num} = JsonReq.get ("params",0);;
        for(index=0; index < JReq_${row_num}.size(); ++index) {
            if ( index  >= JReq_${row_num}_count ) break;
            ${method_name}_input.${param_name}[index] = JReq_${row_num}[index].asInt();
        }
'''  
        if _total_param == 1 :
            stmts = Template(array_single_template).safe_substitute(dict(method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type )) 
        else:
            stmts = Template(array_template).safe_substitute(dict(method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type )) 
         
        self.jsonrpc_types_c.write(stmts)



    def codegen_input_custom(self, _method_name, _row_num, _param_name, _param_type):

        template = '''            
        ${param_type} ${param_name}_in_${row_num};
        simple_struct_de_serialize(JsonReq["params"]["${param_name}"], ${param_name}_in_${row_num} , 0);
''' 
        stmts = Template(template).safe_substitute(dict(method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type )) 
         
        self.jsonrpc_types_c.write(stmts)



    def codegen_output_array(self, _method_name, _row_num, _param_name, _param_type, _total_param, _max_index):

        array_template = '''           
        for(index=0; index < ${max_index}; ++index) 
            JRes["${param_name}"][index] = ${method_name}_output.${param_name}[index];
''' 
        array_single_template = '''            
        for(index=0; index < ${max_index}; ++index) 
            JsonRes["result"][index] = ${method_name}_output.${param_name}[index];
'''  
        if _total_param == 1 :
            stmts = Template(array_single_template).safe_substitute(dict(method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type,  max_index = _max_index )) 
        else:
            stmts = Template(array_template).safe_substitute(dict(method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type, max_index = _max_index )) 
         
        self.jsonrpc_types_c.write(stmts)

    def codegen_output_custom(self, _class_name, _decoding,  _method_name, _row_num, _param_name, _param_type, _total_param):

        template = '''            
        ${param_type} ${param_name}_out_${row_num};
        (void) ${class_name}_instance.${decoding}_out_${row_num}(${method_name}_output , ${param_name}_out_${row_num}); 
        simple_struct_de_serialize(JRes["${param_name}"], ${param_name}_out_${row_num} , 1);
''' 
        single_template = '''            
        ${param_type} ${param_name}_out_${row_num};
        (void) ${class_name}_instance.${decoding}_out_${row_num}(${method_name}_output , ${param_name}_out_${row_num}); 
        simple_struct_de_serialize(JsonRes["result"]["${param_name}"], ${param_name}_out_${row_num} , 1);
''' 
        if _total_param == 1 :
            stmts = Template(single_template).safe_substitute(dict(class_name=_class_name.lower(), decoding = _decoding, method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type )) 
        else:
            stmts = Template(template).safe_substitute(dict(class_name=_class_name.lower(), decoding = _decoding, method_name=_method_name.lower(), \
                row_num = _row_num, param_name = _param_name, param_type = _param_type )) 

        self.jsonrpc_types_c.write(stmts)



    def codegen(self, xlsLists = []):
        for xls_name in xlsLists :
            print ".Generate '"+xls_name+ ".xlsx'"
            wb =  open_workbook('./'+xls_name+'.xlsx')

            for sheet in wb.sheets():
                print "..Scanning "+xls_name+'_'+sheet.name
                self.jsonrpc_counter = self.jsonrpc_counter + 1
                jsonrpc_command = xls_name.upper()+'_'+sheet.name
                num_rows  = sheet.nrows
                num_cells = sheet.ncols
                self.jsonrpc_types_h.write('\n#define '+jsonrpc_command.upper()+'  '+str(self.jsonrpc_counter)+'\n')
                self.jsonrpc_types_h.write('\ntypedef struct '+jsonrpc_command.lower()+'_in {')

                self.jsonrpc_types_c.write('\n\tcase '+jsonrpc_command.upper()+' : { ')
                self.jsonrpc_types_c.write('\n\t\t'+xls_name.title()+' '+xls_name+'_instance;')
                self.jsonrpc_types_c.write('\n\t\t'+jsonrpc_command.lower()+'_in_t '+jsonrpc_command.lower()+'_input;')
                self.jsonrpc_types_c.write('\n\t\t'+jsonrpc_command.lower()+'_out_t '+jsonrpc_command.lower()+'_output;') 
                self.jsonrpc_types_c.write('\n\t\tJson::Value JRes;\n\t\tint index = 0;') 

                #### INPUT
                num_of_params = 0
                curr_row = 0
                while curr_row < num_rows:
                    param_name = sheet.cell_value(curr_row, 0).encode("utf-8")
                    param_type = sheet.cell_value(curr_row, 1).encode("utf-8")
                    curr_row = curr_row + 1
                    #print param_name                   
                    if param_name:
                        num_of_params = num_of_params + 1
                #print num_of_params
                curr_row = 0
                while curr_row < num_rows:
                    param_name = sheet.cell_value(curr_row, 0).encode("utf-8")
                    param_type = sheet.cell_value(curr_row, 1).encode("utf-8")
                    curr_row = curr_row + 1
                    #print param_name                   
                    if param_name:
                        # array
                        if param_type.endswith(']') :
                           indexNum =  re.findall("\d+", param_type)[0]
                           self.jsonrpc_types_h.write('\n\tint  '+param_name+'['+str(indexNum)+'];')
                           self.codegen_input_array(jsonrpc_command, curr_row, param_name, param_type, num_of_params)

                        # user-defined struct. one-level.
                        elif param_type.endswith('}') :
                           param_type = param_type.replace('{}','')
                           self.jsonrpc_types_h.write('\n\t'+param_type +'  '+param_name+';')
                           self.codegen_input_custom(jsonrpc_command, curr_row, param_name, param_type)
                           self.jsonrpc_types_c.write('\n\t\t(void) '+xls_name.lower()+'_instance.'+sheet.name.lower()+'_in_'+str(curr_row)+'('+ jsonrpc_command.lower()+'_input , '+param_name+'_in_'+str(curr_row)+');')
                
                         # simple types. only "int" for now.
                        else:
                           self.jsonrpc_types_h.write('\n\t'+param_type +'  '+param_name+';')
                           self.jsonrpc_types_c.write('\n\t\t'+jsonrpc_command.lower()+'_input.'+param_name+' = JsonReq["params"]["'+param_name+'"].asInt();')

                self.jsonrpc_types_h.write('\n} '+jsonrpc_command.lower()+'_in_t;\n')

                ### <Class_instance>.<Method> ( input, output )
                self.jsonrpc_types_c.write('\n\t\tjsonError = '+xls_name.lower()+'_instance.'+sheet.name.lower()+'('+ jsonrpc_command.lower()+'_input , '+jsonrpc_command.lower()+'_output);')
                
                ### OUTPUT
                self.jsonrpc_types_h.write('\ntypedef struct '+jsonrpc_command.lower()+'_out {')
                num_of_params = 0
                curr_row = 0
                while curr_row < num_rows:
                    param_name = sheet.cell_value(curr_row, 2).encode("utf-8")
                    param_type = sheet.cell_value(curr_row, 3).encode("utf-8")
                    curr_row = curr_row + 1
                    #print param_name                   
                    if param_name:
                       num_of_params = num_of_params + 1
                #print num_of_params

                curr_row = 0
                while curr_row < num_rows:
                    param_name = sheet.cell_value(curr_row, 2).encode("utf-8")
                    param_type = sheet.cell_value(curr_row, 3).encode("utf-8")
                    curr_row = curr_row + 1
                    #print param_name                   
                    if param_name:
                        if param_type.endswith(']') :
                            indexNum =  re.findall("\d+", param_type)[0]
                            self.jsonrpc_types_h.write('\n\tint  '+param_name+'['+str(indexNum)+'];')
                            self.codegen_output_array(jsonrpc_command, curr_row, param_name, param_type, num_of_params, indexNum)

                        elif param_type.endswith('}') :
                            param_type = param_type.replace('{}','')
                            self.jsonrpc_types_h.write('\n\t'+param_type +'  '+param_name+';')
                            self.codegen_output_custom( xls_name.lower(), sheet.name.lower(),  jsonrpc_command, curr_row, param_name, param_type, num_of_params)

                        else:
                            self.jsonrpc_types_h.write('\n\t'+param_type +'  '+param_name+';')
                            self.jsonrpc_types_c.write('\n\t\tJRes["'+param_name+'"] = '+jsonrpc_command.lower()+'_output.'+param_name+';')
                            if num_of_params == 1 :
                                self.jsonrpc_types_c.write('\n\t\tJsonRes["result"] = JRes["'+ param_name  +'"];');
                if num_of_params != 1 : 
                    self.jsonrpc_types_c.write('\n\t\tJsonRes["result"] = JRes;')
                self.jsonrpc_types_h.write('\n} '+jsonrpc_command.lower()+'_out_t;\n')
                self.jsonrpc_types_c.write('\n\t}\n\tbreak;')
                