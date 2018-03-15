
class Math {
public:
	Math();
	~Math();
    
    int subtract_1(math_subtract_1_in_t& , math_subtract_1_out_t&);
    int subtract_2(math_subtract_2_in_t& , math_subtract_2_out_t&);
    int subtract_3(math_subtract_3_in_t& , math_subtract_3_out_t&);
    int subtract_4(math_subtract_4_in_t& , math_subtract_4_out_t&);
    int subtract_5(math_subtract_5_in_t& , math_subtract_5_out_t&);
    int subtract_6(math_subtract_6_in_t& , math_subtract_6_out_t&);
    int subtract_7(math_subtract_7_in_t& , math_subtract_7_out_t&);

    // encoding/decoding - might be better to be auto-generated.
    void subtract_6_in_1(math_subtract_6_in_t &input , simple_struct_t &from);
    void subtract_6_out_1(math_subtract_6_out_t &output , simple_struct_t &to);
    void subtract_7_in_1(math_subtract_7_in_t &input , simple_struct_t &from);
    void subtract_7_in_2(math_subtract_7_in_t &input , simple_struct_t &from);
    void subtract_7_out_1(math_subtract_7_out_t &output , simple_struct_t &to);
    void subtract_7_out_2(math_subtract_7_out_t &output , simple_struct_t &to);
};