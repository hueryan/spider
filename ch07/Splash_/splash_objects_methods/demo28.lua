function main(splash)
    splash:set_viewport_size(400, 700)
    assert(splash:go("http://cuiqingcai.com"))
    return splash:png()
end