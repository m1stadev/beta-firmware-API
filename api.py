#!/usr/bin/env python3

import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='scraper:app', uds='ios-beta-api.sock')
