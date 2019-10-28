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
                if phrases[phrase] and topic not in result:
                    result.add(topic)
            except KeyError:
                if all([word in text for word in phrase.split()]):
                    phrases[phrase] = True
                    if topic not in result:
                        result.add(topic)
                else:
                    phrases[phrase] = False

    result = list(result)
    return result
