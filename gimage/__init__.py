import sys
import json
import urllib
import urllib2

def get_image_url(search_terms):
    url = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % urllib.quote_plus(search_terms.strip())
    try:
        msg = ''
        response = json.load(urllib2.urlopen(urllib2.Request(url, None, {'Referer': 'http://www..com/'})))
        if response.get('responseData') and response['responseData'].get('results'):
            results = response['responseData']['results']
            if len(results):
                msg = results[0]['unescapedUrl']
    except: pass

    return msg

if __name__ == '__main__':
    sys.stdout.write(get_image_url(" ".join(sys.argv)))
