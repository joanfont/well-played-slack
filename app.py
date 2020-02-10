import os

from starlette.applications import Starlette
from starlette.responses import Response, JSONResponse
from starlette.routing import Route


GIF_URL = 'https://media1.giphy.com/media/ZdO4NenDbsQNwUwKDB/giphy.gif'
SLACK_VERIFICATION_TOKEN = os.environ.get('SLACK_VERIFICATION_TOKEN')


async def well_played(request):
    data = await request.form()
    if data.get('token') != SLACK_VERIFICATION_TOKEN:
        return JSONResponse({
            'response_type': 'ephemeral',
            'text': 'Bad played'
        })

    return JSONResponse({
        'response_type': 'in_channel',
        'attachments': [{'image_url': GIF_URL}]
    })

app = Starlette(debug=True, routes=[
    Route('/', well_played, methods=['get', 'post']),
])