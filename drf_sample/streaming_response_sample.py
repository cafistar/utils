# Python 3.7.3
# Djagno 2.2
# djangorestframework 3.7.7
import time

from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view


def response200_streaming(streaming_content):
    response = StreamingHttpResponse(
        streaming_content,
        content_type='text/plain; charset=utf-8',
    )
    response['X-Content-Type-Options'] = 'nosniff'
    response['Content-Encoding'] = 'chunked'
    response['Content-Transfer-Encoding'] = 'binary'
    return response


def renkei(num):
    for i in range(1, num + 1):
        value = str(i) * i
        time.sleep(1)
        yield {
            'index': i,
            'value': value,
        }


def run():
    return renkei(5)


@api_view(['GET'])
def xxx(request):
    return response200_streaming(run())
