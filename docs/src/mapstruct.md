# MapStruct cheatsheet

## Define a global MapperConfig

```java
@MapperConfig(
    componentModel = "spring",
    nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE
)
public class MapStructConfig {
}

@Mapper(config = MapStructConfig.class)
public interface CustomerConverter {
    CustomerDTO toCustomerDTO(Customer customer);
}
```

## Map one object to another with different property names

```java
class Customer {
    private String customerName,
    private String address;
}

class CustomerDTO {
    private String name;
    private String address;
}

@Mapper(config = MapStructConfig.class)
public interface CustomerConverter {
    @Mapping(source = "customerName", target = "name")
    CustomerDTO toCustomerDTO(Customer customer);
}
```

Ref: https://www.baeldung.com/mapstruct-multiple-source-objects
