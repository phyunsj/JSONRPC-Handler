#!/usr/bin/env python

import unittest
import requests
import json
import xmlrpclib
import pexpect
import sys, getopt, pprint

IPADDR = '127.0.0.1'

def cmdOptions(argv):
    global IPADDR  
    try:
      opts, args = getopt.getopt(argv,"ht:",["target="])
    except getopt.GetoptError:
      print 'Usage : unittest-appweb.py -t <target>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print 'Usage : unittest-appweb.py -t <target> '
        sys.exit()
      elif opt in ("-t", "--target"):
        IPADDR = arg
      

class TestAppweb(unittest.TestCase):

    global IPADDR

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_jsonrpc_1(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 401, 'params': { 'first' : 18, 'second' : 13} , 'id': 1}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        self.assertEqual( jsonResponse['result'], 5)

    def test_jsonrpc_2(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 402, 'params': { 'first' : 7, 'second' : 9} , 'id': 2}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        self.assertEqual( jsonResponse['result']['first'], -2)
        self.assertEqual( jsonResponse['result']['second'], 2)
        self.assertEqual( jsonResponse['result']['third'], 4)

    def test_jsonrpc_3(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 403, 'params': { 'first' : 16, 'second' : 17, 'third' : 5} , 'id': 3}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        self.assertEqual( jsonResponse['result']['first'], -1)
        self.assertEqual( jsonResponse['result']['second'], 12)

    def test_test_jsonrpc_4(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 404, 'params': [20,41,63] , 'id': 4}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        print jsonResponse
        self.assertEqual( jsonResponse['result'][0], 19)
        self.assertEqual( jsonResponse['result'][1], 40)
        self.assertEqual( jsonResponse['result'][2], 62)

    def test_jsonrpc_5(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 405, 'params': { 'first' : [20,21,23], 'second' : [11,21,31,41,51]} , 'id': 5}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)

        self.assertEqual( jsonResponse['result']['first'][0], 19)
        self.assertEqual( jsonResponse['result']['first'][1], 20)
        self.assertEqual( jsonResponse['result']['first'][2], 22)
        self.assertEqual( jsonResponse['result']['second'][0], 9)
        self.assertEqual( jsonResponse['result']['second'][1], 19)
        self.assertEqual( jsonResponse['result']['second'][2], 29)
        self.assertEqual( jsonResponse['result']['second'][3], 39)
        self.assertEqual( jsonResponse['result']['second'][4], 49)

    def test_jsonrpc_6(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 406, 'params': { 'first' : { 'p1' : 44, 'p2' : 5, 'p3' : 110}}  , 'id': 6}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)

    def test_jsonrpc_7(self):
        
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 407, 'params': { 'first' : { 'p1' : 44, 'p2' : 5, 'p3' : 110},  'second' : { 'p1' : 33, 'p2' : 75, 'p3' : 20} }  , 'id': 7}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)

    def test_jsonrpc_parse_error(self):
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = "{ 'jsonrpc': '2.0', 'build' : '10101', 'method': '407', 'params': '[ a,b,c,d,''  , 'id': '7'}"
        r = requests.post(TargetUrl, data=payload, timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        self.assertEqual( jsonResponse['error']['code'], -32700)

    def test_jsonrpc_unknwon_method_error(self):
        TargetUrl = 'http://'+IPADDR+':8888/jsonrpc.egi'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # login as admin
        payload = { 'jsonrpc': "2.0", 'build' : 10101, 'method': 600, 'params': { 'first' : { 'p1' : 44, 'p2' : 5, 'p3' : 110},  'second' : { 'p1' : 33, 'p2' : 75, 'p3' : 20} }  , 'id': 7}
        r = requests.post(TargetUrl, data=json.dumps(payload), timeout=60, headers=self.headers, verify=False)
        print '[RESULT] HTTP Response Status :', r.status_code
        print '[RESULT] HTTP Response Header :', r.headers
        print '[RESULT] HTTP Payload         :', r.content 
        jsonResponse = json.loads(r.content)
        self.assertEqual( jsonResponse['error']['code'], -32601)



###################################################################################################
# 
#  __main__  UnitTest Runner
#
if __name__ == '__main__':

    cmdOptions(sys.argv[1:])

    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppweb)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
