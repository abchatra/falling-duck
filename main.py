class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    Gap = SpriteKind.create()

def on_button_pressed():
    mySprite.vy = -100
    animation.set_action(mySprite, ActionKind.Jumping)
    mySprite.start_effect(effects.rings, 300)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_on_overlap(sprite, otherSprite):
    if otherSprite.right - sprite.left < 2:
        info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Gap, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

projectile: Sprite = None
gapSprite: Sprite = None
gapImage: Image = None
bottomImage: Image = None
topImage: Image = None
gap = 0
mySprite: Sprite = None
scene.set_background_color(9)
info.set_score(0)
effects.blizzard.start_screen_effect()
mySprite = sprites.create(assets.image("""
    duck1
"""), SpriteKind.player)
mySprite.ay = 300
anim = animation.create_animation(ActionKind.Jumping, 25)
anim.add_animation_frame(assets.image("""
    duck2
"""))
anim.add_animation_frame(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . b b b b b 5 5 5 5 5 5 5 b . . 
        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
        . . b d 5 5 b 1 f f 5 4 4 c . . 
        b b d b 5 5 5 d f b 4 4 4 4 4 b 
        b d d c d 5 5 b 5 4 4 4 4 4 b . 
        c d d d c c b 5 5 5 5 5 5 5 b . 
        c b d d d d d 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . .
"""))
anim.add_animation_frame(assets.image("""
    duck3
"""))
anim.add_animation_frame(assets.image("""
    duck4
"""))
anim.add_animation_frame(img("""
    . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 d 4 c . . 
        . . . . b 5 5 1 f f d d 4 4 4 b 
        . . . . b 5 5 d f b 4 4 4 4 b . 
        . . . b d 5 5 5 5 4 4 4 4 b . . 
        . b b d d d 5 5 5 5 5 5 5 b . . 
        b d d d b b b 5 5 5 5 5 5 5 b . 
        c d d b 5 5 d c 5 5 5 5 5 5 b . 
        c b b d 5 d c d 5 5 5 5 5 5 b . 
        c b 5 5 b c d d 5 5 5 5 5 5 b . 
        b b c c c d d d 5 5 5 5 5 d b . 
        . . . . c c d d d 5 5 5 b b . . 
        . . . . . . c c c c c b b . . .
"""))
anim.add_animation_frame(img("""
    . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 5 d f . . 
        . . . . b 5 5 1 f f 5 d 4 c . . 
        . . . . b 5 5 d f b d d 4 4 . . 
        . b b b d 5 5 5 5 5 4 4 4 4 4 b 
        b d d d b b d 5 5 4 4 4 4 4 b . 
        b b d 5 5 5 b 5 5 5 5 5 5 b . . 
        c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
        c b d c d 5 5 b 5 5 5 5 5 5 b . 
        . c d d c c b d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        . . . . . . . . . . . . . . . .
"""))
animation.attach_animation(mySprite, anim)

def on_on_update():
    if mySprite.vy > 0:
        animation.set_action(mySprite, ActionKind.Idle)
    if mySprite.bottom > 120 or mySprite.top < 0:
        game.over(False)
game.on_update(on_on_update)

def on_update_interval():
    global gap, topImage, bottomImage, gapImage, gapSprite, projectile
    gap = randint(0, 3)
    if gap == 0:
        topImage = img("""
            .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......beeeeeeeeeeb......
                        .......beeeeeeeeb.......
                        ........beeeeeeb........
        """)
        bottomImage = img("""
            ........................
                        ........................
                        ..........bbbb..........
                        ........bbddddbb........
                        .......bddbbbbddb.......
                        ......bdbbddddbbdb......
                        .....bdbbdbbbbdbbdb.....
                        .....bdbdbddddbdbdb.....
                        .....cdbbdbbbbdbbdc.....
                        .....cbdbbddddbbdbc.....
                        .....efbddbbbbddbce.....
                        .....eeffbddddbccee.....
                        .....eeeeffcccceee......
                        .....ceeeeeeeeeeee......
                        .....ceeeeeeeeeeee......
                        .....feeeeeeeeeeee......
                        .....cceeeeeeeeeee......
                        ......feeeeeeeeeee......
                        .....6fceeeeeeeeee6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6666776...
                        ..67768e67766777667776..
                        ...668ee7768867788666...
                        ......ee77eeee77ecee....
                        ......ee6eeeeee6eef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......ceeeeeeeeeecf.....
                        ......ceeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
                        ......eefeeeeeeece......
                        ......eeceeeeeeece......
                        ......eeceeeeeeefe......
                        ......eeceeeeeeefe......
                        ......eeeeeeeeeefe......
                        ......eeeeeeeeeece......
                        .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......ce6eeeeee6ee......
                        ......ceeeeeeeeeee......
                        ......fcceeeeeecee......
                        ......fccceeececce......
                        ......fcceeecceccc......
                        ......fccceecceccc......
                        ......fccccceceecc......
                        .....6fccccccccccf6.....
                        ....6776ccccccccc676....
                        ...6776676cccc6766776...
                        ..6776cc77777777667776..
                        ...668cc7768867788666...
                        ......cc77cccc67cf......
                        ......cc6cccccc6cf......
        """)
    elif gap == 1:
        topImage = img("""
            .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
                        ......eefeeeeeeece......
                        ......eeceeeeeeece......
                        ......eeceeeeeeefe......
                        ......eeceeeeeeefe......
                        ......eeeeeeeeeefe......
                        ......eeeeeeeeeece......
                        .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......beeeeeeeeeeb......
                        .......beeeeeeeeb.......
                        ........beeeeeeb........
                        ........................
                        ........................
                        ........................
        """)
        bottomImage = img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........bbbb..........
                        ........bbddddbb........
                        .......bddbbbbddb.......
                        ......bdbbddddbbdb......
                        .....bdbbdbbbbdbbdb.....
                        .....bdbdbddddbdbdb.....
                        .....cdbbdbbbbdbbdc.....
                        .....cbdbbddddbbdbc.....
                        .....efbddbbbbddbce.....
                        .....eeffbddddbccee.....
                        .....eeeeffcccceee......
                        .....ceeeeeeeeeeee......
                        .....ceeeeeeeeeeee......
                        .....feeeeeeeeeeee......
                        .....cceeeeeeeeeee......
                        ......feeeeeeeeeee......
                        .....6fceeeeeeeeee6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6666776...
                        ..67768e67766777667776..
                        ...668ee7768867788666...
                        ......ee77eeee77ecee....
                        ......ee6eeeeee6eef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......ceeeeeeeeeecf.....
                        ......ceeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
                        ......eefeeeeeeece......
                        ......eeceeeeeeece......
                        ......eeceeeeeeefe......
                        ......eeceeeeeeefe......
                        ......eeeeeeeeeefe......
                        ......eeeeeeeeeece......
                        .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......ce6eeeeee6ee......
        """)
    elif gap == 2:
        topImage = img("""
            .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67eeee....
                        ......ee6eeeeee6cef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......eeeeeeeeeeecf.....
                        ......eeeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
                        ......eefeeeeeeece......
                        ......eeceeeeeeece......
                        ......eeceeeeeeefe......
                        ......eeceeeeeeefe......
                        ......eeeeeeeeeefe......
                        ......eeeeeeeeeece......
                        .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......beeeeeeeeeeb......
                        .......beeeeeeeeb.......
                        ........beeeeeeb........
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
        """)
        bottomImage = img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........bbbb..........
                        ........bbddddbb........
                        .......bddbbbbddb.......
                        ......bdbbddddbbdb......
                        .....bdbbdbbbbdbbdb.....
                        .....bdbdbddddbdbdb.....
                        .....cdbbdbbbbdbbdc.....
                        .....cbdbbddddbbdbc.....
                        .....efbddbbbbddbce.....
                        .....eeffbddddbccee.....
                        .....eeeeffcccceee......
                        .....ceeeeeeeeeeee......
                        .....ceeeeeeeeeeee......
                        .....feeeeeeeeeeee......
                        .....cceeeeeeeeeee......
                        ......feeeeeeeeeee......
                        .....6fceeeeeeeeee6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6666776...
                        ..67768e67766777667776..
                        ...668ee7768867788666...
                        ......ee77eeee77ecee....
                        ......ee6eeeeee6eef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......ceeeeeeeeeecf.....
                        ......ceeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
        """)
    else:
        topImage = img("""
            .....6fceeeeeeeeee6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6666776...
                        ..67768e67766777667776..
                        ...668ee7768867788666...
                        ......ee77eeee77ecee....
                        ......ee6eeeeee6eef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......ceeeeeeeeeecf.....
                        ......ceeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67eeee....
                        ......ee6eeeeee6cef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeeef.....
                        ......eeeeeeeeeeecf.....
                        ......eeeeeeeeeeecf.....
                        ......eeeeeeeeeeeff.....
                        ......feeeeeeeeeefe.....
                        .....6feeeeeeeeeef6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6667776...
                        ..6776ee67777777667776..
                        ...668ee7768867788666...
                        ......ee77eeee67ee......
                        ......ee6eeeeee6ce......
                        ......eefeeeeeeece......
                        ......eeceeeeeeece......
                        ......eeceeeeeeefe......
                        ......eeceeeeeeefe......
                        ......eeeeeeeeeefe......
                        ......eeeeeeeeeece......
                        .....6eeeeeeeeeece6.....
                        ....6776eeeeeeeee676....
                        ...6776666eeee6766776...
                        ..6776ee77777777667776..
                        ...668ce7768867788666...
                        ......ce77eeee67ee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......eeeeeeeeeeee......
                        ......beeeeeeeeeeb......
                        .......beeeeeeeeb.......
                        ........beeeeeeb........
                        ........................
        """)
        bottomImage = img("""
            ........................
                        ..........bbbb..........
                        ........bbddddbb........
                        .......bddbbbbddb.......
                        ......bdbbddddbbdb......
                        .....bdbbdbbbbdbbdb.....
                        .....bdbdbddddbdbdb.....
                        .....cdbbdbbbbdbbdc.....
                        .....cbdbbddddbbdbc.....
                        .....efbddbbbbddbce.....
                        .....eeffbddddbccee.....
                        .....eeeeffcccceee......
                        .....ceeeeeeeeeeee......
                        .....ceeeeeeeeeeee......
                        .....feeeeeeeeeeee......
                        .....cceeeeeeeeeee......
                        ......feeeeeeeeeee......
                        .....6fceeeeeeeeee6.....
                        ....6776eeeeeeeee676....
                        ...6777666eeee6666776...
                        ..67768e67766777667776..
                        ...668ee7768867788666...
                        ......ee77eeee77ecee....
                        ......ee6eeeeee6eef.....
        """)
    gapImage = image.create(2, scene.screen_height())
    gapImage.fill(1)
    gapSprite = sprites.create(gapImage, SpriteKind.Gap)
    gapSprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
    gapSprite.set_flag(SpriteFlag.INVISIBLE, True)
    gapSprite.left = scene.screen_width()
    gapSprite.vx = -45
    projectile = sprites.create_projectile_from_side(topImage, -45, 0)
    projectile.top = 0
    projectile = sprites.create_projectile_from_side(bottomImage, -45, 0)
    projectile.bottom = scene.screen_height()
game.on_update_interval(1500, on_update_interval)
