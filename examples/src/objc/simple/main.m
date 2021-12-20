#import <Foundation/Foundation.h>

void calling_conventions_parameters_demo() {
    int x = 17;
    int y = 33;
    int z = 34;
    NSString *foo = @"foo";
    NSString *bar = @"bar";

    // Below list which parameter is stored in which register or where in the stack.
    // rdi: instance
    // rsi: initWithFormat selector
    // rdx: format
    // rcx: x
    // r8: y
    // r9: z
    // (rsp): foo
    // 0x8(rsp): bar
    NSString *str = [[NSString alloc] initWithFormat:@"x: %d, y: %d, z: %d, foo: %@, bar: %@", x, y, z, foo, bar];

    NSLog(@"str: %@, len: %lu", str, str.length);
}

void calling_conventions_parameters_with_float_demo() {
    int x = 17;
    int y = 33;
    float pi = 3.1415926;
    int z = 34;
    NSString *foo = @"foo";
    NSString *bar = @"bar";

    // pi is stored in a floating register.
    NSString *str = [[NSString alloc] initWithFormat:@"x: %d, y: %d, pi: %f, foo: %@, bar: %@", x, y, pi, foo, bar];

    NSLog(@"str: %@, len: %lu", str, str.length);
}

int main(int argc, char **argv)
{
    if (argc > 1) {
        calling_conventions_parameters_demo();
    } else {
        calling_conventions_parameters_with_float_demo();
    }

    return 0;
}
