import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))




#from multiprocessing import Pool
#from PIL import Image
#import os
#from os import listdir
#from os.path import isfile, join


#class Thumbnail(object):
#    SIZE = (75,75)


#    def __init__(self, *args, **kwargs):
#        return super(Thumbnail, self).__init__(*args, **kwargs)

#    def run(self):

#        def gen(fl):
#            im = Image.open(fl)
#            im.thumbnail(self.SIZE,Image.ANTIALIAS)
#            base,fname = os.path.split(fl)
#            save_path = os.path.join(base,'thumb',fname)
#            im.save(save_path)


#        pool = Pool()
#        pool.map(gen,self.file_lst)
#        pool.close()
#        pool.join()



#if __name__ == '__main__':

#    basedir = '.\\data'
#    file_lst = [ f for f in listdir(basedir) if isfile(join(basedir,f)) ]


#    #tb = Thumbnail(



