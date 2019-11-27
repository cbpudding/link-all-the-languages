#![no_std]

use core::panic::PanicInfo;
use libc::{abort, puts};

#[cfg(not(test))]
#[panic_handler]
fn panic_heck(_: &PanicInfo) -> ! {
    unsafe { abort() }
}

#[no_mangle]
pub extern "C" fn hello_rust() {
    unsafe {
        puts("Hello from Rust.".as_bytes().as_ptr() as *const i8);
    }
}
