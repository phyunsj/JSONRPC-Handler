///
///	@file 	myEgiForm.h
/// @brief 	Demonstrate the use of Embedded Gate Interface (EGI) 
///

//////////////////////////////// Defines ///////////////////////////////

//
//	Define the our EGI object to be called when the web form is posted.
//
class myJsonRpcEgi : public MaEgiForm {
  public:
			myJsonRpcEgi(char *egiName);
			~myJsonRpcEgi();
	void	run(MaRequest *rq, char *script, char *path, char *query, 
				char *postData, int postLen);
};



