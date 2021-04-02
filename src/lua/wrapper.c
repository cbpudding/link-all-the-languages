#include <lua5.3/lua.h>
#include <lua5.3/lauxlib.h>
#include <lua5.3/lualib.h>

void hello_lua() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    // ...
    lua_close(L);
}