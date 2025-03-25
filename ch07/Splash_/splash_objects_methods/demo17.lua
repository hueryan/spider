function main(splash, args)
  local treat = require("treat")
  local response = splash:http_get("http://httpbin.org/get")
	return {html=treat.as_string(response.body),
    url=response.url,
    status=response.status
    }
end