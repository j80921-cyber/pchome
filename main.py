import json
import requests

activity_url = "https://ecapi.pchome.com.tw/fsapi/marketing/signingift/v1/activity"
base_url = "https://ecapi.pchome.com.tw/fsapi/marketing/signingift/v1/signin"
coin_url = "https://ecvip.pchome.com.tw/fsapi/pchcoin/coinTotal&1"
coin_url2 = (
    "https://ecvip.pchome.com.tw/fsapi/pchcoin/mainList&offset=1&limit=20&1"
)


headers_template = {
    "accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "origin": "https://24h.pchome.com.tw",
    "referer": "https://24h.pchome.com.tw/",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/PChome_APP_ios_3.60.2",
}

# 填入ECWEBSESS=XXXXXX 其中XXXX是你的參數
cookies = [
    "ECWEBSESS=eec816e060.5b0225ad4b6b7441580fe5c2e1a37b53f714c02e.1755527848;",
    "ECWEBSESS=01abeee5bc.5a541099eaef0ef46da7a8ffcd3bb88ff1cbce78.1753901843;",
    "ECWEBSESS=6a70f1b7c6.c16610802a1e1ae306f743f46e1cb8c191e6c122.1753901722;",
    "ECWEBSESS=d852132cc1.117c039acc9fd8bab19d6a964cf17e0462333396.1753899898;",
    "ECWEBSESS=547c5feea4.6769e0dc3b15a3b6f3dacb3147d118ad7d134adf.1753900130;",
    "ECWEBSESS=69fc62126d.59f08fde77a88138bcb3f4d02e9a08d1aa6d2066.1753900246;",
    "ECWEBSESS=65accbef5f.d086fd1e949b8f619c486e057b832c7e3fa7f2cf.1753900405;",
    "ECWEBSESS=2a21d3e2d5.92de67d4d33513dfd7218ae6098a74ab9b59a122.1753898360;",
    "ECWEBSESS=cc155afb8c.8edb26c716c70d2b9bc4903f70b0c13275379af1.1753898660;",
    "ECWEBSESS=6e440be337.dc0be71697955e4a34ead70e85e6346865c0656e.1753899012;",
    "ECWEBSESS=b96285b568.a10aeb671823c83ed4f0590ce82ca8bfeddf5c72.1753899141;",
    "ECWEBSESS=19d52708a0.3ebdb9c440c6f6af014e8e17e4994b0cdfb4576b.1753899318;",
    "ECWEBSESS=be675e717a.3057ca3dda07e07e4ba048b99ff3a0e85da6aee6.1753899469;",
    "ECWEBSESS=b76847b40d.479f3d7a48e4c081e8106210a6b87db975eba73c.1753890795;",
    "ECWEBSESS=d9cacdb928.987455c0b360a442e764587a83bdee4cfbac547c.1753904980;",
    "ECWEBSESS=e2fcc02ea1.01c9e3ada68303b45cd56480556345e9f4ac352e.1753891821;",
    "ECWEBSESS=d149e2f877.afb11aac5fef52fddf25c63e08497e06ddbaf854.1753892229;",
    "ECWEBSESS=d8a370cca3.28a77c9c1523c1ab83e7e1cca83e4decc75f0ef6.1753892555;",
    "ECWEBSESS=9919cde990.60afac8517d795fc63184d28424afb7713579f04.1753892801;",
    "ECWEBSESS=d6839c0a59.9aea7d7a229d754337a20f05c26875430f4f56fc.1753893040;",
    "ECWEBSESS=0634c3e8ec.13579bfb6987c36190e9d13a3c7153c75daa7529.1753893181;",
    "ECWEBSESS=779800a212.bfc947ffb0de2224aebe2ed3711a0b9faf850158.1753895331;",
    "ECWEBSESS=3089028525.524f8e5044f5db3631ba04a5b1f1abc27b5757ec.1753895939;",
    "ECWEBSESS=43a545eb21.09910f95cde4571e6b6f6e0a4e66ce3e600419ff.1753903793;",
    "ECWEBSESS=24d2803233.bf2b957f47d22ed4ad2eafff77d90b732925fb36.1753904156;",
    "ECWEBSESS=588938ab27.859bff098b77cacaf9e6a126a420e720de8cf53b.1753904349;",
    "ECWEBSESS=d6aeb7fa7c.b0147c5feeab74cd7f9ecd22032587bae891db23.1753986373;",
    "ECWEBSESS=473969b526.479eabd777c135eb3655443f0b923808ff907779.1753986504;",
    "ECWEBSESS=bb89bc1b27.5db7299de8a6d1cc898e35bcf8bac266b850f112.1753986635;",
    "ECWEBSESS=d58732e9f9.94e53d6bed28b30a2656ce876cfa5f3a165a6248.1753986770;",
    "ECWEBSESS=7f97e7d3cb.e98e87f2d632f64168de2a21e10b1dfe0f38a01a.1753986887;",
    "ECWEBSESS=e00a7513f5.87e7b851d6d55ebfd3361af54979b7b441df8e89.1753987036;",
    "ECWEBSESS=0042e15299.12562b041117965f144befb280e71b920b3ea5aa.1753987211;",
    "ECWEBSESS=6624af97d1.5493fb063d406c4a53c2cad4fbefd6485954edc5.1753987316;",
    "ECWEBSESS=f6388801fe.0860a66ba24af71a627628c45452bbef7101017f.1753987461;",
    "ECWEBSESS=6bc7f9b394.cf2b2abd45d593a73af746b988c30afff51bfc30.1753987718;",
    "ECWEBSESS=bfda59aca1.8f09ee0871363be4f8fe3005a8cb878509ec41fc.1753988054;",
    "ECWEBSESS=3f8f4f3b37.fea2f7d680a3c056b0bff1c0f160a505a3b3df90.1753988177;",
    "ECWEBSESS=82f34ba3eb.56b17e3d05562d204f7180c828adae80a715cb84.1754235786;",
    "ECWEBSESS=69209f057c.1e904828e2ef28903bb5afb72ac0f883a3002875.1754236051;",
    "ECWEBSESS=6f7d7310c6.f0adcb406d61a09b52ab772cc34cb6ff82d2e36d.1754236306;",
    "ECWEBSESS=86e2d8120b.95e5e4f1164f13b7a19905895d5a908173cc2375.1754236763;",
    "ECWEBSESS=e59a116890.35120cb9eed30612b3a59cefb2a44a9d895e8508.1754237520;",
    "ECWEBSESS=38f0d00c21.c7e92f5972391981589dcd780f4c425ca6e05c88.1754237723;",
    "ECWEBSESS=7bffd72881.c66c52776650c8da4a9add276f05138830449cc4.1754238302;",
    "ECWEBSESS=fea22d4b2f.b4cc0f709714b7c4382debe7fd43d03d9a6ab71d.1754238816;",
    "ECWEBSESS=da453e467d.83ad482c7e18e5b2fe66d98d56d6d2f0225fed0f.1754239035;",
    "ECWEBSESS=12ede60632.e7a1395f616f72f0522f733b429da02b1badeb21.1754239411;",
    "ECWEBSESS=1c51a8f70e.976eeff3873e9bde364b9c314e73c952f8ff3be4.1754239723;",
    "ECWEBSESS=3512ec6963.5c7f5817e51589c726a7326ae5e2c0fc22529a96.1754239917;",
    "ECWEBSESS=6b3de1888e.200211a2fa028d488b3032de192c412becc7b56e.1754240096;",
    "ECWEBSESS=1ef49b416a.11955b9c0601d385b7cf7839f4e9a95bfcb75ac0.1755529045;",
    "ECWEBSESS=42979ef918.8381a2b52c266837cc101cde8d6c304b914fcc8d.1755529370;",
    "ECWEBSESS=0c765739a4.dbc666bc542c55d910ef244c45ef777afa312226.1755529608;",
]

