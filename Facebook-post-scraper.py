import requests
from bs4 import BeautifulSoup
from secrets import username, password
import urllib
import urllib.request

class FaceBookBot():
    login_basic_url = 'https://mbasic.facebook.com/login'
    login_mobile_url = 'https://m.facebook.com/login'
    payload = {
            'email': username,
            'pass': password
        }
    post_ID = ""


    def get_pos

    def parse_html(self, request_url):
        with requests.Session() as session:
            post = session.post(self.login_basic_url, data=self.payload)
            parsed_html = session.get(request_url)
        return parsed_html

    def get_url(self):
        urlData = urllib.request.urlopen('https://www.facebook.com/photo.php?fbid={self.post_ID}&id=415518858611168')
        data = str(urlData.readlines())
        bs = BeautifulSoup(data)
        imgUrl = bs.find('img', attrs={'class': 'fbPhotoImage img'}).get('src')
        urllib.request.urlretrieve(imgUrl, "plane.jpg")
        return imgUrl

    def post_content(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        content = soup.find_all('p')
        post_content = []
        for lines in content:
            post_content.append(lines.text)
        
        post_content = ' '.join(post_content)    
        return post_content

    def date_posted(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        date_posted = soup.find('abbr')
        return date_posted.text


