from sanic.response import json

from topic_detector.data import topics
from topic_detector.helpers import get_topics


async def get_topic(request):
    text = request.args.get('text')
    result = await get_topics(topics, text)
    return json({'topics': result})
