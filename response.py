def http_response(response):
    response_body = str(response)

    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(response_body),
        'Connection': 'close',
    }

    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in response_headers.items())

    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    return ('%s %s %s %s\n%s' %
            (response_proto,
             response_status,
             response_status_text,
             response_headers_raw,
             response_body)
            ).encode()


def http_error():
    response_proto = 'HTTP/1.1'
    response_status = '500'
    response_status_text = 'ERROR'

    return ('%s %s %s' %
            (response_proto,
             response_status,
             response_status_text,)
            ).encode()
