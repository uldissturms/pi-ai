import hmac
from os import getenv
from hashlib import sha256
from urllib.parse import quote, quote_plus
from datetime import datetime

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), sha256).digest()

def getSignatureKey(key, date, region, service):
    kDate = sign(('AWS4' + key).encode('utf-8'), date)
    kRegion = sign(kDate, region)
    kService = sign(kRegion, service)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

def getSignedUrl(host, region, accessKeyId, secretAccessKey, sessionToken):
    t = datetime.utcnow()
    date_time = t.strftime('%Y%m%dT%H%M%SZ')
    date = t.strftime('%Y%m%d')

    method = 'GET'
    protocol = 'wss'
    uri = '/mqtt'
    service = 'iotdevicegateway'
    algorithm = 'AWS4-HMAC-SHA256'

    credential_scope = date + '/' + region + '/' + service + '/' + 'aws4_request'
    signed_headers = 'host'
    canonical_querystring = 'X-Amz-Algorithm=' + algorithm
    canonical_querystring += '&X-Amz-Credential=' + quote_plus(
        accessKeyId + '/' + credential_scope
    )
    canonical_querystring += '&X-Amz-Date=' + date_time
    canonical_querystring += '&X-Amz-SignedHeaders=' + signed_headers

    canonical_headers = 'host:' + host + '\n'
    payload_hash = sha256(('').encode('utf-8')).hexdigest()
    canonical_request = method + '\n' + uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    string_to_sign = algorithm + '\n' +  date_time + '\n' +  credential_scope + '\n' +  sha256(canonical_request.encode('utf-8')).hexdigest()
    signing_key = getSignatureKey(secretAccessKey, date, region, service)
    signature = hmac.new(signing_key, (string_to_sign).encode("utf-8"), sha256).hexdigest()

    canonical_querystring += '&X-Amz-Signature=' + signature
    if sessionToken:
        canonical_querystring += '&X-Amz-Security-Token=' + quote(sessionToken);

    return protocol + '://' + host + uri + "?" + canonical_querystring

request_url = getSignedUrl(
    getenv('AWS_IOT_HOST'),
    getenv('AWS_DEFAULT_REGION'),
    getenv('AWS_ACCESS_KEY_ID'),
    getenv('AWS_SECRET_ACCESS_KEY'),
    getenv('AWS_SESSION_TOKEN')
)

print(request_url)
