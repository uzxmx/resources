#import <Foundation/Foundation.h>
#import <zlib.h>

int main(int argc, char** argv)
{
    char dst[1024];

    bzero(dst, sizeof(dst));
    int dst_len;
    NSLog(@"Before comress");

    NSData *src = [NSData dataWithContentsOfFile:@"input.bin" options:NSDataReadingUncached error:NULL];
    NSLog(@"src len: %d", src.length);

    compress(dst, &dst_len, src.bytes, src.length);
    NSLog(@"After comress");
    NSLog(@"dst len: %d", dst_len);

    for (int i = 0; i < dst_len; i++) {
        // https://stackoverflow.com/questions/41638330/how-to-print-1-byte-with-printf
        printf("%02hhx", dst[i]);
    }

    return 0;
}
