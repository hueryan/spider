function main(splash)
    splash:go("https://www.baidu.com/")
    splash:clear_cookies()
    return splash:get_cookies()
end