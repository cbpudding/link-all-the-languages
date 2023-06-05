public class Hello {
    private static native boolean challenge(int c);

    public static void hello_java(int num) {
        System.out.println("Hello from Java!");
        challenge(num + 5);
    }
}