function main(splash)
    splash:set_viewport_full()
    assert(splash:go("http://cuiqingcai.com"))
    return splash:png()
end