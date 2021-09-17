# -*- coding:utf-8 -*-
"""
# 日期: 2021/09/17 15:30
# 作者：1stPeak
# 版本：V1.0
# 用途：测试主机与IP是否一致
"""
from urllib.parse import urlparse
import argparse
import socket
import requests
import re

def args_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help = "请输入url或ip,例如：https://www.example.com或222.222.222.222")
    parser.add_argument("-f", "--file", help = "请在urls.txt中添加需要扫描的目标域名或IP")
    args = parser.parse_args()
    return args

def host_ip():
    hostname = urlparse(ars_url.url).hostname
    hostname = socket.getaddrinfo(hostname, None)
    global result1
    #print(hostname)
    result1 = hostname[0][4][0]
    #print(result1)

def url_ip():
    bodyip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", ars_url.url)  # 提取ip
    # print(body_ip)
    if bodyip != []:
        bodyip = ''.join(bodyip)
        #print(bodyip)
        if bodyip == result1:
            print("[+]" + ars_url.url + " 主机和IP一致")
            with open('security_urls.txt', 'a') as f:
                f.write(ars_url.url + '\n')
        else:
            print("[+][+]" + ars_url.url + " 主机和IP不一致")
            with open('vulnerable_urls.txt', 'a') as f:
                f.write(ars_url.url + '\n')

    else:
        body = urlparse(ars_url.url).netloc  # 获取URL域名或IP
        body_ip = socket.getaddrinfo(body, None)  # 域名或ip转ip
        body_ip = body_ip[0][4][0]
        #print(body_ip)
        if body_ip == result1:
            print("[+]" + ars_url.url + " 主机和IP一致")
            with open('security_urls.txt', 'a') as f:
                f.write(ars_url.url + '\n')
        else:
            print("[+][+]" + ars_url.url + " 主机和IP不一致")
            with open('vulnerable_urls.txt', 'a') as f:
                f.write(ars_url.url + '\n')

if __name__ == '__main__':
    print("********主机与IP是否一致判断工具V1.0********[Author:1stPeak]")
    #url = 'https://www.baidu.com/xxx'
    ars_url=args_url()
    if ars_url.url:
        try:
            r = requests.get(ars_url.url,timeout=5)
            host_ip()
            url_ip()
        except:
            print("[-]" + ars_url.url + " 目标不可达")
    if ars_url.file:
        fopen = open("urls.txt", 'r')
        lines = fopen.readlines()
        for ars_url.url in lines:
            ars_url.url = ars_url.url.strip()
            #print(ars_url.url)
            try:
                r = requests.get(ars_url.url,timeout=5)
                host_ip()
                url_ip()
            except:
                print("[-]" + ars_url.url + " 目标不可达")