# C and CPP (C plus plus)

### C preprocessor

#### Macro stringizing and concatenation

```
#define NODE_LIST(V) \
  V(NodeType1) \
  V(NodeType2)

#define DECLARE_TYPE_ENUM(type) k##type,
enum NodeType {
  NODE_LIST(DECLARE_TYPE_ENUM)
};
#undef DECLARE_TYPE_ENUM

NodeType node_type;
switch (node_type) {
#define GENERATE_CASE(NodeType)             \
  case k##NodeType:                         \
    printf("NodeType is: " #NodeType "\n"); \
    break;
NODE_LIST(GENERATE_CASE)
#undef GENERATE_CASE
  default:
    break;
}
```

Refs:

* https://gcc.gnu.org/onlinedocs/cpp/Macros.html#Macros
* https://gcc.gnu.org/onlinedocs/cpp/Stringizing.html#Stringizing
* https://gcc.gnu.org/onlinedocs/cpp/Concatenation.html#Concatenation
