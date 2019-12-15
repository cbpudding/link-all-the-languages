#![crate_type = "staticlib"]

extern crate chrono;

use chrono::{Datelike, Local};

#[no_mangle]
pub extern fn hello_rust() {
	let current = Local::today();
	if current.month() == 12 {
		println!("Happy Holidays from Rust!");
	} else {
		println!("Hello from Rust!");
	}
}
