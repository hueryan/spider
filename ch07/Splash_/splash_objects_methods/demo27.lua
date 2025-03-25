function main(splash)
    splash:go("https://www.baidu.com/")
    return splash:get_viewport_size()
end