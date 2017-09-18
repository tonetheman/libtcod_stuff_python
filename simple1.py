import tcod as libtcod

WIDTH = 40
HEIGHT = 50
libtcod.console_set_custom_font("consolas12x12_gs_tc.png")
libtcod.console_init_root(WIDTH,HEIGHT,"simple1",False)
test_console = libtcod.console_new(WIDTH,HEIGHT)

key = libtcod.Key()
mouse = libtcod.Mouse()

while not libtcod.console_is_window_closed():
	libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS |
		libtcod.EVENT_MOUSE, key, mouse)

	libtcod.console_set_default_foreground(None, libtcod.grey)

	if key.vk == libtcod.KEY_ESCAPE:
		break

	libtcod.console_flush()

