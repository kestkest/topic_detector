import pytest


@pytest.mark.parametrize('input,expected',
                         [('', set()),
                          ('набор слов', set()),
                          ('взрыв на заводе', set(['новости'])),
                          ('летняя резина', set(['авто', 'товары']))])
async def test_server(app, test_cli, input, expected):
    response = await test_cli.get('/get_topic', params={'text': input})
    json_resp = await response.json()
    assert expected == set(json_resp['topics'])
