# contain utility function relate to facebook
import httplib, mimetypes
import urllib

#
## decode the signed request
#def load_signed_request(sr, app_secret, time_limit = None):    #time_limit is in second
#    try:
#        sig, payload = sr.split(u'.', 1)
#        sig = Util.base64_url_decode(sig)
#        data = parse_json(Util.base64_url_decode(payload))
#
#        expected_sig = hmac.new(
#            app_secret, msg=payload, digestmod=hashlib.sha256).digest()
#
#        # allow the signed_request to function for upto 1 day
#        if sig == expected_sig: # if the signature is correct
#            if (time_limit is not None and data[u'issued_at'] > (time.time() - time_limit)) or time_limit is None:
#                return data
#        
#        return None
#    
#    except ValueError:
#        return None

def post_multipart_secure(host, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    
    
    h = httplib.HTTPSConnection(host)
    headers = {"Content-type": content_type, "Content-length" : str(len(body)) }
    h.request("POST", selector, body, headers)
    
    response = h.getresponse()
    
    data = response.read()
    h.close()
    
    return data

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for key in fields.keys():
        value = fields[key]
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'