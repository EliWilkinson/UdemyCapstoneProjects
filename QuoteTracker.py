import argparse
import sys
import time
import urllib.request

from xml.etree.ElementTree import parse, fromstring

def check_negative(value):
	errMsg = "Interval {} is an invalid positive int value".format(value)
	try:
		retValue= int(value)
	except:
		raise argparse.ArgumentTypeError(errMsg)

	if retValue < 0:
		raiseargparse.ArgumentTypeError(errMsg)

	return retValue


def getStockValue(symbol):
	url = "http://dev.markitondemand.com/Api/v2/Quote/xml?symbol={}".format(symbol)
	headers= {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5'; 'Windows NT'}
	try:
		req= urllib.request.Request(url, None, headers)
		data= urllib.request.urlopen(req)
		xmlRoot = fromstring(data.read())

		if xmlRoot.tag != "StockQuote":
			print("Company {} not found".format(symbol))
			return None

		xmlDict = {child.tag:child.text for child in xmlRoot}

		if xmlDict.get('Status') is None:
			print("Corrupted Data")
			return None
		elif xmlDict.get('Status') != 'SUCCESS':
			print("Corrupted Data")
			return None

		if xmlDict.get('LastPrice') is None or xmlDict.get('Name') is None:
			print("Corrupted Data")
			return None

		else:
			return [xmlDict.get('Name'), float(xmlDict.get('LastPrice'))]

		except:
			print("Corrupted Data")
			return None








