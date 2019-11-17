#![crate_type="cdylib"]
#[no_mangle]
pub extern "C" fn hello_rust() {
	println!("Hello from Rust!");
}
