from sanic.response import json

from .data import topics
from .helpers import get_topics


async def get_topic(request):
    text = request.args.get('text')
    result = await get_topics(topics, text)
    return json({'topics': result})
