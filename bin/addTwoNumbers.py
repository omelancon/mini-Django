from miniDjango import start_app


def my_app(request):
    request_tokens = request.decode().split(' ')
    method = request_tokens[0]

    if method == 'GET':
        request_url = request_tokens[1]

        try:
            raw_params = request_url.split('?')[1]

            params = {p[0]: p[1] for p in [l.split('=') for l in raw_params.split('&')]}

            if 'num1' in params and 'num2' in params:
                return int(params['num1']) + int(params['num2'])
            else:
                return 'Provide parameters "num1" and "num2" to be added'
        except (ValueError, IndexError):
            return 'NaN'

    else:
        raise ValueError('Method is not GET')


if __name__ == '__main__':
    start_app(my_app)