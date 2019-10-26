async def get_topics(topics, text):
    if text is None:
        return []

    result = set()
    text = text.lower().strip().split()
    text = set(text)

    phrases = {}
    for topic in topics:
        for phrase in topics[topic]:
            try:
                if phrases[phrase].issubset(text):
                    result.add(topic)
            except KeyError:
                phrases[phrase] = set(phrase.split())
                if phrases[phrase].issubset(text):
                    result.add(topic)

    result = list(result)
    return result
