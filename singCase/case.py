#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:29:34 2021

@author: longhuadmin
"""
import  time
def asd():
    Asin= {'data': [{'projectName': '江南天街', 'projectId': '251402', 'subProjectStatus': '执行中', 'subProjectId': '251403', 'subProjectCode': 'XM2109201', 'subProjectName': '江南天街2', 'tpo': '李*', 'sdm': '王*', 'developType': '1', 'currentMilestone': '启动会', 'currentMilestoneName': '启动会', 'currentMilestoneId': 'd3b9fb63783f45e686b0cb0c5587ca9a', 'milestoneTime': '2021-05-28', 'healthyStatus': '2', 'rdCenterName': '商业业务数字科技中心', 'rdCenterNameSort': 'SHANGYEYEWUSHUZIKEJIZHONGXIN', 'projectBenchmarking': True, 'rdCenter': '1000000073', 'benchmarking': True}], 'code': 10000, 'msg': '成功', 'curTime': '2021-06-17 17:20:20', 'totalCount': 1, 'pageInfo': {'pageNum': 1, 'pageSize': 30, 'direction': None, 'lastIndex': None}}
    data = Asin.get('data')
    print(data[0].get('projectId'))


def time2():
     time2 =time.strftime('H%M%S',time.localtime(time.time()))
     return time2
if __name__ == '__main__':
     
    print(time2())