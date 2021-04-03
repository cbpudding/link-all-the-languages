#include <lua5.3/lua.h>
#include <lua5.3/lauxlib.h>
#include <lua5.3/lualib.h>

#include "luascript.h"

void call_hello_lua() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    
    luaL_loadstring(L, hello_lua);
    lua_pcall(L, 0, LUA_MULTRET, 0);

    lua_close(L);
}
