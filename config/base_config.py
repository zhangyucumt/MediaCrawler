# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/config/base_config.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# 基础配置
PLATFORM = "dy"  # 平台，xhs | dy | ks | bili | wb | tieba | zhihu
KEYWORDS = "刘翔"  # 关键词搜索配置，以英文逗号分隔
LOGIN_TYPE = "cookie"  # qrcode or phone or cookie
COOKIES = "UIFID_TEMP=9f119777b70db29e092f16dc2972b95ccc9df01a979ae01132052c40ee3e10ba7c8195c93f3bfa9274616ce0d5f5239b07c83aa29db62999af1169df142899cd51687c645e10e6a7bb89af83d482380b; hevc_supported=true; fpk1=U2FsdGVkX1+u+VhstiOZejhlF59d6oSzGD2HwTFa/jmQycoFyamYuoi2QIL9GmD3a3mWSs2Ub+0qvDfi5OZ8ag==; fpk2=d6dcc0a6def5582f8d3a9f7f2addb88b; UIFID=9f119777b70db29e092f16dc2972b95ccc9df01a979ae01132052c40ee3e10ba7c8195c93f3bfa9274616ce0d5f5239b3cf9f5306b18771140479f60e388cc667b9f163c0b777abdba91ef5011c109f2a4155f3f1583c9e8a577f94f8f86fce7052084bf7ad483c3db6587cf4baec41a08de28169168eb2d0c9054a598d1984469c85be4c37b67f55c97d7d16aa925d336b6eb821d88fb93e22a04517d86da92; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; enter_pc_once=1; s_v_web_id=verify_mhngmjtj_amzi8AKo_REdv_4H2c_9jye_uh1Dma272LEu; dy_swidth=1920; dy_sheight=1080; passport_csrf_token=bfb5ab325aa705257a137a0106dcc41c; passport_csrf_token_default=bfb5ab325aa705257a137a0106dcc41c; bd_ticket_guard_client_web_domain=2; passport_mfa_token=CjfUqiB7IujTefguhq0aInb64PsOukq8No6AD1b%2BfEtOJSQURh0tf%2FvdWO6RctNPe0Pd5kwrROz8GkoKPAAAAAAAAAAAAABPrl0N9EtkQk1wD%2B8l6Le40Q3UCgpZklEDgLFa90FHXM9yRekGH6blP%2BN3th4vWPKdgRDW6oAOGPax0WwgAiIBA3artBs%3D; d_ticket=dff9dbf2442f6c4180616164aef509f8e76d3; n_mh=pDrxk-g7dfEXl_RBVi-gXFGnxyswZ1Lt2CkHlrCaQlM; passport_auth_status=1cbcb8887d7325c2fd41d1b752f9e95b%2C; passport_auth_status_ss=1cbcb8887d7325c2fd41d1b752f9e95b%2C; is_staff_user=false; __security_server_data_status=1; SelfTabRedDotControl=%5B%5D; is_dash_user=1; SEARCH_RESULT_LIST_TYPE=%22single%22; xgplayer_device_id=92843313787; xgplayer_user_id=626682905618; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAQbsmI0ID0KQuPb_M--4TGEMJmRuh-efD39ZbsvcotQ5BWa1SKw_Cqg8jKwwb56Yj%2F1763049600000%2F0%2F0%2F1763030447037%22; WallpaperGuide=%7B%22showTime%22%3A1762436032430%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A14%2C%22cursor2%22%3A4%7D; publish_badge_show_info=%220%2C0%2C0%2C1763120797901%22; download_guide=%223%2F20251114%2F0%22; pwa2=%220%7C0%7C1%7C0%22; passport_assist_user=CkG93fdroDX9tBu_vzQKIxT6J8Iigm69kG7_49KSyIZZmH761TDI7JmqgoKtOy95Z_D3i_9XC2NyFGoc4dI4bOKB3RpKCjwAAAAAAAAAAAAAT7mZsZH4jHE-mSUXCVX258qJwxnNz6Mi57IzQb-p6OKX8dB8KFZ-WnEeboryo_6MgP4Q9eGBDhiJr9ZUIAEiAQMuLLZQ; sid_guard=75e3b347ff07fa120ca1ce501f6c1ab6%7C1763351386%7C5184000%7CFri%2C+16-Jan-2026+03%3A49%3A46+GMT; uid_tt=af119da7f6ac40ac8cabd2272d9e5767; uid_tt_ss=af119da7f6ac40ac8cabd2272d9e5767; sid_tt=75e3b347ff07fa120ca1ce501f6c1ab6; sessionid=75e3b347ff07fa120ca1ce501f6c1ab6; sessionid_ss=75e3b347ff07fa120ca1ce501f6c1ab6; session_tlb_tag=sttt%7C3%7CdeOzR_8H-hIMoc5QH2watv________-qi0j6YAvUeLcuRx93g875iasWdJQ50gzY107nMYKVMy0%3D; session_tlb_tag_bk=sttt%7C3%7CdeOzR_8H-hIMoc5QH2watv________-qi0j6YAvUeLcuRx93g875iasWdJQ50gzY107nMYKVMy0%3D; sid_ucp_v1=1.0.0-KGQ3NWNhN2UzZjQ4MDRiZWRjYTExMjk5ZTZlOTIxZTRkYTA1N2Y4YjUKIQiHypDN3YzmAxDaturIBhjvMSAMMI639ooGOAdA9AdIBBoCaGwiIDc1ZTNiMzQ3ZmYwN2ZhMTIwY2ExY2U1MDFmNmMxYWI2; ssid_ucp_v1=1.0.0-KGQ3NWNhN2UzZjQ4MDRiZWRjYTExMjk5ZTZlOTIxZTRkYTA1N2Y4YjUKIQiHypDN3YzmAxDaturIBhjvMSAMMI639ooGOAdA9AdIBBoCaGwiIDc1ZTNiMzQ3ZmYwN2ZhMTIwY2ExY2U1MDFmNmMxYWI2; _bd_ticket_crypt_cookie=da73f98f1124970aaefcf0566dbb5801; login_time=1763351384684; DiscoverFeedExposedAd=%7B%7D; __security_mc_1_s_sdk_crypt_sdk=ddf663af-4d94-b798; __security_mc_1_s_sdk_cert_key=1c6b161e-49e6-aba3; __security_mc_1_s_sdk_sign_data_key_web_protect=3c19a07b-43d6-ab28; __ac_nonce=0691c17bf00811dcd5f93; __ac_signature=_02B4Z6wo00f01IBivxgAAIDB0oFrFh.YqTCAQruAAEkJ7b; douyin.com; device_web_cpu_core=6; device_web_memory_size=8; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A6%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; strategyABtestKey=%221763448771.455%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAQbsmI0ID0KQuPb_M--4TGEMJmRuh-efD39ZbsvcotQ5BWa1SKw_Cqg8jKwwb56Yj%2F1763481600000%2F0%2F1763448771826%2F0%22; ttwid=1%7C3uTKEYFBPGKQC1whprNYLdA4dD4mUUY5a1-aVTuaZSY%7C1763448772%7Cd3723879ef988c64c31d6fe801ceb0e43c0ad380c04d285b2071a0320d5728fa; biz_trace_id=df4c4ed3; odin_tt=aab1aa57589b0a95302f194bac77b804602789b7198a1a87fc3cd2a0852e6aead25cf8abd1a661a0999203805d75496de3c31fd9d060f177dff5fe4279d5d30c; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUGQ2QjRiV3M1RnF3NE9tZTdtc01XTndkOFYxS2FDZ0dDWjdKZnRwc2s0Ym1yVUM5cW9sMFUrN01CWXFDNFEyd3RXUEx4OWJJWE0wUFBIam9zZjJjQW89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJQZDZCNGJXczVGcXc0T21lN21zTVdOd2Q4VjFLYUNnR0NaN0pmdHBzazRibXJVQzlxb2wwVSs3TUJZcUM0UTJ3dFdQTHg5YklYTTBQUEhqb3NmMmNBbz0iLCJ0c19zaWduIjoidHMuMi5iMTVhNDg3OWJmNWM3ODdiNDdjNThkM2UyYjllNGVkZjIwNjNmNDEwNmJkYjFlODNkZGRjZjNlZTJjYjY2YjU0YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJWdDBBZ1JMemhRMDI4RVNteWhISHVSdFEvWGhtd0kwdkhLUnRzVGNLS0VFPSIsInNlY190cyI6IiNwR0VTNGt6V3lDQWd3VW0wUzlZVzBSMU1SQk9aK2dzbHN1QXowQXhUMGZMR2M1bVBmMkdUZFpqOXpJTkkifQ%3D%3D; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=true"
CRAWLER_TYPE = (
    "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
)
# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"  # kuaidaili | wandouhttp

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# ==================== CDP (Chrome DevTools Protocol) 配置 ====================
# 是否启用CDP模式 - 使用用户现有的Chrome/Edge浏览器进行爬取，提供更好的反检测能力
# 启用后将自动检测并启动用户的Chrome/Edge浏览器，通过CDP协议进行控制
# 这种方式使用真实的浏览器环境，包括用户的扩展、Cookie和设置，大大降低被检测的风险
ENABLE_CDP_MODE = True

