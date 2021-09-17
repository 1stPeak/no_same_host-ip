# no_same_host-ip
用途：测试主机与IP是否一致

optional arguments:
  -h, --help            show this help message and exit

  -u URL, --url URL     请输入url或ip,例如：https://www.example.com或222.222.222.222

  -f FILE, --file FILE  请在urls.txt中添加需要扫描的目标域名或IP

存在漏洞的URL保存在vulnerable_urls.txt中

不存在漏洞的URL保存在security_urls.txt中

环境：python3.x

依赖库：urllib、urlparse、argparse、socket、requests、re

Tips：不保证完全正确 仅供参考思路
