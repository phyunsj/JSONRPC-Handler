#
#	Makefile for the simpleEgi sample + json + xmlrpc
#
#

BUILD_NATIVE	:= 0
EXPORT_OBJECTS	:= 0
NAME			:= simpleEgi

include 		make.dep

MAKE_IFLAGS		:= -I$(BLD_TOP)/appweb -I$(BLD_TOP)/http \
				   -I$(BLD_TOP)/http/modules -I$(BLD_TOP)/esp \
				   -I$(BLD_TOP)/http/modules/gaCompat \
				   -I$(BLD_TOP)/ejs -I$(BLD_TOP)/mpr \
				   -I$(BLD_TOP)/../lib/egiForm -I$(BLD_TOP)/../lib/xmlrpc/include

compileExtra: $(NAME)$(BLD_EXE)

$(NAME)$(BLD_EXE): $(BLD_LIB_DIR)/libappweb$(BLD_LIB)  \
		$(BLD_OBJ_DIR)/$(NAME)$(BLD_OBJ) 
	@bld --c++ --executable $(NAME)$(BLD_EXE) \
		--libs "appwebStatic" \
		$(BLD_OBJ_DIR)/$(NAME)$(BLD_OBJ) -legiForm -ljson \
		$(BLD_TOP)/lib/libxmlrpc_server++.a \
		$(BLD_TOP)/lib/libxmlrpc_server.a \
		$(BLD_TOP)/lib/libxmlrpc++.a \
		$(BLD_TOP)/lib/libxmlrpc_util++.a \
		$(BLD_TOP)/lib/libxmlrpc.a \
		$(BLD_TOP)/lib/libxmlrpc_xmlparse.a \
		$(BLD_TOP)/lib/libxmlrpc_xmltok.a \
		$(BLD_TOP)/lib/libxmlrpc_util.a

run:
	./$(NAME)$(BLD_EXE)

cleanExtra:
	@echo "    rm -f $(NAME)$(BLD_EXE)"
	@rm -f $(NAME)$(BLD_EXE) $(NAME)

projects:
	@MAKE_IFLAGS="-I../../../include" \
	makeProj --executable $(NAME)${BLD_EXE} --exeBaseDir "." \
		--sources "*.cpp" --libraryPath ../../../bin --libs "appwebStatic"
