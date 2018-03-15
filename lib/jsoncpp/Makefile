CXX = g++

LIB = ../libjson.so

SRCS = \
	json_reader.cpp \
	json_value.cpp \
	json_writer.cpp 

OBJS = $(SRCS:.cpp=.o)

%.o: %.cpp
	$(CXX) -O0 -g -D_DEBUG -Wall -Wno-write-strings -Wno-write-strings  -DLINUX -D_REENTRANT -fno-stack-protector -DAMD64   -fno-rtti -fPIC -DPIC  -I. -c $<

$(LIB): $(OBJS)
	$(CXX) -shared $(OBJS) -o $(LIB)

clean:
	-@$(RM) $(OBJS)
	-@$(RM) $(LIB)
