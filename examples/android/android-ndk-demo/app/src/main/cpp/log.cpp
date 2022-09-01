#include <android/log.h>

#include "log.hpp"

#define LOG(prio, fmt) \
    va_list args; \
    va_start(args, fmt); \
    __android_log_vprint(prio, tag, fmt, args); \
    va_end(args);

void log_debug(const char* tag, const char* fmt, ...) {
    LOG(ANDROID_LOG_DEBUG, fmt)
}

void log_info(const char* tag, const char* fmt, ...) {
    LOG(ANDROID_LOG_INFO, fmt)
}

void log_warn(const char* tag, const char* fmt, ...) {
    LOG(ANDROID_LOG_WARN, fmt)
}

void log_error(const char* tag, const char* fmt, ...) {
    LOG(ANDROID_LOG_ERROR, fmt)
}
