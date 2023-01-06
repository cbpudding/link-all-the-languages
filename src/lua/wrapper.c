#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
#include <stdbool.h>

#include "hello.luac.h"

extern bool challenge(int c);

static int lua_challenge(lua_State *L) {
    int c = luaL_checkinteger(L, 1);
    lua_pushboolean(L, challenge(c));
    return 1;
}

void hello_lua(int c) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    lua_pushcfunction(L, lua_challenge);
    lua_setglobal(L, "challenge");
    luaL_loadbuffer(L, hello_luac, hello_luac_len, "hello.lua");
    lua_pcall(L, 0, 0, 0);
    lua_getglobal(L, "hello_lua");
    lua_pushinteger(L, c);
    lua_pcall(L, 1, 0, 0);
    lua_close(L);
}