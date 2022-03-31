#import <Foundation/Foundation.h>

void testARC() {
    NSString *strongReference = [[NSString alloc] initWithCString:"hello, world"
                                                         encoding:NSUTF8StringEncoding];
    NSString * __weak weakReference = strongReference;
    NSLog(@"strongReference: %@", strongReference);
    NSLog(@"weakReference: %@", weakReference);
    strongReference = nil;
    NSLog(@"strongReference: %@", strongReference);
    NSLog(@"weakReference: %@", weakReference);
}

int main() {
    @autoreleasepool {
        testARC();
    }
    return 0;
}
