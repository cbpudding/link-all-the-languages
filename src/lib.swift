import Foundation

@_cdecl("hello_swift")
func hello_swift() {
	let current = Calendar.current
	let components = DateComponents(calendar: current)
	if components.month! == 12 {
		print("Merry Christmas from Swift!")
	} else {
		print("Hello from Swift!")
	}
}