status_mapping = {
    "success": "已簽到",
    "400-001": "已額滿",
    "400-002": "活動已暫停",
    "400-003": "簽到失敗",
    "400-004": "重覆簽到",
    "403": "綁定手機完成簽到",
    "401": "立即登入簽到",
    "401-001": "NO_LOGIN",
}


r = requests.get(activity_url, headers=headers_template)
data = r.json()
activity_id = data["current"]["activity_id"]
gift_id = data["current"]["activity_duration"][0]["gift_id"]


data2 = {"activity_id": activity_id, "gift_id": gift_id}

for i, cookie in enumerate(cookies, start=1):
    headers = headers_template.copy()
    headers["cookie"] = cookie
    response = requests.post(base_url, headers=headers, json=data2)
    response_data = response.json()
    status = response_data.get("status", "未知錯誤")
    message = status_mapping.get(status, "未知錯誤")

    r3 = requests.get(coin_url, headers=headers)
    r3_data = r3.json()

    if r3_data.get("objTotal") and isinstance(r3_data["objTotal"], dict):
        RESTAMT = r3_data["objTotal"].get("RESTAMT", "N/A")
        EXPAMT = r3_data["objTotal"].get("EXPAMT", "N/A")
        EXPDATE = r3_data["objTotal"].get("EXPDATE", "N/A")
    else:
        RESTAMT = "N/A"
        EXPAMT = "N/A"
        EXPDATE = "N/A"

    r4 = requests.get(coin_url2, headers=headers)
    r4_data = r4.json()
    if (
        r4_data.get("rows")
        and isinstance(r4_data["rows"], list)
        and len(r4_data["rows"]) > 0
    ):
        PPBALANCE = r4_data["rows"][0].get("PPBALANCE", "N/A")
        PPBALANCEDESC = r4_data["rows"][0].get("PPBALANCEDESC", "")
    else:
        PPBALANCE = "N/A"
        PPBALANCEDESC = ""

    account_str = f"帳號{i}".ljust(7)
    message_str = message.ljust(8)
    rest_amt_str = f"可用P幣:{RESTAMT}".ljust(12)
    exp_amt_str = f"到期P幣:{EXPAMT}".ljust(12)
    exp_date_str = f"到期時間:{EXPDATE}".ljust(18)

    # 修正原本縮排錯誤與斷行問題
    if PPBALANCE != "N/A":
        pp_balance_str = f"待生效:{PPBALANCE}".ljust(10)
    else:
        pp_balance_str = "待生效:0".ljust(10)

    print(
        f"{account_str}{message_str}{rest_amt_str}{exp_amt_str}{exp_date_str}{pp_balance_str}"  
