import requests
from bs4 import BeautifulSoup
import random
import time
from email.mime.text import MIMEText
import smtplib
from email.header import Header

def send_remind(shoujianren):
    from_addr = '邮箱'
    passwd = '密码'
    to_addr = shoujianren

    msg = MIMEText('XX小区自如房源更新啦！', 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('XX小区自如房源更新啦！', 'utf-8').encode()

    ser = smtplib.SMTP('smtp.163.com', 25) #当from的邮箱是163邮箱时
    ser.set_debuglevel(1)
    ser.login(from_addr, passwd)
    ser.sendmail(from_addr, [to_addr], msg.as_string())
    ser.quit()

if __name__ =='__main__':
    cookies = [
        'PHPSESSID=tg93ph4k8dnj5smgfmcmcdf0u1; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=4f8c5ea3-105d-41b0-8ba5-f4f8c226261c; __utma=14049387.1251815800.1527058479.1527058479.1527058479.1; __utmc=14049387; __utmz=14049387.1527058479.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527058479; gr_session_id_8da2730aaedd7628=50fcd86b-1f2b-47cf-ae97-7d3bd7ba8e26_true; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]',
        'PHPSESSID=rqfvcrc9k1ictv46nib0id3d66; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=0df141a4-f093-44b1-92f1-9f7b73b59f03; __utma=14049387.1670358485.1527047111.1527047111.1527047111.1; __utmc=14049387; __utmz=14049387.1527047111.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527047111; gr_session_id_8da2730aaedd7628=b74e3f3c-e2ae-41ef-81e2-20778a3f70d5_true; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]',
        'PHPSESSID=eo8j681h0i42m1bqtbrnctfbs6; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=a3ac7e72-6f2b-420c-987f-f23aa3a2e7d8; __utma=14049387.1298641926.1527058780.1527058780.1527058780.1; __utmc=14049387; __utmz=14049387.1527058780.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527058780; gr_session_id_8da2730aaedd7628=78cad9d6-f29d-4bb9-be1b-87660cc87f4e_true; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]',
        'PHPSESSID=lec52qrkrvnupld61ivlassb56; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=b0fa0aef-9387-4998-86e2-0a5875518674; __utma=14049387.384096565.1527058872.1527058872.1527058872.1; __utmc=14049387; __utmz=14049387.1527058872.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527058872; gr_session_id_8da2730aaedd7628=90106001-bc71-4c2a-b780-7c5f1f167906_true; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]',
        'PHPSESSID=sbkoc6iignipomlhf63gplbbr2; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=a6a99a04-b0aa-4f37-99c3-3cf2c973ee2f; gr_session_id_8da2730aaedd7628=8d562931-b897-45ec-8dc9-629d0caa348a_true; __utma=14049387.1300717609.1527058937.1527058937.1527058937.1; __utmc=14049387; __utmz=14049387.1527058937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527058937; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]'
    ]
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'Cache - Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=rqfvcrc9k1ictv46nib0id3d66; hlwyfb_m_current_city_code=110000; CURRENT_CITY_CODE=110000; curUrl=index; gr_user_id=0df141a4-f093-44b1-92f1-9f7b73b59f03; __utma=14049387.1670358485.1527047111.1527047111.1527047111.1; __utmc=14049387; __utmz=14049387.1527047111.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=14049387.1.10.1527047111; gr_session_id_8da2730aaedd7628=b74e3f3c-e2ae-41ef-81e2-20778a3f70d5_true; city_code=110000; history=[{%22flag%22:%22%22%2C%22keywords%22:%22%E5%8F%8C%E7%B4%AB%E5%B0%8F%E5%8C%BA%22}]',
        'Host': 'm.ziroom.com',
        'Upgrade - Insecure - Requests': '1',
        'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
    session = requests.session()
    fangyuan_url = "http://m.ziroom.com/BJ/room/99999999.html" #此处为关注的房源的m端url
    while True:
        x = random.randint(0, 4)
        header['Cookie'] = cookies[x]
        wb_data = session.get(fangyuan_url, headers=header)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        img_name = soup.select('#detailFocusSlider > div.slick_detail > div > img')[0].get('onerror')
        if img_name != "this.src='/img/pzz_big.jpg'":
            send_remind('接收通知的邮箱')
            break
        a = random.uniform(60, 100)
        time.sleep(a)
