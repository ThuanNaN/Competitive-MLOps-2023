import json
import ast
import time
import uvicorn

from cfg.api_config import app_cfg

## FastAPI 
from fastapi import Request, FastAPI, Response
from uvicorn.config import LOGGING_CONFIG
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from apis.base import api_router

########## FastAPI App ##########
app = FastAPI(
    title=app_cfg.title,
    description=app_cfg.description,
    version=app_cfg.version,
    docs_url=app_cfg.docs_url,
    redoc_url=app_cfg.redoc_url
)

# Include routers
app.include_router(api_router)

# Custom response if needed
class MyMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        media_type = 'application/json'

        try:
            response = await call_next(request)

            process_time = time.time() - start_time

            if 'documentation' in request.url._url or \
                        'redoc' in request.url._url or \
                        'openapi' in request.url._url:

                return response

            response_body = b''
            async for chunk in response.body_iterator:
                response_body += chunk

            resp_body_str = response_body.decode('unicode_escape').strip('"')

            resp_str_to_dict = ast.literal_eval(resp_body_str)

            response_status = response.status_code
        except Exception as e:
            process_time = time.time() - start_time
            response_status = 500

            resp_str_to_dict = {
                'code': response_status,
                'version': app_cfg.version,
                'process_time': process_time
            } 

            print('\nError while request:')
            print(e)

        resp_dict_to_json  = json.dumps(resp_str_to_dict, indent=4)
        resp_body_json_length = len(resp_dict_to_json.encode('utf8'))

        json_headers = {
            'content-length': str(resp_body_json_length),
            'content-type': media_type,
            'X-Process-Time': str(process_time),
            'API-Version': str(app.version)
        }

        return Response(
            content=resp_dict_to_json, 
            status_code=response_status,
            headers=json_headers,
            media_type=media_type
        )

origins = [
    '*'
]

app.add_middleware(MyMiddleWare)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == '__main__':
    LOGGING_CONFIG['formatters']['access']['fmt'] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    LOGGING_CONFIG['formatters']['access']['datefmt'] = '%Y-%m-%d %H:%M:%S'

    app_name = 'main:app'
    host_ip = '0.0.0.0'
    port = 9292
    is_reload = False
    n_workers = 1
    is_debug = False

    uvicorn.run(
        app_name,
        host=host_ip,
        port=port,
        reload=is_reload,
        workers=n_workers,
        debug=is_debug
    )
