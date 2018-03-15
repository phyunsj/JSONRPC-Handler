///
///	@file 	myEgiForm.cpp
/// @brief 	Demonstrate the use of Embedded Gate Interface (EGI) 
///

#include    "appweb/appweb.h"
//#include    "egiHandler.h"

#include    "include/json.h"

#include    "myEgiForm.h"

#include     "jsonrpc_user_defined_types.h"
#include     "jsonrpc_class_types.include"

#include     "jsonrpc_user_defined_types.include"

#include     "Math.h"
//
////////////////////////////////////////////////////////////////////////

myJsonRpcEgi::myJsonRpcEgi(char *name) : MaEgiForm(name)
{
    //  Put required initialization (if any) here
}

////////////////////////////////////////////////////////////////////////

myJsonRpcEgi::~myJsonRpcEgi()
{
    //  Put cleanup here
}

////////////////////////////////////////////////////////////////////////
//
//  Method that is run when the EGI form is called from the web
//  page. Rq is the request context. URI is the bare URL minus query.
//  Query is the string after a "?" in the URL. Post data is posted
//  HTTP form data.
//

void myJsonRpcEgi::run(MaRequest *rq, char *script, char *uri, char *query, 
    char *postData, int postLen)
{

#if TEST_MULTI_THREADED_ACCESS
    mprPrintf("In myJsonRpcEgi::run, thread %s\n", mprGetCurrentThreadName());
#else
    mprPrintf("In myJsonRpcEgi::run, single threaded\n");
#endif
    std::cout << "run::req[" << postData << "] size : " << postLen << std::endl;

    Json::Value      JsonReq;
    Json::Reader     JsonReader;
    Json::Value      JsonRes;
    Json::FastWriter JsonWriter;
    std::string      postResponse;
    int jsonError      = 0;
    int jsonrpc_id     = 0;
    int jsonrpc_method = 0;
    int jsonrpc_buildnumber = 0; /* AABBCC AA: Major, BB: Minor, CC: Patch*/
    std::string session;
    jsonError = JsonReader.parse( postData, JsonReq );
    if ( !jsonError )
    {
        /* {"code": -32700, "message": "Parse error"} */
        JsonRes["error"]["code"] = -32700;
        JsonRes["error"]["message"] = "Parse error";

    } else {
    
    /* session management */
    session = JsonReq.get("session", "wsxaljren" ).asString();
    /* ...do something with session. omitted... */
    /* id counter management */
    jsonrpc_id = JsonReq.get("id", 0 ).asInt();
    /* ...do something with id. omitted... */
    /* jsonrpc version check */
    /* ...do something with version. omitted... */
    jsonrpc_buildnumber = JsonReq.get("build", 0 ).asInt();
    /* ...do something with buildnumber. omitted... */ 

    jsonrpc_method = JsonReq.get("method", 0 ).asInt();
    switch( jsonrpc_method ) {
#include "jsonrpc_switch_handler.include" // Auto-Generated switch body 
    default :
        /* {"code": -32601, "message": "Method not found"} */
        JsonRes["error"]["code"] = -32601;
        JsonRes["error"]["message"] = "Method not found";
    }
  
  }
  JsonRes["id"] = jsonrpc_id++;
  JsonRes["session"] = session;
  JsonRes["jsonrpc"] = "2.0";
  postResponse = JsonWriter.write(JsonRes);
  rq->writeFmt("%s", postResponse.c_str());
  std::cout << "run::res[" << postResponse << "] size : " << postResponse.length() << std::endl;
  return;
}

