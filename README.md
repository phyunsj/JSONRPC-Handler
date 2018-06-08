
# JSONRPC Handler with JSONCPP+Code Generator

JSONRPC Specification : http://www.jsonrpc.org/specification 

- Start with JSONRPC `V2.0` and made some adjustment for my need. 
- Focus on Web Application rather than typical Clinet/Server Applicaiton.
- Auto-Generated Code as much as possible. More can be done. 

## ThingsBoard IoT Platform - RPC Capabilities

#### DISCLAIMER  
6/8/2018: I am not associated with [ThingsBoard.io](https://thingsboard.io/). I simply found ThingsBoard.io while I was reviewing IoT platforms. The examples I found are quite similar to JSONRPC format.   
 

[![alt text](https://github.com/phyunsj/jsonrpc-embedded-cgi-handler/blob/master/thingsboard-IoT-jsonrpc.png)](https://thingsboard.io/docs/user-guide/rpc/ )

set-gpio-request.json
```
{
  "method": "setGpio",
  "params": {
    "pin": "23",
    "value": 1
  }
}
```

set-gpio-request.sh

```
curl -v -X POST -d @set-gpio-request.json http://localhost:8080/api/plugins/rpc/twoway/$DEVICE_ID \
--header "Content-Type:application/json" \
--header "X-Authorization: $JWT_TOKEN"
```

## JSONRPC Implementation in various formats. 

> **run::req**  --> data sent to Server

> **run::res** <-- data sent to Client

#### 1. RPC with named parameters 

##### math_subtract_1.csv 


|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|int|result|int|
|second|int||||


|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|4|result|3|
|second|1||||

>run::req[{"id": 1, "params": {"second": 13, "first": 18}, "jsonrpc": "2.0", "build": 10101, "method": 401}] size : 97

>run::res[{"id":1,"jsonrpc":"2.0","result":5,"session":"wsxaljren"}] size : 58

##### math_subtract_2.csv

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|int|first|int|
|second|int|second|int|
|||third|int|

|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|7|first|6|
|second|8|second|7|
|||third|9|

>run::req[{"id": 2, "params": {"second": 9, "first": 7}, "jsonrpc": "2.0", "build": 10101, "method": 402}] size : 95

>run::res[{"id":2,"jsonrpc":"2.0","result":{"first":-2,"second":2,"third":4},"session":"wsxaljren"}] size : 90


##### math_subtract_3.csv

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|int|first|int|
|second|int|second|int|
|third|int||||

|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|7|first|6|
|second|8|second|7|
|third|9||||

> run::req[{"id": 3, "params": {"second": 17, "third": 5, "first": 16}, "jsonrpc": "2.0", "build": 10101, "method": 403}] size : 109

> run::res[{"id":3,"jsonrpc":"2.0","result":{"first":-1,"second":12},"session":"wsxaljren"}] size : 81


#### 2. RPC with positioned parameters (Array)

##### math_subtract_4.csv

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|[3]|first|[3]|

|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|[7,9,10]|first|[6,8,9]|


> run::req[{"id": 4, "params": [20, 41, 63], "jsonrpc": "2.0", "build": 10101, "method": 404}] size : 82

> run::res[{"id":4,"jsonrpc":"2.0","result":[19,40,62],"session":"wsxaljren"}] size : 67

##### math_subtract_5.csv

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|int[3]|first|int[3]|
|second|int[5]|second|int[8]|

|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|[7,9,10]|first|[6,8,9]|
|second|[7,9,10,...]|second|[6,8,9,...]|

>run::req[{"id": 5, "params": {"second": [11, 21, 31, 41, 51], "first": [20, 21, 23]}, "jsonrpc": "2.0", "build": 10101, "method": 405}] size : 125

>run::res[{"id":5,"jsonrpc":"2.0","result":{"first":[19,20,22],"second":[9,19,29,1908443698,32506,0,0,0]},"session":"wsxaljren"}] size : 119


#### 3. RPC with dictionary (struct)

##### math_subtract_6.csv 

**dict** type is a similar to **struct** in C/C++.

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|simple_struct{} |first|simple_struct{} |


|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|{ "p1" : 2 , "p2" : 4 , "p3" : 10}|first|{ "p1" : 4 , "p2" : 5, "p3" : 6}|


**simple_struct** for math_subtract_dict example.

|PARAMETER|TYPE|
|-|-|
|p1|int|
|p2|int|
|p3|int|

>run::req[{"id": 6, "params": {"first": {"p2": 5, "p3": 110, "p1": 44}}, "jsonrpc": "2.0", "build": 10101, "method": 406}] size : 111

>run::res[{"id":6,"jsonrpc":"2.0","result":{"first":{"p1":40,"p2":1,"p3":106}},"session":"wsxaljren"}] size : 92


##### math_subtract_7.csv 

**dict** type is a similar to **struct** in C/C++.

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|first|simple_struct{} |first|simple_struct{} |
|second|simple_struct{} |second|simple_struct{} |

|INPUT|VALUE|OUTPUT|VALUE|
|-|-|-|-|
|first|{ "p1" : 2 , "p2" : 4 , "p3" : 10}|first|{ "p1" : 4 , "p2" : 5, "p3" : 6}|
|second|{ "p1" : 2 , "p2" : 4 , "p3" : 10}|second|{ "p1" : 4 , "p2" : 5, "p3" : 6}|

> run::req[{"id": 7, "params": {"second": {"p2": 75, "p3": 20, "p1": 33}, "first": {"p2": 5, "p3": 110, "p1": 44}}, "jsonrpc": "2.0", "build": 10101, "method": 407}] size : 153

> run::res[{"id":7,"jsonrpc":"2.0","result":{"first":{"p1":40,"p2":1,"p3":106},"second":{"p1":28,"p2":70,"p3":15}},"session":"wsxaljren"}] size : 127


#### Additioanl Parameters (Automatically Added)

|INPUT|TYPE|OUTPUT|TYPE|
|-|-|-|-|
|id|int|id|int|
|session|int|session|string|
|jsonrpc|string|jsonrpc | string| 
|build|int| | | |

`session`  is an unique ID allocated by the back-end. 

`build` is the release number.

`method` is an `enum` value from code-generator. (`V2.0` uses a `string` instead)

#### 4. RPC Batch

**TBD**

#### 5. RPC Error Detection

##### 5.1 Parsing Error (JSON Format Error) -32700

> run::req[{ 'jsonrpc': '2.0', 'build' : '10101', 'method': '407', 'params': '[ a,b,c,d,''  , 'id': '7'}] size : 93

> run::res[{"error":{"code":-32700,"message":"Parse error"},"id":0,"jsonrpc":"2.0","session":""}] size : 86


##### 5.2 Unknown "method" -32601

> run::req[{"id": 7, "params": {"second": {"p2": 75, "p3": 20, "p1": 33}, "first": {"p2": 5, "p3": 110, "p1": 44}}, "jsonrpc": "2.0", "build": 10101, "method": 600}] size : 153

>run::res[{"error":{"code":-32601,"message":"Method not found"},"id":7,"jsonrpc":"2.0","session":"wsxaljren"}] size : 100


## Limitations

No type checking. Support `int` and `simple struct` with 3 fields. 

## Implementation

For a simplicity reason, I use Microsoft Excel to put all examples in a single file.

- `math.xlsx` becomes Math class. Each tab becomes method definition.
- `user-defined-types.xlsx` has a `simple struct` definition.

Read .xls and generate codes as much as possible. - `generator.py`

The following packages are used :
- jsoncpp (MIT License)
- AppWeb 2 EgiHandler (Commercial or GPL)
- python 

Generated Code `sonrpc_handler.switch.include` will be called from `EgiForm::run()`. 


```
 /* ...omitted for brevity... */
 	case MATH_SUBTRACT_1 : { 
		Math math_instance;   // Math Class
		math_subtract_1_in_t math_subtract_1_input;    
		math_subtract_1_out_t math_subtract_1_output;
		Json::Value JRes;  // A temporary place for JSON response
		int index = 0;
		math_subtract_1_input.first = JsonReq["params"]["first"].asInt();
		math_subtract_1_input.second = JsonReq["params"]["second"].asInt();
		// method call
		jsonError = math_instance.subtract_1(math_subtract_1_input , math_subtract_1_output);  
		JRes["result"] = math_subtract_1_output.result;
		JsonRes["result"] = JRes["result"];  // The final place
	}
/* ...omitted for brevity... */
```

`test/unittest_jsonrpc.py` is a test script for all examples.

## Consideration

- Use *.h (type definitions, function protoypes definitiosn, etc) instead. 

