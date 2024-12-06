# -*- coding: utf-8 -*-
from dataclasses import dataclass

import uvicorn
from litestar import Litestar, get
from litestar.config.cors import CORSConfig

from converter import convert_to_chs, convert_to_cht

cors_config = CORSConfig(allow_origins=["*"])


@dataclass
class QueryText:
    text: str
    to: str


@get("/convert")
async def index(query: QueryText) -> dict:
    if query.to == "chs":
        result = convert_to_chs(query.text)
    elif query.to == "cht":
        result = convert_to_cht(query.text)
    else:
        return {"msg": "invalid converter (to=cht or to=chs)"}
    return {
        "msg": "success",
        "data": {"converter": query.to, "input": query.text, "output": result},
    }


app = Litestar(
    [index],
    cors_config=cors_config,
)

if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=27272, reload=True)