# CDP调试端口，用于与浏览器通信
# 如果端口被占用，系统会自动尝试下一个可用端口
CDP_DEBUG_PORT = 9222

# 自定义浏览器路径（可选）
# 如果为空，系统会自动检测Chrome/Edge的安装路径
# Windows示例: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# macOS示例: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CUSTOM_BROWSER_PATH = ""

# CDP模式下是否启用无头模式
# 注意：即使设置为True，某些反检测功能在无头模式下可能效果不佳
CDP_HEADLESS = False

# 浏览器启动超时时间（秒）
BROWSER_LAUNCH_TIMEOUT = 60

# 是否在程序结束时自动关闭浏览器
# 设置为False可以保持浏览器运行，便于调试
AUTO_CLOSE_BROWSER = True

# 数据保存类型选项配置,支持四种类型：csv、db、json、sqlite, 最好保存到DB，有排重的功能。
SAVE_DATA_OPTION = "json"  # csv or db or json or sqlite

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 15

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬媒体模式（包含图片或视频资源），默认不开启爬媒体
ENABLE_GET_MEIDAS = False

# 是否开启爬评论模式, 默认开启爬评论
ENABLE_GET_COMMENTS = True

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 10

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    "零几": "年份",  # 将“零几”识别为一个整体
    "高频词": "专业术语",  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"

# 爬取间隔时间
CRAWLER_MAX_SLEEP_SEC = 2

from .bilibili_config import *
from .xhs_config import *
from .dy_config import *
from .ks_config import *
from .weibo_config import *
from .tieba_config import *
from .zhihu_config import *
