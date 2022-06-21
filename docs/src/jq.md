# jq

## Filter an array by key value

Given:

```
{
  "records": [
    { "name": "foo", "other": "bar" },
    { "name": "bar", "other": "baz" },
    { "name": "baz", "other": "bang" }
  ]
}
```

To filter out the array element with name equals to `foo`:

```
jq '.records[] | select(.name == "foo")'
```

To filter out the array elements with name containing `ba`:

```
jq '.records[] | select(.name | contains("ba"))'
```

The above output is not a valid json. To build a json array, we can change it
to:

```
jq '[.records[] | select(.name | contains("ba"))]'
```

This is equivalent to:

```
jq '.records | map(select(.name | contains("ba")))'
```

Ref: https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key

## Edit JSON

### Add field

```
echo '{"foo": 0}' | jq '. += {"bar": "baz"}'
```

### Update field

```
echo '{"foo": 0}' | jq '. += {"foo": 1}'
echo '{"foo": 0}' | jq '. += {"foo": "bar"}'
```

### Delete field

```
echo '{"foo": 0, "bar": 1}' | jq 'del(.foo)'
```

## Convert null to empty string

```
echo '{"foo": 0, "bar": 1}' | jq -r '.baz | values'
```

Ref: https://github.com/stedolan/jq/issues/354
