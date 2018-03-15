#include     "jsonrpc_user_defined_types.h"
#include     "jsonrpc_class_types.include"
#include     "Math.h"

Math::Math() {}
Math::~Math() {}
int Math::subtract_1(math_subtract_1_in_t &input , math_subtract_1_out_t &output) 
{
	output.result = input.first - input.second;
    return 0;
}
int Math::subtract_2(math_subtract_2_in_t &input , math_subtract_2_out_t &output) 
{
    output.first = input.first - input.second;
    output.second = input.second - input.first;
    output.third = output.second - output.first;
    return 0;
}
int Math::subtract_3(math_subtract_3_in_t &input , math_subtract_3_out_t &output) 
{
    output.first = input.first - input.second;
    output.second = input.second - input.third;
    return 0;
}
int Math::subtract_4(math_subtract_4_in_t &input , math_subtract_4_out_t &output) 
{
	output.first[0] = input.first[0] - 1;
	output.first[1] = input.first[1] - 1;
	output.first[2] = input.first[2] - 1;
    return 0;
}
int Math::subtract_5(math_subtract_5_in_t &input , math_subtract_5_out_t &output) 
{
    output.first[0] = input.first[0] - 1;
	output.first[1] = input.first[1] - 1;
	output.first[2] = input.first[2] - 1;
	output.second[0] = input.second[0] - 2;
	output.second[1] = input.second[1] - 2;
	output.second[2] = input.second[2] - 2;
	output.second[3] = input.second[3] - 2;
	output.second[4] = input.second[4] - 2;
    output.second[5] = 0;
    output.second[6] = 0;
    output.second[7] = 0;
    return 0;
}
int Math::subtract_6(math_subtract_6_in_t &input , math_subtract_6_out_t &output) 
{
	output.first.p1 = input.first.p1 - 4;
	output.first.p2 = input.first.p2 - 4;
    output.first.p3 = input.first.p3 - 4;
    return 0;
}
void Math::subtract_6_in_1(math_subtract_6_in_t &input , simple_struct_t &from) 
{
    input.first.p1 = from.p1 ;
    input.first.p2 = from.p2;
    input.first.p3 = from.p3;
    return;
}
void Math::subtract_6_out_1(math_subtract_6_out_t &output , simple_struct_t &to) 
{
    to.p1 = output.first.p1;
    to.p2 = output.first.p2;
    to.p3 = output.first.p3;
    return;
}

int Math::subtract_7(math_subtract_7_in_t &input , math_subtract_7_out_t &output) 
{
    output.first.p1 = input.first.p1 - 4;
	output.first.p2 = input.first.p2 - 4;
    output.first.p3 = input.first.p3 - 4;
    output.second.p1 = input.second.p1 - 5;
	output.second.p2 = input.second.p2 - 5;
    output.second.p3 = input.second.p3 - 5;
    return 0;
}

void Math::subtract_7_in_1(math_subtract_7_in_t &input , simple_struct_t &from) 
{
    input.first.p1  = from.p1;
    input.first.p2  = from.p2;
    input.first.p3  = from.p3;
    return;
}
void Math::subtract_7_in_2(math_subtract_7_in_t &input , simple_struct_t &from) 
{
    input.second.p1 = from.p1;
    input.second.p2 = from.p2;
    input.second.p3 = from.p3;
    return;
}

void Math::subtract_7_out_1(math_subtract_7_out_t &output , simple_struct_t &to ) 
{
    to.p1 = output.first.p1;
    to.p2 = output.first.p2;
    to.p3 = output.first.p3;
    return;
}


void Math::subtract_7_out_2(math_subtract_7_out_t &output , simple_struct_t &to ) 
{
    to.p1 = output.second.p1;
    to.p2 = output.second.p2;
    to.p3 = output.second.p3;
    return;
}