
from BaseHandler import BaseHandler
import conf
import fb_util
import urllib

class CreateCoverHandler(BaseHandler):
    
    def get(self):
        if self.user:

            albumList = self.facebook.api(u'/'+self.user.user_id,
                                {u'fields': 'albums'})
            # check if there is an album name fabpica
            fabpica_album_id = -1
            for album in albumList['albums']['data']:
                if album['name'] == conf.FACEBOOK_ALBUMNAME:    # if the album already created, take the id and break    
                    fabpica_album_id = album['id']
                    break
            if fabpica_album_id == -1:
                #create the album
                result = self.facebook.api(u'/'+self.user.user_id+'/albums', params={u'name':conf.FACEBOOK_ALBUMNAME}, method='POST')
                fabpica_album_id = result['id'] #record the id of the created album
            try:
                img_data = open("D:\My Personal Files\Work\FBCoverMaker\static\splash.jpg", 'rb').read()
            except Exception, ex:
                print "cannot open picture"
            
            self.facebook.api_multipart(u'/'+fabpica_album_id+'/photos', 
                                        [('source','pic.jpg',img_data)],
                                        params={'message':'no unicode support'})
        else:
            print "USER NOT LOGGED IN"
            