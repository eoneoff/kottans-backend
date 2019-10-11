module.exports.dataHandler = (stack, list) => {

    return function(request, response) {
        const structureType = request.url.split("/")[1];
        if (request.method == "GET") {
            response.writeHead(200, {"Content-Type": "application/json"});
            response.end(JSON.stringify({"data": list.showList()}));
        } else if (request.method == "POST" || request.method == "DELETE") {
            if (request.headers["content-type"] == "application/json") {
                let body = "";
                request.on("data", chunk => body += chunk.toString());
                request.on("end", () => {
                    const data = JSON.parse(body);
                    if (isValidType(data.data)) {
                        switch (structureType) {
                        case "stack":
                            switch (request.method) {
                            case "POST":
                                stack.push(data.data);
                                response.writeHead(200);
                                response.end();
                                break;
                            case "DELETE":
                                response.writeHead(200);
                                response.end(JSON.stringify({"data": stack.pop()}));
                                break;
                            }
                            break;
                        case "list":
                            switch (request.method) {
                            case "POST":
                                if (isValidType(data.successor)) {
                                    try {
                                        list.insert(data.data, data.successor);
                                        response.writeHead(200);
                                    } catch (err) {
                                        response.writeHead(400, err.message);
                                    }
                                } else {
                                    response.writeHead(400, "Wrong data type");
                                }
                                break;
                            case "DELETE":
                                try {
                                    list.remove(data.data);
                                    response.writeHead(200);
                                } catch (err) {
                                    response.writeHead(400, err.message);
                                }
                            }
                            response.end();
                            break;
                        default:
                            response.writeHead(404, "Url not found");
                            response.end();
                            break;
                        }
                    } else {
                        response.writeHead(400, "Wrong data type");
                        response.end();
                    }
                });
            } else {
                response.writeHead(400, "Wrong content type");
                response.end();
            }
        }
    };
};

function isValidType(value) {
    return typeof(value) == "string"
        || typeof(value) == "number";
}
