function main(splash)
    splash:go("https://www.taobao.com")
    splash:wait(2)
    return {html=splash:html()}
end