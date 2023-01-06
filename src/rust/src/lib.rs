use core::ffi::c_int;

extern "C" {
    fn challenge(c: c_int) -> bool;
}

#[no_mangle]
extern "C" fn hello_rust(c: c_int) {
    println!("Hello from Rust!");
    unsafe {
        // Hide your valuables! It's an unsafe block! ~Alex
        challenge(c + 5);
    }
}