# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
data = """





背景.png (55.24 KB, 下载次数: 39)

下载附件 
下载到手机

 保存到相册








▍发布时间
MIUI 开发版 9.5.23 部分机型延迟发布

▍升级说明
1.已加入防回刷机制的机型无法降级刷回旧版本的开发版或稳定版，否则会导致手机变砖，小米Max 3防回刷说明 小米6X防回刷说明 红米6 Pro防回刷说明 红米Note 5防回刷说明
2. MIUI 6/7/8/9开发版可进入“设置→我的设备→MIUI版本”在线升级
3. MIUI 6/7/8/9稳定版用户，建议通过线刷升级至 MIUI 10开发版，教程请见下方“刷机指南”
4. 部分机型可能因功能进版时间略有差异，具体功能请以手机端展示日志为准


▍重要说明
1. 已升级 Android P 的小米6用户，不建议回刷版本，因底层版本不同，可能出现功能异常等问题；从 Android P 回刷至 Android O, 若出现查找手机、指纹支付等异常问题，需先刷入过渡的线刷包（点击下载），再刷 Android O 版本即可正常使用。
2. 红米6A、红米6、小米平板4、小米平板4 Plus、小米PLAY、红米6 Pro因测试系统稳定性延迟发布公测
3. 小米8、小米9 SE因处理开启DC调光后屏幕闪烁问题延迟发布公测
4. 小米8透明探索版、小米8屏幕指纹版、小米8 SE、小米MIX 3、小米9、小米MIX 2S 因排查闹钟是否正常关闭问题延迟发布公测
5. 小米Note3 因适配 Android P，暂停公测发布

系统
优化 取消定时关闭勿扰后的声音提示
       
锁屏、状态栏、通知栏 
修复 息屏时偶现屏下指纹无法解锁的问题
        
相册
优化 最近相册可以显示相册编辑后的照片
优化 相册设置项支持云同步
修复 照片电影微信无法发送问题

设置
新增 防闪烁模式，全局直流调光，前往设置-显示-防闪烁模式开启（小米MIX3、小米8）

小爱同学
新增 语音打开“米家摄像机”，家中情况一目了然
新增 语音开启/关闭省电模式和Talkback，试试说“打开省电模式”
新增 小爱捷径支持增删卡片选项，长按捷径卡片进入编辑态，点击你想要的卡片就能使用该功能了
新增 小爱捷径新增布朗熊、一键截屏、今日热点和乘车码等捷径卡片
优化 小爱在人脸解锁、屏下指纹解锁下的交互体验

小米云服务
修复 偶现在系统设置中登录帐号后，云服务闪退的问题

   
▍刷机指南
1. MIUI 6/7/8/9开发版可点击“设置”→“我的设备”→“MIUI版本”在线升级，升级前务必备份重要数据
2. MIUI 6/7/8/9稳定版用户版本用户建议通过线刷升级，线刷会清除全部数据
3. 开发版/稳定版相互刷机时，需备份好重要数据，再通过线刷方式清除所有数据进行刷机，防止出现异常问题
4. 新机型有防刷机保护，线刷前请先进行 Bootloader 解锁，点此立即解锁BL
5. 小米手机完整刷机教程：点此查看



"""

import re
print(data)

print(repr(data))
b = re.sub(r'\xa0| ', '',data)
# b = data.replace('\xa0','')
# b = b.replace(' ','')
# print('#'*20)
# print(b)
# print(repr(b))
# # print('#'*20)
# # for text in re.findall('(.+?)(\n\n)', b, flags=re.DOTALL):
# #     print(text)

# print(re.search('(▍重要说明.+?)(\n{2,})', b, flags=re.DOTALL).group(0))
# print(re.search('(▍重要说明.+?)(\n{2,})', b, flags=re.S).group(0))
print(re.search('(▍重要说明.+?)([\n\s]{2,})', data, flags=re.S).group(0))
print(re.search('(▍刷机指南.+?)([\n\s]{2,})', data, flags=re.DOTALL).group(0))
print(re.search('(▍发布时间.+?)([\n\s]{2,})', data, flags=re.DOTALL).group(0))

# print(re.search('(▍刷机指南.+?)(\n{2,})', b, flags=re.DOTALL).group(0))
# print(re.search('(▍发布时间.+?)(\n{2,})', b, flags=re.DOTALL).group(0))


# import re
# print("="*20)
# a = re.search("(▍重要说明[.\s\S]*)[\n]{2,}", data)
# print(a.group(1))
# print("="*20)
# # for i in  re.finditer(r'(?s)((?:[^\n][\n]?)+)', data):
# #     print(i.group(),'====='*20)
# print(re.search("▍刷机指南[.\s\S]*[\n]{2,}", data).group())
# print("="*20)
#
# print(re.search(r"▍发布时间[.\s\S]*[\n]{2,}", data).group())


import re

# text = '''Paragraph one
# on two lines.
#
#
# Paragraph two.
#
#
# Paragraph three.'''
#
# print('With findall:')
# for num, para in enumerate(re.findall(r'(.+?)(\n{2,})',
#                                       data,
#                                       flags=re.DOTALL)
#                            ):
#     print(num, repr(para))

# print(re.search(r'▍重要说明(.+)\n{2,}$', data, flags=re.DOTALL).group(1))

# print('With re.split:')
# for num, para in enumerate(re.split(r'\n{2,}', data)):
#     # print(num, repr(para))
#     # print(num, para)
#     print(para,"#"*50)