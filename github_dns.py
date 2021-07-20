import re

import requests


class gitip:
    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'}
        self.ip_1 = 'https://github.com.ipaddress.com/alive.github.com'  # alive.github.com
        self.ip_2 = 'https://github.com.ipaddress.com/live.github.com'  # live.github.com
        self.ip_3 = 'https://githubassets.com.ipaddress.com/github.githubassets.com'  # github.githubassets.com
        self.ip_4 = 'https://github.com.ipaddress.com/central.github.com'  # central.github.com
        self.ip_5 = 'https://githubusercontent.com.ipaddress.com/desktop.githubusercontent.com'  # desktop.githubusercontent.co
        self.ip_6 = 'https://github.com.ipaddress.com/assets-cdn.github.com'  # assets-cdn.github.com
        self.ip_7 = 'https://githubusercontent.com.ipaddress.com/camo.githubusercontent.com'  # camo.githubusercontent.com
        self.ip_8 = 'https://fastly.net.ipaddress.com/github.map.fastly.net'  # github.map.fastly.net
        self.ip_9 = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'  # github.global.ssl.fastly.net
        self.ip_10 = 'https://github.com.ipaddress.com/gist.github.com'  # gist.github.com
        self.ip_11 = 'https://github.io.ipaddress.com/'  # github.io
        self.ip_12 = 'https://github.com.ipaddress.com/'  # github.com
        self.ip_13 = 'https://github.blog.ipaddress.com/'  # github.blog
        self.ip_14 = 'https://github.com.ipaddress.com/api.github.com'  # api.github.com
        self.ip_15 = 'https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com'  # raw.githubusercontent.com
        self.ip_16 = 'https://githubusercontent.com.ipaddress.com/user-images.githubusercontent.com'  # user-images.githubusercontent.com
        self.ip_17 = 'https://githubusercontent.com.ipaddress.com/favicons.githubusercontent.com'  # favicons.githubusercontent.com
        self.ip_18 = 'https://githubusercontent.com.ipaddress.com/avatars5.githubusercontent.com'  # avatars5.githubusercontent.com
        self.ip_19 = 'https://githubusercontent.com.ipaddress.com/avatars4.githubusercontent.com'  # avatars4.githubusercontent.com
        self.ip_20 = 'https://githubusercontent.com.ipaddress.com/avatars3.githubusercontent.com'  # avatars3.githubusercontent.com
        self.ip_21 = 'https://githubusercontent.com.ipaddress.com/avatars2.githubusercontent.com'  # avatars2.githubusercontent.com
        self.ip_22 = 'https://githubusercontent.com.ipaddress.com/avatars1.githubusercontent.com'  # avatars1.githubusercontent.com
        self.ip_23 = 'https://githubusercontent.com.ipaddress.com/avatars0.githubusercontent.com'  # avatars0.githubusercontent.com
        self.ip_24 = 'https://githubusercontent.com.ipaddress.com/avatars.githubusercontent.com'  # avatars.githubusercontent.com
        self.ip_25 = 'https://github.com.ipaddress.com/codeload.github.com'  # codeload.github.com
        self.ip_26 = 'https://amazonaws.com.ipaddress.com/github-cloud.s3.amazonaws.com'  # github-cloud.s3.amazonaws.com
        self.ip_27 = 'https://amazonaws.com.ipaddress.com/github-com.s3.amazonaws.com'  # github-com.s3.amazonaws.com
        self.ip_28 = 'https://amazonaws.com.ipaddress.com/github-production-release-asset-2e65be.s3.amazonaws.com'  # github-production-release-asset-2e65be.s3.amazonaws.com
        self.ip_29 = 'https://amazonaws.com.ipaddress.com/github-production-user-asset-6210df.s3.amazonaws.com'  # github-production-user-asset-6210df.s3.amazonaws.com
        self.ip_30 = 'https://amazonaws.com.ipaddress.com/github-production-repository-file-5c1aeb.s3.amazonaws.com'  # github-production-repository-file-5c1aeb.s3.amazonaws.com
        self.ip_31 = 'https://githubstatus.com.ipaddress.com/'  # githubstatus.com
        self.ip_32 = 'https://github.community.ipaddress.com/'  # github.community
        self.ip_33 = 'https://githubusercontent.com.ipaddress.com/media.githubusercontent.com'  # media.githubusercontent.com

    def get_1(self):  # github.com
        response = requests.get(self.ip_1, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    alive.github.com')
        print(ret.group() + '    alive.github.com')

    def get_2(self):
        response = requests.get(self.ip_2, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    live.github.com')
        print(ret.group() + '    live.github.com')

    def get_3(self):
        response = requests.get(self.ip_3, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.githubassets.com')
        print(ret.group() + '    github.githubassets.com')

    def get_4(self):
        response = requests.get(self.ip_4, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    central.github.com')
        print(ret.group() + '    central.github.com')

    def get_5(self):
        response = requests.get(self.ip_5, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    desktop.githubusercontent.com')
        print(ret.group() + '    desktop.githubusercontent.com')

    def get_6(self):
        response = requests.get(self.ip_6, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    assets-cdn.github.com')
        print(ret.group() + '    assets-cdn.github.com')

    def get_7(self):
        response = requests.get(self.ip_7, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    camo.githubusercontent.com')
        print(ret.group() + '    camo.githubusercontent.com')

    def get_8(self):
        response = requests.get(self.ip_8, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.map.fastly.net')
        print(ret.group() + '    github.map.fastly.net')

    def get_9(self):
        response = requests.get(self.ip_9, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.global.ssl.fastly.net')
        print(ret.group() + '    github.global.ssl.fastly.net')

    def get_10(self):
        response = requests.get(self.ip_10, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    gist.github.com')
        print(ret.group() + '    gist.github.com')

    def get_11(self):
        response = requests.get(self.ip_11, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.io')
        print(ret.group() + '    github.io')

    def get_12(self):
        response = requests.get(self.ip_12, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.com')
        print(ret.group() + '    github.com')

    def get_13(self):
        response = requests.get(self.ip_13, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.blog')
        print(ret.group() + '    github.blog')

    def get_14(self):
        response = requests.get(self.ip_14, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    api.github.com')
        print(ret.group() + '    api.github.com')

    def get_15(self):
        response = requests.get(self.ip_15, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    raw.githubusercontent.com')
        print(ret.group() + '    raw.githubusercontent.com')

    def get_16(self):
        response = requests.get(self.ip_16, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    user-images.githubusercontent.com')
        print(ret.group() + '    user-images.githubusercontent.com')

    def get_17(self):
        response = requests.get(self.ip_17, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    favicons.githubusercontent.com')
        print(ret.group() + '    favicons.githubusercontent.com')

    def get_18(self):
        response = requests.get(self.ip_18, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars5.githubusercontent.com')
        print(ret.group() + '    avatars5.githubusercontent.com')

    def get_19(self):
        response = requests.get(self.ip_19, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars4.githubusercontent.com')
        print(ret.group() + '    avatars4.githubusercontent.com')

    def get_20(self):
        response = requests.get(self.ip_20, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars3.githubusercontent.com')
        print(ret.group() + '    avatars3.githubusercontent.com')

    def get_21(self):
        response = requests.get(self.ip_21, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars2.githubusercontent.com')
        print(ret.group() + '    avatars2.githubusercontent.com')

    def get_22(self):
        response = requests.get(self.ip_22, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars1.githubusercontent.com')
        print(ret.group() + '    avatars1.githubusercontent.com')

    def get_23(self):
        response = requests.get(self.ip_23, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars0.githubusercontent.com')
        print(ret.group() + '    avatars0.githubusercontent.com')

    def get_24(self):
        response = requests.get(self.ip_24, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    avatars.githubusercontent.com')
        print(ret.group() + '    avatars.githubusercontent.com')

    def get_25(self):
        response = requests.get(self.ip_25, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    codeload.github.com')
        print(ret.group() + '    codeload.github.com')

    def get_26(self):
        response = requests.get(self.ip_26, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github-cloud.s3.amazonaws.com')
        print(ret.group() + '    github-cloud.s3.amazonaws.com')

    def get_27(self):
        response = requests.get(self.ip_27, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github-com.s3.amazonaws.com')
        print(ret.group() + '    github-com.s3.amazonaws.com')

    def get_28(self):
        response = requests.get(self.ip_28, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github-production-release-asset-2e65be.s3.amazonaws.com')
        print(ret.group() + '    github-production-release-asset-2e65be.s3.amazonaws.com')

    def get_29(self):
        response = requests.get(self.ip_29, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github-production-user-asset-6210df.s3.amazonaws.com')
        print(ret.group() + '    github-production-user-asset-6210df.s3.amazonaws.com')

    def get_30(self):
        response = requests.get(self.ip_30, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github-production-repository-file-5c1aeb.s3.amazonaws.com')
        print(ret.group() + '    github-production-repository-file-5c1aeb.s3.amazonaws.com')

    def get_31(self):
        response = requests.get(self.ip_31, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    githubstatus.com')
        print(ret.group() + '    githubstatus.com')

    def get_32(self):
        response = requests.get(self.ip_32, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    github.community')
        print(ret.group() + '    github.community')

    def get_33(self):
        response = requests.get(self.ip_33, headers=self.header)
        ret = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',
                        response.text)
        self.ip_list.append(ret.group() + '    media.githubusercontent.com')
        print(ret.group() + '    media.githubusercontent.com')


if __name__ == '__main__':
    ip_list = []
    error = 0
    github = gitip(ip_list)
    github.get_1()
    github.get_2()
    github.get_3()
    github.get_4()
    github.get_5()
    github.get_6()
    github.get_7()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
    github.get_8()
