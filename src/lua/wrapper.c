#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

#include "hello.luac.h"

void hello_lua() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_loadbuffer(L, hello_luac, hello_luac_len, "hello.lua");
    lua_pcall(L, 0, 0, 0);
    lua_getglobal(L, "hello_lua");
    lua_pcall(L, 0, 0, 0);
    lua_close(L);
}
