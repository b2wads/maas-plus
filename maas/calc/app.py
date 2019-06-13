from aiohttp import web
from asyncworker import App, RouteTypes

from contrib.parser import Tree

app = App("", "", "", 1)


@app.route(["/eval"], type=RouteTypes.HTTP, methods=["POST"])
async def calc(request: web.Request):
    expr = (await request.json())["expr"]
    parser = Tree()
    parser.parse(expr)

    try:
        parser.evaluate()
    except Exception as e:
        return web.json_response(
            {
                "result": None,
                "error": {"exc": str(e), "reason": "Invalid Expression"},
            },
            status=400,
        )

    try:
        result = await parser.root.eval()
        return web.json_response({"result": result})
    except Exception as e:
        return web.json_response(
            {
                "result": None,
                "error": {
                    "exc": str(e),
                    "reason": "Error evaluating expression",
                },
            },
            status=500,
        )
