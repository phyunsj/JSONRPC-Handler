///
///	@file 	simpleEgi.cpp
/// @brief 	Demonstrate the use of Embedded Server Pages (EGI) in a 
///			simple multi-threaded application.
///
////////////////////////////////////////////////////////////////////////////
//
//	Copyright (c) Embedthis Software LLC, 2003-2009. All Rights Reserved.
//	The latest version of this code is available at http://www.mbedthis.com
//
//	This software is open source; you can redistribute it and/or modify it 
//	under the terms of the GNU General Public License as published by the 
//	Free Software Foundation; either version 2 of the License, or (at your 
//	option) any later version.
//
//	This program is distributed WITHOUT ANY WARRANTY; without even the 
//	implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
//	See the GNU General Public License for more details at:
//	http://www.mbedthis.com/downloads/gplLicense.html
//	
//	This General Public License does NOT permit incorporating this software 
//	into proprietary programs. If you are unable to comply with the GPL, a 
//	commercial license for this software and support services are available
//	from Embedthis Software at http://www.mbedthis.com
//
/////////////////////////////// Includes ///////////////////////////////

#include	"appweb/appweb.h"

#ifdef BLD_FEATURE_EGI_MODULE 

//#include    "xmlrpc-c/base.hpp"
//#include    "xmlrpc-c/registry.hpp"

#include    "myEgiForm.h"

/////////////////////////////////// Code ///////////////////////////////

int main(int argc, char** argv)
{
	MaHttp		*http;					// Http service inside our app
	MaServer	*server;				// For the HTTP server
	Mpr			mpr("simpleEgi");		// Initialize the run time

#if BLD_FEATURE_LOG
	//
	//	Do the following two statements only if you want debug trace
	//
	mpr.addListener(new MprLogToFile());
	mpr.setLogSpec("stdout:4");
#endif

	//
	//	Start the Embedthis Portable Runtime
	//
	mpr.start(0);

	//
	//	Create Http and Server objects for this application. We set the
	//	ServerName to be "default" and the initial serverRoot to be ".".
	//	This will be overridden in simpleEgi.conf.
	//
	http = new MaHttp();
	server = new MaServer(http, "default", ".");
	
	//
	//	Activate the copy module and handler
	//
	new MaCopyModule(0);
	new MaEgiModule(0);

	//
	//	Configure the server with the configuration directive file
	//
	if (server->configure("simpleEgi.conf") < 0) {
		mprFprintf(MPR_STDERR, 
			"Can't configure the server. Error on line %d\n", 
			server->getLine());
		exit(2);
	}

	//
	//	Define our EGI procedures
	//
	new myJsonRpcEgi("/jsonrpc.egi");
    //new myXmlRpcEgi("/xmlrpc.egi");
	//
	//	Start the server
	//
	if (http->start() < 0) {
		mprFprintf(MPR_STDERR, "Can't start the server\n");
		exit(2);
	}

	//
	//	Tell the MPR to loop servicing incoming requests. We can 
	//	replace this call with a variety of event servicing 
	//	mechanisms offered by AppWeb.
	//
	mpr.serviceEvents(0, -1);

	//
	//	Orderly shutdown
	//
	http->stop();
	delete server;
	delete http;

	//
	//	MPR run-time will automatically stop and be cleaned up
	//
	return 0;
}

////////////////////////////////////////////////////////////////////////
#else
int main()
{
	fprintf(stderr, "BLD_FEATURE_EGI_MODULE is not defined in config.h\n");
	exit(2);
}
#endif /* BLD_FEATURE_EGI_MODULE */


