############################################################################
#
#   Find_Trusted_Proxies.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import requests
#
#
class RequestData():
    #
    def __init__(self):
        #
        self.input_type = 'GET'
        self.input_url = ''
        self.input_params = None
        self.input_form = None
        self.input_json = None
        self.input_proxies = None
        self.input_headers = None
        self.input_timeout = 1
        #
        self.result_error = False
        self.result_error_proxy = False
        self.result_error_timeout = False
        self.result_error_required_url = False
        self.result_error_invalid_url = False
        self.result_code = 0
        self.result_header = ''
        self.result_body = ''
        self.result_cookies = ''
#
#
def url_function(data:RequestData):
    #
    res = None
    #
    if data.input_type == 'GET':
            try:
                res = requests.get(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json, timeout=data.input_timeout )
            except requests.exceptions.Timeout:
                data.result_error_timeout = True
                data.result_error = True
            except requests.exceptions.ProxyError:
                data.result_error_proxy = True
                data.result_error = True
            except requests.exceptions.URLRequired:
                data.result_error_required_url = True
                data.result_error = True
            except requests.exceptions.InvalidURL:
                data.result_error_invalid_url = True
                data.result_error = True
            except:
                data.result_error = True
    #
    elif data.input_type == 'POST':
        try:
            res = requests.post(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json,
                               timeout=data.input_timeout)
        except requests.exceptions.Timeout:
            data.result_error_timeout = True
            data.result_error = True
        except requests.exceptions.ProxyError:
            data.result_error_proxy = True
            data.result_error = True
        except requests.exceptions.URLRequired:
            data.result_error_required_url = True
            data.result_error = True
        except requests.exceptions.InvalidURL:
            data.result_error_invalid_url = True
            data.result_error = True
        except:
            data.result_error = False
    #
    elif data.input_type == 'PUT':
        try:
            res = requests.put(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json,
                               timeout=data.input_timeout)
        except requests.exceptions.Timeout:
            data.result_error_timeout = True
            data.result_error = True
        except requests.exceptions.ProxyError:
            data.result_error_proxy = True
            data.result_error = True
        except requests.exceptions.URLRequired:
            data.result_error_required_url = True
            data.result_error = True
        except requests.exceptions.InvalidURL:
            data.result_error_invalid_url = True
            data.result_error = True
        except:
            data.result_error = False
    #
    elif data.input_type == 'DELETE':
        try:
            res = requests.delete(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json,
                               timeout=data.input_timeout)
        except requests.exceptions.Timeout:
            data.result_error_timeout = True
            data.result_error = True
        except requests.exceptions.ProxyError:
            data.result_error_proxy = True
            data.result_error = True
        except requests.exceptions.URLRequired:
            data.result_error_required_url = True
            data.result_error = True
        except requests.exceptions.InvalidURL:
            data.result_error_invalid_url = True
            data.result_error = True
        except:
            data.result_error = False
    #
    elif data.input_type == 'HEAD':
        try:
            res = requests.head(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json,
                               timeout=data.input_timeout)
        except requests.exceptions.Timeout:
            data.result_error_timeout = True
            data.result_error = True
        except requests.exceptions.ProxyError:
            data.result_error_proxy = True
            data.result_error = True
        except requests.exceptions.URLRequired:
            data.result_error_required_url = True
            data.result_error = True
        except requests.exceptions.InvalidURL:
            data.result_error_invalid_url = True
            data.result_error = True
        except:
            data.result_error = False
    #
    #
    elif data.input_type == 'OPTIONS':
        try:
            res = requests.options(url=data.input_url, headers=data.input_headers, proxies=data.input_proxies,
                               params=data.input_params, data=data.input_form, json=data.input_json,
                               timeout=data.input_timeout)
        except requests.exceptions.Timeout:
            data.result_error_timeout = True
            data.result_error = True
        except requests.exceptions.ProxyError:
            data.result_error_proxy = True
            data.result_error = True
        except requests.exceptions.URLRequired:
            data.result_error_required_url = True
            data.result_error = True
        except requests.exceptions.InvalidURL:
            data.result_error_invalid_url = True
            data.result_error = True
        except:
            data.result_error = False
    #
    #
    #
    if res is not None:
        if res.status_code is not  None:
            data.result_code = res.status_code
        if res.headers is not None:
            data.result_header = res.headers
        if res.text is not None:
            data.result_body = res.text
        if res.cookies is not None:
            cookies = ''
            for ii in  res.cookies:
                cookies += '"Path":"' + str(ii.path) + '"\t"Name":"' + str(ii.name) +'"\t"Value":"' + str(ii.value) + '"'
                cookies += '\n'
            data.result_cookies = cookies
    #
    return data

#
#
def get_proxy_list(filename='trusted_proxy_list.txt'):
    result = list()
    try:
        with open(filename, 'r') as rfile:
            proxy_txt = rfile.read()
            tmp_list = proxy_txt.split(sep='\n')
            proxies = tmp_list[3:-1]
            for proxy in proxies:
                if proxy is not  None:
                    add_proxy = proxy.strip()
                    if add_proxy != '':
                        result.append(proxy)
    except:
        pass
    return result
