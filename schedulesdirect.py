#!/usr/bin/python
import hashlib, json, os, requests, sys

class SchedulesDirect:
	#BASE_URL = 'https://json.schedulesdirect.org/20131021'
	BASE_URL = 'https://json.schedulesdirect.org/20140530'

	def __init__(self):
		self.headers = {'User-agent': 'schedulesdirect.py'}
	
	def get_randhash(self,username,password):
		del self.headers['token']
		passhash = hashlib.sha1(password.encode('utf-8')).hexdigest()
		data = json.dumps({"password":passhash,"username":username})
		resp = requests.post(SchedulesDirect.BASE_URL+"/token",headers=self.headers,data=data).json()
		if not resp['code']:
			self.headers['token'] = resp['token']
		return resp
	
	def _get(self,path):
		return requests.get(SchedulesDirect.BASE_URL+"/"+path,headers=self.headers).json()
	
	def _put(self,path):
		return requests.put(SchedulesDirect.BASE_URL+"/"+path,headers=self.headers).json()
	
	def _post(self,path,request=None):
		data = ""
		if request:
			data = json.dumps({'request':request})
		return requests.post(SchedulesDirect.BASE_URL+"/"+path,headers=self.headers,data=data)
	
	def get_status(self):
		return self._get('status')
	
	def get_lineups(self):
		return self._get('lineups')
	
	def get_schedules(self,stationIDs):
		return self._post('schedules',stationIDs)
	
	def get_programs(self,programIDs):
		return self._post('programs',programIDs)

