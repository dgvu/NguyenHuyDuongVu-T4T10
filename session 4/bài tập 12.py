import datetime
stop = False
while stop == False:
    x = str(datetime.datetime.now().time())
    print(x)
    if x >= "20:07:00.000000":
        stop = True
        import pyglet
        music = pyglet.resource.media('Con-Trai-Cung-K-ICM-B-Ray.mp3')
        music.play()
        pyglet.app.run()