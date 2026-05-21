import requests
import re
import os
import sys

url = "https://www.520switch.com/user/coin/"

# 从环境变量获取 Cookie（GitHub Actions 环境）
cookie = os.environ.get('COOKIE_520')
if not cookie:
    print("❌ 错误: 未找到 COOKIE_520 环境变量")
    print("请在 GitHub Secrets 中配置 COOKIE_520")
    sys.exit(1)

# 先获取页面（需要登录态）
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Cookie': cookie
})

print("📡 正在访问签到页面...")
response = session.get(url)
html = response.text
print(html)
# 提取 nonce
match = re.search(r'"ajax_nonce"\s*:\s*"([a-f0-9]+)"', html)
if match:
    nonce = match.group(1)
    print(f"✅ 获取到 nonce: {nonce}")
    
    # 使用 nonce 发起 AJAX 签到请求
    ajax_data = {
        'action': 'zb_user_qiandao',
        'nonce': nonce
    }
    
    print("🎯 正在执行签到...")
    ajax_response = session.post(
        'https://www.520switch.com/wp-admin/admin-ajax.php',
        data=ajax_data
    )
    
    result = ajax_response.json()
    print(f"📊 签到结果: {result}")
    
    # 判断签到是否成功
    if result.get('status') == 1:
        print("🎉 签到成功！")
    else:
        print(f"⚠️ 签到失败: {result.get('msg', '未知错误')}")
        sys.exit(1)
else:
    print("❌ 未找到 nonce，可能 Cookie 已过期或需要重新登录")
    sys.exit(1)
