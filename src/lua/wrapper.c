#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

void hello_lua() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    // ...
    lua_close(L);
}